def validar_nombre(nombre):
    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío")
    return True


def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    if edad < 18:
        raise ValueError("El usuario debe ser mayor de edad")

    return True
