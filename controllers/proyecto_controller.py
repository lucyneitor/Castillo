from views.vista_proyecto import ProyectoView


class ProyectoController:
    @staticmethod
    def menu() -> None:
        while True:
            print("\n" + "=" * 35)
            print("GESTIÓN DE PROYECTOS")
            print("=" * 35)
            print("1. Listar proyectos")
            print("2. Agregar proyecto")
            print("3. Buscar proyecto")
            print("4. Actualizar proyecto")
            print("5. Eliminar proyecto")
            print("0. Volver")
            print("=" * 35)

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                ProyectoView.listar_proyectos()
            elif opcion == "2":
                ProyectoView.agregar_proyecto()
            elif opcion == "3":
                ProyectoView.buscar_proyecto()
            elif opcion == "4":
                ProyectoView.actualizar_proyecto()
            elif opcion == "5":
                ProyectoView.eliminar_proyecto()
            elif opcion == "0":
                return
            else:
                print("\nOpción no válida.")