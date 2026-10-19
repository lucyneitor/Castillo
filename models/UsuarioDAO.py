"""

REVISAR, SE LO PEDI A LA IA PERO HAY QUE VERLO BIEN

"""


import hashlib
import secrets
import sqlite3
from contextlib import closing

from config.database import Database
from models.Usuario import Usuario


class UsuarioDAO:
    """Operaciones de persistencia para las cuentas de usuario."""

    _PBKDF2_ITERATIONS = 600_000

    def __init__(self) -> None:
        self._database = Database()

    def guardar(self, usuario: Usuario, rut: str) -> int:
        """Guarda una cuenta vinculada a un empleado y devuelve su identificador."""
        if not isinstance(rut, str) or not rut.strip():
            raise ValueError("El RUT del empleado es obligatorio.")
        rut = rut.strip()

        with closing(self._database.get_connection()) as conn:
            with conn:
                if conn.execute(
                    "SELECT 1 FROM empleado WHERE rut = ?", (rut,)
                ).fetchone() is None:
                    raise ValueError("No existe un empleado con ese RUT.")

                if conn.execute(
                    "SELECT 1 FROM usuario WHERE user = ? COLLATE NOCASE",
                    (usuario.usuario,),
                ).fetchone() is not None:
                    raise ValueError("Ese nombre de usuario ya está registrado.")

                contrasenia_hash = self._hash_password(usuario.contrasena)
                try:
                    cursor = conn.execute(
                        """
                        INSERT INTO usuario (user, contrasenia, rut)
                        VALUES (?, ?, ?)
                        """,
                        (usuario.usuario, contrasenia_hash, rut),
                    )
                except sqlite3.IntegrityError as error:
                    if conn.execute(
                        "SELECT 1 FROM usuario WHERE user = ? COLLATE NOCASE",
                        (usuario.usuario,),
                    ).fetchone() is not None:
                        raise ValueError(
                            "Ese nombre de usuario ya está registrado."
                        ) from error
                    raise
                return int(cursor.lastrowid)

    @classmethod
    def _hash_password(cls, contrasena: str) -> str:
        salt = secrets.token_bytes(16)
        digest = hashlib.pbkdf2_hmac(
            "sha256",
            contrasena.encode("utf-8"),
            salt,
            cls._PBKDF2_ITERATIONS,
        )
        return (
            f"pbkdf2_sha256${cls._PBKDF2_ITERATIONS}"
            f"${salt.hex()}${digest.hex()}"
        )
