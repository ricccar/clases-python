"""Ejercicio - registro de usuarios
 Tendremos una lista de usuarios
 
usuarios = ["joaquin", "ana", "maria", "pablo"]
 
y queremos un sistema que nos pida un usuario, si el usuario ya existe, se le dice que ya existe y no se añade, si no existe, se añade y se notifica (y damos el total de usuarios)
 
punto extra:
 
en vez de pedir un usuario, pedimos los usuarios que queramos, hasta poner STOP
 """
usuarios = ["joaquin", "ana", "maria", "pablo"]



usuario = input("Introduce un usuario: ")

if usuario.lower() in usuarios:
    print("El usuario ya exite")
else:
    usuarios.append(usuario.lower())
    print("El usuario ha sido añadido")
