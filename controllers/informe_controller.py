from views.Vista_informe import InformeView


class InformeController:
    @staticmethod
    def menu() -> None:
        while True:
            print("\n" + "=" * 35)
            print("INFORMES")
            print("=" * 35)
            print("1. Informe de empleados")
            print("2. Informe de departamentos")
            print("3. Tiempos por proyecto")
            print("0. Volver")
            print("=" * 35)

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                InformeView.mostrar_empleados()
            elif opcion == "2":
                InformeView.mostrar_departamentos()
            elif opcion == "3":
                InformeView.mostrar_tiempos_por_proyecto()
            elif opcion == "0":
                return
            else:
                print("\nOpción no válida.")