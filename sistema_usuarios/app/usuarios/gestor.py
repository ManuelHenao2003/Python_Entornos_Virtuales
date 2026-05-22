from app.usuarios.validaciones import validar_nombre, validar_edad

usuarios = []


def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre: ")
        validar_nombre(nombre)

        edad = int(input("Ingrese la edad: "))
        validar_edad(edad)

        usuario = {
            "nombre": nombre,
            "edad": edad
        }

        usuarios.append(usuario)

        print("Usuario registrado correctamente")

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios():
    if len(usuarios) == 0:
        print("No hay usuarios registrados")
        return

    print("\nLISTA DE USUARIOS")

    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario['nombre']} - {usuario['edad']} años")


def buscar_usuario():
    nombre_buscar = input("Ingrese el nombre a buscar: ")

    encontrado = False

    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre_buscar.lower():
            print("Usuario encontrado:")
            print(usuario)
            encontrado = True

    if not encontrado:
        print("Usuario no encontrado")
