# 201901069-LFP-Practica
Entrega de Practica 1

SimpleQL es un lenguaje de consultas que funciona únicamente a nivel de consola, su
propósito es facilitar al usuario la búsqueda de registros completos en archivos json, en los
que buscar registro por registro podría ser muy tedioso y cansado.

El usuario podra ingresar el comando que dese utilizar en tiempo real, los comandos a utilizar
son los siguientes.

Cargar: Este comando permitira al usuario cargar los archivos a memoria del programa con los cuales podra trabajar
durante la ejecucion del programa, teniendo en cuenta que todos los archivos deben tener la misma estructura.
su sintaxis es la siguiente: CARGAR archivo1, archivo2, archivo3, …… archivoN

Seleccionar: Este comando permite mostrar uno o mas registros o atributos con base a condiciones simples que se
pueden aplicar a los atributos.
Su sintaxis es la siguiente: SELECCIONAR nombre, edad, promedio, activo DONDE nombre = “Francisco”
Tambien se puede utilizar el comando SELECCIONAR* que muestra todos los registros con sus atributos correspondientes.


Maximo: Este comando mostrara el maximo valor existente entre los registros cargados a memoria dependiendo el 
atributo que se le haya especificado.
Su sintaxis es la siguiente: MAXIMO edad

Minimo: Al igual que el comando maximo este devuelve el valor mas pequeño existente entre los registros cargados 
a memoria dependiendo el atributo que se le haya especificado.
Su sintaxis es la siguiente: MINIMO edad

Suma: Este comando mostrara en pantalla la sumatoria de todos los datos cargados a memoria dependiendo el atributo que
se le haya especificado.
Su sintaxis es la siguiente: SUMA edad

Cuenta: Este comando muestra en pantalla al usuario la cantidad de registros que se hayan cargado a memoria. Es de mucha utilidad
cuando se han cargado diversos documento json a memoria y no se sabe cuantos registros contenia cada archivo.
Su sintaxis es la siguiente: CUENTA

Reportar: Este comando permite crear un reporte en html que contendra la cantidad de registros que el usuario haya especificado.
Su sintaxis es la siguiente: REPORTAR 10

Como una ventaja de SimpleQL es que la aplicacion es case insensitive lo cual permite al usuario ingresar los comandos que desee
ejecutar con letra mayuscula o minuscula a disposicion del mismo.

