import json
import webbrowser
Vector_Nombre=[]
Vector_Edad=[]
Vector_Activo=[]
Vector_Promedio=[]



def cargar_datos(ruta):
    try:
        with open(ruta) as contenido:
            documentos =json.load(contenido)
            for i in documentos:
                Vector_Nombre.append(i['nombre'])
                Vector_Edad.append(i['edad'])
                Vector_Activo.append(i['activo'])
                Vector_Promedio.append(i['promedio'])
    except Exception as ex:
        print(ex)
        print("**Error El archivo no se cargo**")
        inicio()


def reporte(texto):
    f = open("Reporte.html", "w")
    m = f"""
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Reporte</title>
        <link rel="stylesheet" href="style.css">


    </head>
    <body>
        <h1>Reporte de Registros</h1>
    <br>
    <br>
    <div id="main-container">
       <table>
            <thead>
                <tr>
                <th>No.</th><th>NOMBRE</th><th>EDAD</th><th>ACTIVO</th><th>PROMEDIO</th>
                </tr>
            </thead>
            <tbody>
                <tr>{texto}</tr>
            </tbody>
        </table>
    </div>
<br>
    <br><br>
    
    </body>
    </html>
    """

    f.write(m)
    f.close()
    webbrowser.open_new_tab("Reporte.html")






