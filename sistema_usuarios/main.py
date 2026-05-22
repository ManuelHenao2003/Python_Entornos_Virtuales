from app.usuarios.gestor import (
    registrar_usuario,
    listar_usuarios,
    buscar_usuario
)

from app.config.settings import (
    APP_NAME,
    APP_VERSION,
    ADMIN_USER
)


def menu():

    print(f"\n{APP_NAME}")
    print(f"Versión: {APP_VERSION}")
    print(f"Administrador: {ADMIN_USER}")

    while True:

        print("\n===== MENÚ =====")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            listar_usuarios()

        elif opcion == "3":
            buscar_usuario()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


menu()