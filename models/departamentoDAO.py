from sqlite3 import Cursor
from config.database import Database
from models.Empleado import empleado
from models.departamento import Departamento

class departamentoDAO: #primer bsoquejo
    """
    Data Access Object para la entidad Paciente.
    Maneja todas las operaciones CRUD en la base de datos.
    """
    @staticmethod
    def agregar_departamento(departamento: Departamento) -> bool:
        """
        Agrega un nuevo departamento a la base de datos.
        """
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO departamento (id_departamento, nombre, gerente, presupuesto)
                VALUES (?, ?, ?, ?)
            """, (departamento.id_departamento, departamento.nombre, departamento.gerente, departamento.presupuesto))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar departamento en BD: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod #revisar
    def obtener_todos_departamentos() -> list:
        """
        Obtiene todos los departamentos de la base de datos.
        """
        db = Database()
        conn = db.get_connection()
        cursor: Cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM departamento")
            departamentos = cursor.fetchall()
            return departamentos
        except Exception as e:
            print(f"Error al obtener departamentos de BD: {e}")
            return []
        finally:
            conn.close()
    @staticmethod
    def obtener_departamento_por_id(id_departamento: int) -> Departamento:
        """
        Obtiene un departamento de la base de datos por su ID.
        """
        db = Database()
        conn = db.get_connection()
        cursor: Cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM departamento WHERE id_departamento = ?", (id_departamento,))
            departamento_data = cursor.fetchone()
            if departamento_data:
                return Departamento(*departamento_data)
        except Exception as e:
            print(f"Error al obtener departamento por ID de BD: {e}")
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