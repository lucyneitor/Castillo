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
            print("3. Crear un nuevo empleado")
            print("0. Volver al menú anterior")
            print("-" * 35)

            opcion = leer_numero("Seleccione una opción: ")

            if opcion == 1:
                VistaEmpleado.mostrar_empleados()
            elif opcion == 2:
                VistaEmpleado.modificar_empleado()
            elif opcion == 3:
                VistaEmpleado.crear_empleado()
            elif opcion == 0:
                return
            else:
                print("\nOpción no válida. Seleccione 1, 2, 3 o 0.")

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
    def crear_empleado() -> None:
        print("\n" + "-" * 35)
        print("CREAR NUEVO EMPLEADO")
        print("-" * 35)

        while True:
            rut = input("RUT: ").strip()
            if rut:
                break
            print("El RUT no puede estar vacío.")

        while True:
            nombre = input("Nombre: ").strip()
            if len(nombre) >= 3:
                break
            print("El nombre debe tener al menos 3 caracteres.")

        direccion = input("Dirección: ").strip()
        while True:
            telefono = input("Teléfono: ").strip()
            if telefono:
                break
            print("El teléfono no puede estar vacío.")

        while True:
            correo = input("Correo: ").strip()
            if "@" in correo and "." in correo:
                break
            print("Correo inválido. Debe incluir '@' y dominio.")

        while True:
            user = input("Usuario: ").strip()
            if user:
                break
            print("El usuario no puede estar vacío.")

        password = input("Contraseña: ").strip()
        if not password:
            print("La contraseña no puede estar vacía.")
            return

        while True:
            try:
                id_departamento = int(input("ID departamento: ").strip())
                if id_departamento > 0:
                    break
                print("Debe ingresar un ID mayor a 0.")
            except ValueError:
                print("Debe ingresar un número entero válido.")

        while True:
            try:
                sueldo = int(input("Sueldo: ").strip())
                if sueldo > 0:
                    break
                print("El sueldo debe ser mayor que 0.")
            except ValueError:
                print("Debe ingresar un número entero válido.")

        while True:
            valor = input("Inicio de contrato (AAAA-MM-DD): ").strip()
            if not valor:
                print("La fecha de inicio no puede estar vacía.")
                continue
            try:
                inicio_contrato = date.fromisoformat(valor)
                break
            except ValueError:
                print("Fecha inválida. Use el formato AAAA-MM-DD.")

        while True:
            rol_admin = input("¿Es administrador? (s/n): ").strip().lower()
            if rol_admin in ("s", "si", "sí"):
                rol_admin = True
                break
            if rol_admin in ("n", "no"):
                rol_admin = False
                break
            print("Responda s o n.")

        while True:
            estado = input(f"Estado ({', '.join(ESTADO)}): ").strip().lower()
            if estado in ESTADO:
                break
            print(f"Estado inválido. Elija uno de estos valores: {', '.join(ESTADO)}")

        try:
            nuevo_empleado = empleado(
                id_departamento=id_departamento,
                sueldo=sueldo,
                inicio_contrato=inicio_contrato,
                rut=rut,
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                correo=correo,
                user=user,
                password=password,
                rol_admin=rol_admin,
                estado=estado
            )

            guardado = EmpleadoDAO.agregar_empleado(nuevo_empleado)

            if guardado:
                print("\nEmpleado registrado correctamente.")
            else:
                print("\nNo se pudo registrar el empleado.")

        except ValueError as error:
            print(f"\nError al crear el empleado: {error}")
        except sqlite3.Error as error:
            print(f"\nError al guardar el empleado en BD: {error}")
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


    @staticmethod
    def crear_empleado() -> None:
        print("\n" + "=" * 35)
        print("REGISTRAR NUEVO EMPLEADO")
        print("=" * 35)

        # 1. Capturar datos personales
        rut = VistaEmpleado._leer_texto_nuevo("RUT")
        nombre = VistaEmpleado._leer_texto_nuevo("Nombre")
        direccion = VistaEmpleado._leer_texto_nuevo("Dirección")
        telefono = VistaEmpleado._leer_texto_nuevo("Teléfono")
        correo = VistaEmpleado._leer_texto_nuevo("Correo")
        user = VistaEmpleado._leer_texto_nuevo("Usuario")
        password = VistaEmpleado._leer_texto_nuevo("Contraseña")

        # 2. Capturar datos laborales
        id_departamento = VistaEmpleado._leer_entero_nuevo(
            "ID del departamento"
        )
        sueldo = VistaEmpleado._leer_entero_nuevo("Sueldo")
        inicio_contrato = VistaEmpleado._leer_fecha_nueva()
        rol_admin = VistaEmpleado._leer_rol_nuevo()
        estado = VistaEmpleado._leer_estado_nuevo()

        # 3. Crear el objeto empleado
        try:
            nuevo_empleado = empleado(
                id_departamento,
                sueldo,
                inicio_contrato,
                rut,
                nombre,
                direccion,
                telefono,
                correo,
                user,
                password,
                rol_admin,
                estado
            )
        except (ValueError, TypeError) as error:
            print(f"\nNo se pudo crear el empleado: {error}")
            return

        # 4. Confirmar los datos antes de guardar
        print("\nResumen del nuevo empleado:")
        print(nuevo_empleado.mostrar_detalle())

        confirmar = input(
            "\n¿Desea registrar este empleado? (s/n): "
        ).strip().lower()

        if confirmar not in ("s", "si", "sí"):
            print("Registro cancelado.")
            return

        # 5. Guardar mediante el DAO
        try:
            registrado = EmpleadoDAO.agregar_empleado(nuevo_empleado)
        except sqlite3.Error as error:
            print(f"\nError al registrar el empleado: {error}")
            return

        if registrado:
            print("\nEmpleado registrado correctamente.")
        else:
            print(
                "\nNo se pudo registrar el empleado. "
                "Compruebe los datos y que el departamento exista."
            )

    @staticmethod
    def _leer_texto_nuevo(etiqueta: str) -> str:
        while True:
            valor = input(f"{etiqueta}: ").strip()

            if valor:
                return valor

            print(f"{etiqueta} no puede estar vacío.")

    @staticmethod
    def _leer_entero_nuevo(etiqueta: str) -> int:
        while True:
            valor = input(f"{etiqueta}: ").strip()

            try:
                numero = int(valor)

                if numero < 0:
                    raise ValueError

                return numero

            except ValueError:
                print("Ingrese un entero igual o mayor que cero.")

    @staticmethod
    def _leer_fecha_nueva() -> date:
        while True:
            valor = input(
                "Inicio de contrato (AAAA-MM-DD): "
            ).strip()

            try:
                return date.fromisoformat(valor)

            except ValueError:
                print("Fecha inválida. Use el formato AAAA-MM-DD.")

    @staticmethod
    def _leer_rol_nuevo() -> bool:
        while True:
            valor = input(
                "¿Es administrador? (s/n): "
            ).strip().lower()

            if valor in ("s", "si", "sí"):
                return True

            if valor in ("n", "no"):
                return False

            print("Responda s o n.")

    @staticmethod
    def _leer_estado_nuevo() -> str:
        opciones = ", ".join(ESTADO)

        while True:
            valor = input(
                f"Estado ({opciones}): "
            ).strip().lower()

            if valor in ESTADO:
                return valor

            print(f"Estado inválido. Opciones: {opciones}.")
