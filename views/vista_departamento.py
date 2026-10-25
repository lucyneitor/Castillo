from models.departamento import Departamento
from models.departamentoDAO import DepartamentoDAO
from views.utils import leer_numero #hacer controllers


class DepartamentoView:
    @staticmethod
    def listar_departamentos():
        departamentos = DepartamentoDAO.obtener_todos_departamentos()
        if not departamentos:
            print("No hay departamentos registrados.")
            return

        print("\n--- LISTA DE DEPARTAMENTOS ---")
        for d in departamentos:
            print(f"ID: {d.id_departamento} | Nombre: {d.nombre} | Gerente: {d.gerente} | Presupuesto: {d.presupuesto}")

    @staticmethod
    def agregar_departamento():
        print("\n--- AGREGAR DEPARTAMENTO ---")
        try:
            id_departamento = leer_numero("ID departamento: ")
            nombre = input("Nombre: ")
            gerente = input("RUT gerente: ")
            if gerente == "":
                gerente = None
            presupuesto = leer_numero("Presupuesto: ")
        except ValueError as e:
            print(f"Error: {e}")
            return

        departamento = Departamento(id_departamento, nombre, gerente, presupuesto)

        if DepartamentoDAO.agregar_departamento(departamento):
            print("Departamento agregado correctamente.")
        else:
            print("No se pudo agregar el departamento.")

    @staticmethod
    def buscar_departamento():
        id_departamento = int(input("Ingrese ID del departamento: "))
        departamento = DepartamentoDAO.obtener_departamento_por_id(id_departamento)

        if departamento:
            print(f"\nID: {departamento.id_departamento}")
            print(f"Nombre: {departamento.nombre}")
            print(f"Gerente: {departamento.gerente}")
            print(f"Presupuesto: {departamento.presupuesto}")
        else:
            print("No se encontró el departamento.")

    @staticmethod
    def actualizar_departamento():
        id_departamento = int(input("Ingrese ID del departamento a actualizar: "))
        departamento = DepartamentoDAO.obtener_departamento_por_id(id_departamento)

        if not departamento:
            print("Departamento no encontrado.")
            return

        print("Deje vacío cualquier campo que no quiera cambiar.")
        nuevo_nombre = input(f"Nuevo nombre ({departamento.nombre}): ") or departamento.nombre
        nuevo_gerente = input(f"Nuevo gerente ({departamento.gerente}): ") or departamento.gerente
        nuevo_presupuesto = input(f"Nuevo presupuesto ({departamento.presupuesto}): ")

        if nuevo_presupuesto.strip() != "":
            departamento.presupuesto = float(nuevo_presupuesto)
        departamento.nombre = nuevo_nombre
        departamento.gerente = nuevo_gerente

        if DepartamentoDAO.actualizar_departamento(departamento):
            print("Departamento actualizado correctamente.")
        else:
            print("No se pudo actualizar el departamento.")

    @staticmethod
    def eliminar_departamento():
        id_departamento = int(input("Ingrese ID del departamento a eliminar: "))
        if DepartamentoDAO.eliminar_departamento(id_departamento):
            print("Departamento eliminado correctamente.")
        else:
            print("No se pudo eliminar el departamento.")