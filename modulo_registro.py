import random
import json
ruta="D:\\Users\\CRISTIAN DBAY\\Desktop\\curso de python\\python\\proyecto #1\\"
nom_arch=ruta+"base_datos.json"
def ingresar_usuario():
    ROLES=("admin","medico")
    identificacion=((input("Ingrese el numero de identificacion: ")))
    nombre=input("ingrese el nombre del usuario: ")
    apellidos=input("ingrese los apellidos del usuario: ")
    email=input("ingrese el email del usuario: ")
    direccion=input("ingrese la direccion del usuario: ")
    telefono= (input("ingrese el numero de telefono del usuario: "))
    while True:
        rol=input("ingrese el rol admin o medico: ").strip().lower()
        if rol in ROLES:
            break
        else:
            print("rol invalido\n ingresa admin o medico")
    
    contrasena=""   
    for i in range (8):
        digitos=random.randint(0,9)
        contrasena+=str(digitos)
    print(contrasena)
    print(f"creacion de usuario exitosa\n su usuario es {email} y su contrasena es {contrasena}")
    info_usuario={
        'identificacion':identificacion,
        'nombre':nombre,
        'apellidos':apellidos,
        'email':email,
        'direccion':direccion,
        'telefono':telefono,
        'contrasena':contrasena,
        'rol':rol} 
    return info_usuario
def crear_base_usuario():
    try:
        with open (nom_arch,"r",encoding="utf-8") as arch:
            datos=json.load(arch)
    except (FileNotFoundError,json.JSONDecodeError):
        with open (nom_arch,"w",encoding="utf-8") as arch:
            json.dump({"usuarios":[]},arch,indent=4)
def cargar_usuario_credenciales(info_usuario):
    with open (nom_arch,"r",encoding="utf-8") as arch:
        datos = json.load(arch)
        usuario_ex=False
        for usuario in datos["usuarios"]:
            if usuario["identificacion"]==info_usuario["identificacion"]:
                usuario_ex=True
                break
        if usuario_ex==False:
            datos["usuarios"].append(info_usuario)
            with open (nom_arch,"w",encoding="utf-8") as arch:
                json.dump(datos,arch,indent=4)
        else:
            print("el usuario ya existe se procede a cancelar el proceso")
                    
