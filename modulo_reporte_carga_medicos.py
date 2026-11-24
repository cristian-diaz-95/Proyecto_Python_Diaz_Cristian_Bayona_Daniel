import json
ruta="D:\\Users\\CRISTIAN DBAY\\Desktop\\curso de python\\python\\proyecto #1\\"
nom_arch=ruta+"base_datos.json"

def reporte_carga_medico_nombre(ID_medico):
    a=0
    with open (nom_arch,"r",encoding="utf-8") as arch:
            datos = json.load(arch)
            for medico in datos["usuarios"]:
                if ID_medico == medico ["identificacion"]:
                    a=medico["nombre"]
                    return  a
            print("ID ingresada no corresponde a un medico")    
            return None
def reporte_cerga_medico_diagnostico(ID_medico):
    counter=0
    with open (nom_arch,"r",encoding="utf-8") as arch:
                datos = json.load(arch)
                for diagnostico in datos["diagnosticos"]:
                    if ID_medico == diagnostico["identificacion del doctor"]:
                            counter+=1
                            return counter
def reporte_carga_medico_paciente (ID_medico):
    pacientes_dist={}
    with open (nom_arch,"r",encoding="utf-8") as arch:
                    datos = json.load(arch)
                    for diagnostico in datos["diagnosticos"]:
                        if ID_medico == diagnostico["identificacion del doctor"]:
                            pacientes_dist.update(diagnostico["identificacion del paciente"])
                    pacientes_dist.fromkeys()
                    return len(pacientes_dist)
