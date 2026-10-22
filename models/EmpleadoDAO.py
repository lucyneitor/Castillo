from sqlite3 import Cursor
from config.database import Database
from models.Empleado import empleado

class EmpleadoDAO:
    def __init__(self):
        self.db = Database()
    """
    Data Access Object para la entidad Paciente.
    Maneja todas las operaciones CRUD en la base de datos.
    """
    def agregar_empleado(empleado: empleado) -> bool:
        """
        Agrega un nuevo empleado a la base de datos.
        """
        conn = self.db.get_connection()
        cursor: Cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO empleado (rut, nombre, direccion, telefono, correo, user, password, area_trabajo, sueldo, inicio_contrato, rol_admin, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (empleado.rut, empleado.nombre, empleado.direccion, empleado.telefono,
                  empleado.correo, empleado.user, empleado.password,
                  empleado.area_trabajo, empleado.sueldo,
                  empleado.inicio_contrato, empleado.rol_admin, empleado.estado))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar empleado en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod #revisar
    def obtener_todos_empleados() -> list:
        """
        Obtiene todos los empleados de la base de datos.
        """
        db = Database()
        conn = db.get_connection()
        cursor: Cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM empleado")
            empleados = cursor.fetchall()
            return empleados
        except Exception as e:
            print(f"Error al obtener empleados de BD: {e}")
            return []
        finally:
            conn.close()
    @staticmethod
    def obtener_empleado_por_rut(rut: str) -> empleado:
        """
        Obtiene un empleado de la base de datos por su RUT.
        """
        db = Database()
        conn = db.get_connection()
        cursor: Cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM empleado WHERE rut = ?", (rut,))
            empleado_data = cursor.fetchone()
            if empleado_data: #corregir
                return empleado(*empleado_data)   
        except Exception as e:
            print(f"Error al obtener empleado por RUT de BD: {e}")
        finally:
            conn.close()
    @staticmethod #revisar
    def actualizar_empleado(empleado: empleado) -> bool:
        """
        Actualiza los datos de un empleado en la base de datos.
        """
        db = Database()
        conn = db.get_connection()
        cursor: Cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE empleado
                SET nombre = ?, direccion = ?, telefono = ?, correo = ?, user = ?, password = ?,
                    area_trabajo = ?, sueldo = ?, inicio_contrato = ?, rol_admin = ?, estado = ?
                WHERE rut = ?
            """, (empleado.nombre, empleado.direccion, empleado.telefono, empleado.correo,
                  empleado.user, empleado.password, empleado.area_trabajo, empleado.sueldo,
                  empleado.inicio_contrato, empleado.rol_admin, empleado.estado, empleado.rut))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar empleado en BD: {e}")
            return False
        finally:
            conn.close()
    @staticmethod # revisar
    def eliminar_empleado(rut: str) -> bool:
        """
        Elimina un empleado de la base de datos por su RUT.
        """
        db = Database()
        conn = db.get_connection()
        cursor: Cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM empleado WHERE rut = ?", (rut,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar empleado de BD: {e}")
            return False
        finally:
            conn.close()