try:
    #----------------------------------------------para cargar los archivos
    def inicio():
        Entrada = input("Cargue los archivos con los que desea trabajar:\n ").lower()
        vector = Entrada.split(" ", 1)
        if vector[0] == "cargar":
            print("Usted uso el comando de ", vector[0]," Se cargaron los siguientes archivos")
            vector2 = vector[1].split(", ")
            for i in range(0, vector2.__len__()):
                cargar_datos(vector2[i])
                print("se abrio", vector2[i])
        else:
            print("*Error* el comando --",vector[0].upper(),"-- no se reconoce")
            inicio()

    #---------------------------------------para ejecutar comandos
    def desarrollo():
        Entrada = input("Ingrese el comando que desea ejecutar:\n ").lower()
        vector = Entrada.split(" ", 1)
    #---------------------------------------------------abrir
        if vector[0] == "cargar":
            print("Usted uso el comando de ", vector[0], " Se cargaron los siguientes archivos")
            vector2 = vector[1].split(", ")
            for i in range(0, vector2.__len__()):
                cargar_datos(vector2[i])
                print("se abrio", vector2[i])
            desarrollo()
    #---------------------------------------------------seleccionar
        if vector[0] == "seleccionar":
            print("uso el comando SELECCIONAR")
            vector2 = vector[1].split(" donde ",2)
            vectorCampos=vector2[0].split(", ")# aqui tengo los campos a usar nombre, edad, activo, promedio
            nombre=False
            edad=False
            activo=False
            promedio=False
            for i in range(0,len(vectorCampos)):
                if vectorCampos[i]=="nombre": nombre=True
                elif vectorCampos[i]=="edad": edad=True
                elif vectorCampos[i] == "activo": activo = True
                elif vectorCampos[i] == "promedio": promedio = True
                else:
                    print("El Campo-->",vectorCampos[i],"<--No es valido")
                    desarrollo()
            vectorCondicion=vector2[1].split(("="))# aqui tengo la condicion promedio=100

            if vectorCondicion[0]=="nombre":
                if vectorCondicion[1].count('"')==2:
                    for i in range(0,len(Vector_Nombre)):
                        if str(Vector_Nombre[i]).lower()==vectorCondicion[1].replace('"','').lower():
                            if nombre: print("Nombre: ",Vector_Nombre[i])
                            if activo: print("Activo: ", Vector_Activo[i])
                            if promedio: print("Promedio: ", Vector_Promedio[i])
                            if edad: print("Edad: ", Vector_Edad[i])
                            print("--------------------------------------------------------------")
                    desarrollo()
                else: print("Ingreso mal el comando de Seleccionar")
                desarrollo()

            elif vectorCondicion[0] == "edad":
                for i in range(0,len(Vector_Edad)):
                    if int(Vector_Edad[i])==int(vectorCondicion[1]):
                        if nombre: print("Nombre: ",Vector_Nombre[i])
                        if activo: print("Activo: ", Vector_Activo[i])
                        if promedio: print("Promedio: ", Vector_Promedio[i])
                        if edad: print("Edad: ", Vector_Edad[i])
                        print("--------------------------------------------------------------")
                desarrollo()
            elif vectorCondicion[0] == "activo":
                for i in range(0, len(Vector_Activo)):
                    if str(Vector_Activo[i]).lower() == vectorCondicion[1].lower():
                        if nombre: print("Nombre: ", Vector_Nombre[i])
                        if activo: print("Activo: ", Vector_Activo[i])
                        if promedio: print("Promedio: ", Vector_Promedio[i])
                        if edad: print("Edad: ", Vector_Edad[i])
                        print("--------------------------------------------------------------")
                desarrollo()

            elif vectorCondicion[0] == "promedio":
                print("buscar en promedio")
                for i in range(0,len(Vector_Promedio)):
                    if float(Vector_Promedio[i])==float(vectorCondicion[1]):
                        if nombre: print("Nombre: ",Vector_Nombre[i])
                        if activo: print("Activo: ", Vector_Activo[i])
                        if promedio: print("Promedio: ", Vector_Promedio[i])
                        if edad: print("Edad: ", Vector_Edad[i])
                        print("--------------------------------------------------------------")
                desarrollo()

        elif vector[0]=="seleccionar*":
            print("uso seleccionar todo")
            for i in range(0, len(Vector_Nombre)):
                print("No. ", i+1,"|Nombre: ", Vector_Nombre[i], "|Edad", Vector_Edad[i],"|Activo", Vector_Activo[i], "|Promedio", Vector_Promedio[i] )
            desarrollo()
    #-----------------------------------------------------Maximo
        elif vector[0]=="maximo":
            print("uso el comando Maximo")
            if vector[1]=="edad":
                Maximo = 0
                for i in range(0,len(Vector_Edad)):
                    if Vector_Edad[i]>Maximo:
                        Maximo=Vector_Edad[i]
                print("El valor maximo de edad es: ",Maximo)
                desarrollo()
            elif vector[1]=="promedio":
                Maximo = 0
                for i in range(0, len(Vector_Promedio)):
                    if Vector_Promedio[i] > Maximo:
                        Maximo = Vector_Promedio[i]
                print("El valor maximo de Promedio es: ", Maximo)
                desarrollo()
            else:
                print("No selecciono ningun atributo")
            desarrollo()

    #------------------------------------------------------Minimo
        elif vector[0]=="minimo":
            print("uso el comando Minimo")
            if vector[1] == "edad":
                Minimo = 100
                for i in range(0, len(Vector_Edad)):
                    if Vector_Edad[i] < Minimo:
                        Minimo = Vector_Edad[i]
                print("El valor maximo de edad es: ", Minimo)
                desarrollo()
            elif vector[1]=="promedio":
                Minimo = 100
                for i in range(0, len(Vector_Promedio)):
                    if Vector_Promedio[i] < Minimo:
                        Minimo = Vector_Promedio[i]
                print("El valor minimo de Promedio es: ", Minimo)
                desarrollo()
            else:
                print("No selecciono ningun atributo")
    # ------------------------------------------------------suma
        elif vector[0] == "suma":
            print("uso el comando Suma")
            if vector[1] == "edad":
                suma = 0
                for i in range(0, len(Vector_Edad)):
                        suma=suma+Vector_Edad[i]
                print("La suma de las edades es: ", suma)
                desarrollo()
            elif vector[1] == "promedio":
                suma = 0
                for i in range(0, len(Vector_Promedio)):
                        suma=suma+Vector_Promedio[i]
                print("La suma de las edades es: ", suma)
                desarrollo()
            else:
                print("No selecciono ningun atributo")
        elif vector[0] == "cuenta":
            contador=0
            for i in range(0, len(Vector_Nombre)):
                contador=contador+1
            print("La cantidad de registros en memoria es: ", contador)
            desarrollo()
        elif vector[0] == "reportar":
            print("uso el comando Reportar")
            texto=""
            if int(vector[1].isnumeric()):
                cantidad=int(vector[1])
                if cantidad<=len(Vector_Nombre):
                    for i in range(0,cantidad):
                        texto=texto+f"<tr><td>{i+1}</td><td>{Vector_Nombre[i]}</td><td>{Vector_Edad[i]}</td><td>{Vector_Activo[i]}</td><td>{Vector_Promedio[i]}</td></tr>"
                    reporte(texto)
                else:print("no existe esa cantidad de archivos en memoria solo existen ",len(Vector_Nombre)," archivos")
                desarrollo()
            else: print("No ingreso un comando valido")
            desarrollo()
        else:
            print("No ingreso un comando valido ")
            desarrollo()
except Exception as ex:
    print(ex)
    print("Ocurrio un error al escribir el comando")
    desarrollo()

print("*****************Bienvenido A SimpleQL*****************")
inicio()
desarrollo()

#lower minusculas upper mayusculas










