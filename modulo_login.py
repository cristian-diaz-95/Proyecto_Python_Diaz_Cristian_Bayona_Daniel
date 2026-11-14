import json
ruta="D:\\Users\\CRISTIAN DBAY\\Desktop\\curso de python\\python\\proyecto #1\\"
nom_arch=ruta+"base_datos.json"

def validacion_usuario(email):
    try:
        with open (nom_arch,"r",encoding="utf-8") as arch:
            datos=json.load(arch)
        posicion=0
        for usuario in datos["usuarios"]:
            if email==usuario["email"]:
                return posicion
            posicion=posicion+1
        print("el usuario ingresado no existe")
        return None
    except ValueError:
        print("el usuario ingresado no existe")

def validacion_contrasena(posicion,contrasena):
    if posicion== None:
        return False
    with open (nom_arch,"r",encoding="utf-8") as arch:
        datos=json.load(arch)
    contra_base=datos["usuarios"][posicion]["contrasena"]
    if contra_base==contrasena:
        print("ingreso exitoso")
    else:
        print("contrasena incorrecta")
        return False




