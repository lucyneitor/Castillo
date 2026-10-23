from models.Empleado import empleado
from views.utils import leer_numero

class VistaEmpleado:
    def vista_empleado():
        print("\n" + "-"*30)
        print("Accesos Empleado")
        print("-"*30)
        print("1. Ver informacion Empleado")
        print("2. modificar informacion Empleado")
        print("0. Volver al menu anterior")
        print("-"*30)
        return leer_numero("Seleccione una opción: ")

    if leer_numero == 1:
            print(mostrar_empleado())
    elif leer_numero == 2:
            print(modificar_empleado())
    elif leer_numero == 0:
            print(menu_pendiente())

def modificar_empleado():
    print(id_empleado())

def mostrar_empleado():
    print(informacion_empleado())

def informacion_empleado():
    print(area_trabajo()) 
    print(sueldo)

def menu_pendiente():
      print("xd")