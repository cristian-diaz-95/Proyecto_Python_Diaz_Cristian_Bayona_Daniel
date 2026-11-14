import json
ruta="D:\\Users\\CRISTIAN DBAY\\Desktop\\curso de python\\python\\proyecto #1\\"
nom_arch=ruta+"base_datos.json"

def ingresar_paciente():
    identificacion=((input("Ingrese el numero de identificacion del paciente: ")))
    nombre=input("ingrese el nombre del paciente: ")
    apellidos=input("ingrese los apellidos del paciente: ")
    email=input("ingrese el email del paciente: ")
    direccion=input("ingrese la direccion del paciente: ")
    telefono= (input("ingrese el numero de telefono del paciente: "))
    genero=input("ingrese el genero del paciente: ")
    estado_civil=input("ingrese el estado civil del paciente: ")
    print(f"creacion del paciente {nombre} identificado con el numero {identificacion} ha sido exitosa")
    info_paciente={
        'identificacion':identificacion,
        'nombre':nombre,
        'apellidos':apellidos,
        'email':email,
        'direccion':direccion,
        'telefono':telefono,
        'genero':genero,
        'estado civil':estado_civil        
        }
    return info_paciente
def crear_base_paciente():
    with open (nom_arch,"r",encoding="utf-8") as arch:
                datos=json.load(arch)
                datos["pacientes"] = []
    with open (nom_arch,"w",encoding="utf-8") as arch:
                    json.dump(datos,arch,indent=4)
def cargar_paciente(info_paciente):
    with open (nom_arch,"r",encoding="utf-8") as arch:
            datos = json.load(arch)
            paciente_ex=False
            for paciente in datos["pacientes"]:
                if paciente ["identificacion"]==info_paciente["identificacion"]:
                    paciente_ex=True
                    break
            if paciente_ex==False:
                datos["pacientes"].append(info_paciente)
                with open (nom_arch,"w",encoding="utf-8") as arch:
                    json.dump(datos,arch,indent=4)
            else:
                print("el paciente ya existe se procede a cancelar el proceso")
    
def crear_base_diagnostico():
    with open (nom_arch,"r",encoding="utf-8") as arch:
                datos=json.load(arch)
                datos["diagnosticos"] = []
    with open (nom_arch,"w",encoding="utf-8") as arch:
                    json.dump(datos,arch,indent=4)

def verificacion_paciente(identificacion):
    with open (nom_arch,"r",encoding="utf-8") as arch:
        datos=json.load(arch)
        posicion=0
        for paciente in datos["pacientes"]:
            if identificacion==paciente["identificacion"]:
                return posicion
            posicion=posicion+1
        print("el paciente no esta registrado")
        return None

def extraccion_doctor(identificacion):
    with open (nom_arch,"r",encoding="utf-8") as arch:
        datos=json.load(arch)
        posicion=0
        for usuario in datos["usuarios"]:
            if identificacion== usuario["identificacion"]:
                return posicion
            posicion=posicion+1
        print("el usuario no esta registrado")
        return None


def info_diagnostico(posicion_pac,posicion_doc):
    with open (nom_arch,"r",encoding="utf-8") as arch:
        datos=json.load(arch)
        nombre_pac=datos["pacientes"][posicion_pac]["nombre"]
        identificacion_pac=datos["pacientes"][posicion_pac]["identificacion"]
        nombre_doc=datos["usuarios"][posicion_doc]["nombre"]
        identificacion_doc=datos["usuarios"][posicion_doc]["identificacion"]
        fecha=input("ingrese la fecha en el formato dia-mes-ano-hora militar: ")
        sintomas=input(f"doctor {nombre_doc} ingresa los sintomas que presenta el paciente: ")
        diagnostico=input(f"ingresa el diagnostico de la patologia del paciente {nombre_pac}: ")
        prescripcion=input("ingrese la prescipcion recetada para el paciente: ")
        info_diagnostico={
            "nombre del paciente":nombre_pac,
            "identificacion del paciente": identificacion_pac,
            "nombre del doctor":nombre_doc,
            "identificacion del doctor":identificacion_doc,
            "fecha":fecha,
            "sintomas": sintomas,
            "diagnostico": diagnostico,
            "prescripcion": prescripcion
        }
        return info_diagnostico

def cargar_diagnostico(info_diagnostico):
    with open (nom_arch,"r",encoding="utf-8") as arch:
            datos = json.load(arch)
            diagnostico_ex=False
            for diagnostico in datos["diagnosticos"]:
                if diagnostico ["fecha"]==info_diagnostico["fecha"]:
                    diagnostico_ex=True
                    break
            if diagnostico_ex==False:
                datos["diagnosticos"].append(info_diagnostico)
                with open (nom_arch,"w",encoding="utf-8") as arch:
                    json.dump(datos,arch,indent=4)
            else:
                print("el diagnostico ya existe se procede a cancelar el proceso")
    



