from config.database import Database

def main() -> None:
    # 1. Inicializar la base de datos (crear tablas si no existen)
    print("Inicializando sistema...")
    db = Database()
    db.init_db()

if __name__ == "__main__":
    main()