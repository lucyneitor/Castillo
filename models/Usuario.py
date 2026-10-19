class Usuario:
    """
    Credenciales de un usuario para iniciar sesión.
    """

    def __init__(self, usuario: str, contrasena: str) -> None:
        self.usuario = usuario
        self.contrasena = contrasena

    @property
    def usuario(self) -> str:
        return self._usuario

    @usuario.setter
    def usuario(self, usuario: str) -> None:
        if not isinstance(usuario, str) or len(usuario.strip()) < 3:
            raise ValueError("El nombre del usuario debe tener al menos 3 caracteres.")
        self._usuario = usuario.strip()

    @property
    def contrasena(self) -> str:
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena: str) -> None:
        if (
            not isinstance(contrasena, str)
            or not contrasena.strip()
            or len(contrasena) < 8
        ):
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        self._contrasena = contrasena