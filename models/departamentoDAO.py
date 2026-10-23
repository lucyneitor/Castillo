from sqlite3 import Cursor, sqlite3
from config.database import Database
from models.Empleado import empleado
from models.departamento import Departamento

class departamentodao: #primer bsoquejo
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
            cursor.execute(
                """
                INSERT INTO departamento (id_departamento, nombre, gerente, presupuesto)
                VALUES (?, ?, ?, ?)
                """, 
                (
                    departamento.id_departamento, departamento.nombre, departamento.gerente, 
                    departamento.presupuesto
                )
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar departamento en BD: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod #revisar
    def obtener_todos_departamentos() -> list[Departamento]:
        """
        Obtiene todos los departamentos de la base de datos.
        """
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            departamentos = []
            cursor.execute(
                """
                SELECT id_departamento, nombre, e.nombre, presupuesto
                FROM departamento d, empleado e
                WHERE d.gerente = e.rut
                """
            )
            departamentos = cursor.fetchall()
            for fila in departamentos:
                departamentos.append(Departamento([fila['id_departamento'], fila['nombre'], fila['gerente'], fila['presupuesto']]))
        except Exception as e:
            print(f"Error al obtener departamentos de BD: {e}")
            return None
        finally:
            conn.close()
        return departamentos
    
    @staticmethod
    def obtener_departamento_por_id(id_departamento: int) -> Departamento:
        """
        Obtiene un departamento de la base de datos por su ID.
        """
        conn = Database().get_connection()
        departamentos = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                SELECT nombre, gerente, presupuesto 
                FROM departamento WHERE id_departamento = ?
                """, (id_departamento,)
            )
            filas = cursor.fetchall()
            for fila in filas:
                departamentos.append(Departamento([fila['id_departamento'], fila['nombre'], fila['gerente'], fila['presupuesto']]))
        except Exception as e:
            print(f"Error al obtener departamento por ID de BD: {e}")
        finally:
            conn.close()
        return departamentos
    
    @staticmethod #revisar
    def actualizar_departamento(departamento: Departamento) -> bool:
        """
        Actualiza los datos de un departamento en la base de datos.
        """
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE departamento
                SET nombre = ?, gerente = ?, presupuesto = ?
                WHERE id_departamento = ?
                """, 
                    (
                        departamento.nombre, departamento.gerente, departamento.presupuesto, departamento.id_departamento
                    )
                )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar departamento en BD: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod # revisar
    def eliminar_departamento(id_departamento: int) -> bool:
        """
        Elimina un departamento de la base de datos por su ID.
        """
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM departamento WHERE id_departamento = ?", (id_departamento,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar departamento de BD: {e}")
            return False
        finally:
            conn.close()