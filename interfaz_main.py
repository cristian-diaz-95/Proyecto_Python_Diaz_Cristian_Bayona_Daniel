import modulo_login
import modulo_pacientes
import modulo_historia_clinica
import modulo_registro
import menus
import json
ruta="D:\\Users\\CRISTIAN DBAY\\Desktop\\curso de python\\python\\proyecto #1\\"
nom_arch=ruta+"base_datos.json"

base_usuario=modulo_registro.crear_base_usuario()
base_pacientes=modulo_pacientes.crear_base_paciente()
base_diagnosticos=modulo_pacientes.crear_base_diagnostico()

while True:
    print("______BIENVENIDO____")
    email=input("Ingrese su usuario para continuar: ")
    validar_e=modulo_login.validacion_usuario(email)
    if validar_e != None:
        break
while True:
    contra=input("Ingrese la contrasena para continuar: ")
    validar_contra=modulo_login.validacion_contrasena(validar_e,contra)
    if validar_contra != False:
        break
with open (nom_arch,"r",encoding="utf-8") as arch:
        datos=json.load(arch)
        rol=datos["usuarios"][validar_e]["rol"]
if rol == "admin":
    while True:
        menus.menu_admin()       
        opcion=int(input("que opcion desea ejecutar: "))
        if opcion<1 or opcion > 3:
            print("ERROR\n Opcion ingresada invalida\n Vuelve a intentarlo")
            continue    
        match opcion:
            case 1:
                usuario=modulo_registro.ingresar_usuario()
                modulo_registro.cargar_usuario_credenciales(usuario)
            case 2:
                buscar=input("ingrese el numero de identificacion del paciente a buscar:  ")
                modulo_historia_clinica.busqueda_paciente(buscar)
                modulo_historia_clinica.busqueda_diagnostico(buscar)
            case 3:
                print("vuelva pronto")
                break   
else:
    while True:
        menus.menu_doc()
        opcion=int(input("que opcion desea ejecutar: "))
        if opcion<1 or opcion > 4:
            print("ERROR\n Opcion ingresada invalida\n Vuelve a intentarlo")
            continue    
        match opcion:
                case 1:
                    paciente=modulo_pacientes.ingresar_paciente()                   
                    modulo_pacientes.cargar_paciente(paciente)
                case 2:
                    paci_diag=input("ingrese el numero de identificacion del paciente a diagnosticar: ")
                    doc_diag=input("ingrese el numero de identificacion del doctor: ")
                    veri_paci=modulo_pacientes.verificacion_paciente(paci_diag)
                    extrac_doc=modulo_pacientes.extraccion_doctor(doc_diag)
                    diagnostico=modulo_pacientes.info_diagnostico(veri_paci,extrac_doc)
                    modulo_pacientes.cargar_diagnostico(diagnostico)
                case 3:
                    buscar=input("ingrese el numero de identificacion del paciente a buscar:  ")
                    modulo_historia_clinica.busqueda_paciente(buscar)
                    modulo_historia_clinica.busqueda_diagnostico(buscar)
                case 4:
                    print("vuelva pronto")
                    break
                
                    