from sqlite3 import Cursor
from config.database import Database
from models.persona import Persona
from models.Empleado import empleado

class EmpleadoDAO:
    def __init__(self):
        self.db = Database()

    def agregar_empleado(self, empleado: empleado) -> None:
        """
        Agrega un nuevo empleado a la base de datos.
        """
        conn = self.db.get_connection()
        cursor: Cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO empleado (rut, nombre, direccion, telefono, correo, user, password, area_trabajo, sueldo, inicio_contrato, rol_admin)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (Persona.rut, Persona.nombre, Persona.direccion, Persona.telefono,
                Persona.correo, Persona.user, Persona.password,
                empleado.area_trabajo, empleado.sueldo,
                empleado.inicio_contrato.isoformat(), empleado.rol_admin))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar empleado en BD: {e}")
            return False
        finally:
            conn.close()

        #continuara