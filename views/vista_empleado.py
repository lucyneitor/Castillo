import sqlite3
from datetime import date

from models.Empleado import ESTADO, empleado
from models.EmpleadoDAO import EmpleadoDAO
from views.utils import leer_numero


class VistaEmpleado:
    @staticmethod
    def vista_empleado() -> None:
        while True:
            print("\n" + "-" * 35)
            print("GESTIÓN DE EMPLEADOS")
            print("-" * 35)
            print("1. Ver información de empleados")
            print("2. Modificar información de un empleado")
            print("0. Volver al menú anterior")
            print("-" * 35)

            opcion = leer_numero("Seleccione una opción: ")

            if opcion == 1:
                VistaEmpleado.mostrar_empleados()
            elif opcion == 2:
                VistaEmpleado.modificar_empleado()
            elif opcion == 0:
                return
            else:
                print("\nOpción no válida. Seleccione 1, 2 o 0.")

    @staticmethod
    def mostrar_empleados() -> None:
        try:
            empleados: list[empleado] = EmpleadoDAO.obtener_todos_empleados()
        except sqlite3.Error as error:
            print(f"\nNo se pudieron consultar los empleados: {error}")
            return

        if not empleados:
            print("\nNo hay empleados para mostrar.")
            return

        print(f"\nEmpleados encontrados: {len(empleados)}")
        print("=" * 45)
        for persona in empleados:
            print(persona.mostrar_detalle())
            print("-" * 45)

    @staticmethod
    def modificar_empleado() -> None:
        rut = input("\nIngrese el RUT del empleado que desea modificar: ").strip()
        if not rut:
            print("El RUT no puede estar vacío.")
            return

        try:
            persona = EmpleadoDAO.obtener_empleado_por_rut(rut)
        except (sqlite3.Error, ValueError) as error:
            print(f"\nNo se pudo consultar el empleado: {error}")
            return

        if persona is None:
            print(f"\nNo se encontró un empleado con RUT {rut}.")
            return

        print("\nDatos actuales:")
        print(persona.mostrar_detalle())
        print("\nDeje el campo vacío y presione Enter para conservar el valor actual.")

        persona.nombre = VistaEmpleado._leer_texto("Nombre", persona.nombre)
        persona.direccion = VistaEmpleado._leer_texto("Dirección", persona.direccion)
        persona.telefono = VistaEmpleado._leer_texto("Teléfono", persona.telefono)
        persona.correo = VistaEmpleado._leer_texto("Correo", persona.correo)
        persona.id_departamento = VistaEmpleado._leer_entero(
            "ID de departamento", persona.id_departamento
        )
        persona.sueldo = VistaEmpleado._leer_entero("Sueldo", persona.sueldo)
        persona.inicio_contrato = VistaEmpleado._leer_fecha(persona.inicio_contrato)
        persona.rol_admin = VistaEmpleado._leer_rol(persona.rol_admin)
        persona.estado = VistaEmpleado._leer_estado(persona.estado)

        confirmar = input("\n¿Guardar los cambios? (s/n): ").strip().lower()
        if confirmar not in ("s", "si", "sí"):
            print("Cambios descartados.")
            return

        try:
            actualizado = EmpleadoDAO.actualizar_empleado(persona)
        except sqlite3.Error as error:
            print(f"\nNo se pudieron guardar los cambios: {error}")
            return

        if actualizado:
            print("Información del empleado actualizada correctamente.")
        else:
            print("No se actualizaron los datos. Verifique que el empleado exista.")

    @staticmethod
    def _leer_texto(etiqueta: str, actual: str) -> str:
        valor = input(f"{etiqueta} [{actual}]: ").strip()
        return valor or actual

    @staticmethod
    def _leer_entero(etiqueta: str, actual: int) -> int:
        while True:
            valor = input(f"{etiqueta} [{actual}]: ").strip()
            if not valor:
                return actual
            try:
                numero = int(valor)
                if numero < 0:
                    raise ValueError
                return numero
            except ValueError:
                print("Ingrese un número entero igual o mayor que cero.")

    @staticmethod
    def _leer_fecha(actual: date) -> date:
        while True:
            valor = input(f"Inicio de contrato [{actual.isoformat()}] (AAAA-MM-DD): ").strip()
            if not valor:
                return actual
            try:
                return date.fromisoformat(valor)
            except ValueError:
                print("Fecha inválida. Use el formato AAAA-MM-DD.")

    @staticmethod
    def _leer_rol(actual: bool) -> bool:
        valor_actual = "s" if actual else "n"
        while True:
            valor = input(
                f"¿Es administrador? (s/n) [{valor_actual}]: "
            ).strip().lower()
            if not valor:
                return actual
            if valor in ("s", "si", "sí"):
                return True
            if valor in ("n", "no"):
                return False
            print("Responda s o n.")

    @staticmethod
    def _leer_estado(actual: str) -> str:
        opciones = ", ".join(ESTADO)
        while True:
            valor = input(f"Estado ({opciones}) [{actual}]: ").strip().lower()
            if not valor:
                return actual
            if valor in ESTADO:
                return valor
            print(f"Estado inválido. Elija uno de estos valores: {opciones}.")
