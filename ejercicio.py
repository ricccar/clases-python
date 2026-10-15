# Crear un sistema de usuarios con contraseñas y emails
usuarios = {
    1: {
        "nombre": "Juan",
        "contraseña": "abc123!",
        "email": "test@test.com"
    },
    2: {
        "nombre": "Marta",
        "contraseña": "1234",
        "email": "marta@test.com"
    },
    3: {
        "nombre": "Joaquin",
        "contraseña": "666",
        "email": "joa_profe@test.com"
    },
    4: {
        "nombre": "Ana",
        "contraseña": "kjabsdk",
        "email": None
    }
}

# Logica de programacion
mi_usuario = input("Pon tu usuario: ")
mi_contrasena = input("Pon tu contraseña: ")
usuario_encontrado = False
for usuario in usuarios.values():
    if mi_usuario.lower() == usuario["nombre"].lower():
        usuario_encontrado = True
        if mi_contrasena == usuario["contraseña"]:
            print("Usuario y contraseña correctos!")
            break
        else:
            print("La contraseña no fue correcta!")
        if not usuario["email"]:  # Si no tenemos un email
            nuevo_email = input("Tu usuario no tiene email, crea uno!\n")
            if nuevo_email.count("@") == 1:  # todo bien!
                usuario["email"] = nuevo_email
            else:
                print("Ese email no fue valido!")

if not usuario_encontrado:
    print("El usuario no se encontro")
