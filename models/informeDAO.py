from sqlite3 import Cursor
from config.database import Database
from models.Empleado import empleado
from models.departamento import Departamento
from models.Proyecto import Proyecto
from models.Tiempo import Tiempo 
from models.informe import Informe

class informeDAO:

    def obtenerEmpleadoDepto(informe: Informe)-> bool:
        conn = Database().get_connection()
        informe:None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT e.nombre, e.sueldo, e.inicio_contrato,d.nombre" \
            "from empleado e, departamento d" \
            "where e.id_departamento = d.departamento")
        except Exception as e:
            print(f"Error al obtener informe en BD: {e}")
            return False
        finally:
            conn.close()