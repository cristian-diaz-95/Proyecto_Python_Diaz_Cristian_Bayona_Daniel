import json
ruta="D:\\Users\\CRISTIAN DBAY\\Desktop\\curso de python\\python\\proyecto #1\\"
nom_arch=ruta+"base_datos.json"

def busqueda_paciente(identificacion):
    with open (nom_arch,"r",encoding="utf-8") as arch:
            datos=json.load(arch)
            for paciente in datos["pacientes"]:
                if identificacion==paciente["identificacion"]:
                    print("la informacion del paciente: ")
                    print("nombre: ",paciente["nombre"])
                    print("apellidos: ",paciente["apellidos"])
                    print("identificacion: ",paciente["identificacion"])
                    print("email: ",paciente["email"])
                    print("direccion: ",paciente["direccion"])
                    print("telefono: ",paciente["telefono"])
                    print("genero: ",paciente["genero"])
                    print("estado civil: ",paciente["estado civil"],"\n")

def busqueda_diagnostico(identificacion):
    with open (nom_arch,"r",encoding="utf-8") as arch:
            datos=json.load(arch)
            print("Historia clinica del paciente: ")
            for diagnostico in datos["diagnosticos"]:
                if identificacion==diagnostico["identificacion del paciente"]:
                    print("fecha: ",diagnostico["fecha"])
                    print("nombre del doctor: ",diagnostico["nombre del doctor"])
                    print("identificacion del doctor: ",diagnostico["identificacion del doctor"])
                    print("sintomas: ",diagnostico["sintomas"])
                    print("diagnostico: ",diagnostico["diagnostico"])
                    print("prescripcion: ",diagnostico["prescripcion"],"\n")

        
