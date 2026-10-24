from config.database import Database
from controllers.main_controller import MainController
def main() -> None:
    # 1. Inicializar la base de datos (crear tablas si no existen)
    print("Inicializando sistema...")
    db = Database()
    db.init_db()
    MainController.iniciar()
    
if __name__ == "__main__":
    main()