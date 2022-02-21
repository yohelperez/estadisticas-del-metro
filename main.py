# Implemente aquí los menús y el programa principal que invoca las funciones de los otros módulos
import system


cargarArchivo1= system.chargeFiles1()
cargarArchivo2 = system.chargeFiles2()
Diccionario = system.dictionary()
print("SISTEMA DE CONSULTA DE ESTADISTICAS METRO\n")

print(" Digite 1 para estadisticas generales del sistema\n","Digite 2 para estadisticas por estacion\n","Digite x para salir\n")


dato = input("elija su opcion")
if dato == 'x':
    print('closing...')

elif int(dato) == 1:
    dato1= input('1. Cantidad de personas que usaron el metro\n 2. Cantidad de viajes que hubo\n 3. Hora pico de ingreso de usuarios\n 4. Ingresos totales por concepto de tiquedes\n 5. Estaciones en las que más personas ingresan y salen\n 6. Distancia y tiempo promedio de viaje de los usuarios\n Ingrese el número con la opción deseada(o x para salir)\n')
    if 'x' in dato1:
        print('closing...')
    elif int(dato1) ==1:
        system.countPeople(cargarArchivo2)
    elif int(dato1) ==2:
        system.cantidadViajes()
    elif int(dato1) == 3:
        system.Hpico()
    elif int(dato1) == 4:
        system.ingresosTotal()
    elif int(dato1) ==5:
        system.estacionesMax()
    elif int(dato1) == 6:
        system.dtPromedio()

elif int(dato) == 2:
    estación = input('ingrese el nombre o el código de la estación de interés\n')
    dato2 =input('1. Cantidad total de viajes\n 2. Horas pico de ingreso y salida de usuarios\n 3. Estaciones de origen y destino más comunes\n Ingrese el número con la opción deseada(o x para salir): \n')
    if 'x' in dato2:
        print('closing...')
    elif int(dato2) ==1:
        system.cantidadViajesEst(dato2)
    elif int(dato2) == 2:
        system.Hpico2(estación)
    elif int(dato2) ==3:
        system.estacionesMax2()