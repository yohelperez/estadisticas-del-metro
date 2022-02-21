# Módulo que contiene las funciones relacionadas con la generación de estadísticas generales del sistema metro


from math import *

#funciones para cargar archivos(general)--------------------------------------------------

def chargeFiles1():
    #funcion que carga el archivo station.info
    diccionario = {}
    i = 0
    archivo = open('stations.info', 'r')
    for linea in archivo:
        diccionario[i] = linea
        i=i+1
    archivo.close()
    return diccionario

def chargeFiles2(): #abre metro.log y lo usa la funcion countpeople , meter en una variable
    #funcion que carga el archivo metro.log
    diccionario2 = {}
    j = 0
    archivo2 = open('metro.log', 'r')
    for linea2 in archivo2:
        diccionario2[j] = linea2
        j=j+1
    archivo2.close()

    return diccionario2

def dictionary():
    d = open("stations.info","r")
    m={}
    for i in d:
        i = i.split(",")
        if 'ESTACION' not in i:
            m[i[1]]=(i[0],float(i[2]),float(i[3]))

    return m



#----------------------------opcion 1 del menu--------------------------------------------

#funcion para la opcion 1
def countPeople(VarChargeFiles2):
    #recibe la variable que contiene la funcion chargeFiles2
    #retorna cantidad de personas que ingresaron al metro

    lista = []
    numeroPersonas = 0
    Vrestar = 0
    for i in VarChargeFiles2:
        numIn = VarChargeFiles2[i][-4:-1]
        if  'IN' in numIn:
            numeroPersonas = numeroPersonas +1
        Lprovicional = [VarChargeFiles2[i][4:12]]
        lista = lista + Lprovicional
    longitudl = len(lista)
    i = 0
    while i < longitudl:
        termino = lista[i]
        count1 = lista.count(termino)
        if count1 == 2:
            i = i+ 1
        elif count1 > 2:
            valor = count1//2
            valor = valor+1 - valor
            Vrestar = Vrestar +valor
            i = i + 1
        i = i+ 1
    totalPersonas = numeroPersonas - Vrestar
    print('la cantidad de personas que usaron el metro fue de: ' + str(totalPersonas))

#funcion para la opcion 2-----------------------------------------------------------

def cantidadViajes():
    #imprime la cantidad de viajes
    sumaViajes = 1
    listarchivo = []

    archivo= open('metro.log', 'r')
    for line in archivo:
        listarchivo+= [line]
    listarchivo.remove(listarchivo[0])
    longitud = len(listarchivo)
    while longitud !=2:

        indice = 1
        if 'IN' in listarchivo[0]:
            IdIn = listarchivo[0][4:12]
            while listarchivo[indice][4:12] !=IdIn :
                indice += 1
            IdOut = listarchivo[indice][4:12]

        else:
            IdOut = listarchivo[0][4:12]
            while listarchivo[indice][4:12] != IdOut :
                indice +=1
            IdIn = listarchivo[indice][4:12]

        sumaViajes += 1
        listarchivo.remove(listarchivo[indice])
        listarchivo.remove(listarchivo[0])
        longitud = len(listarchivo)

    print('la cantidad de viajes fueron: ' + str(sumaViajes))


#funcion para la opcion 3

def Hpico():
    #imprime dos horas pico, que son los dos intervalos de una hora en que más personas entraron
    diccionarioIn = {}
    diccionarioInKeys =[]
    clavesIguales = []
    keys = ''
    keys1 = ''

    archivo = open('metro.log', 'r')
    for line in archivo:
        if  'IN' in line:
            hora = line[-11:-8]
            if hora in diccionarioIn:
                diccionarioIn[hora] += 1
            else:
                diccionarioIn[hora] = 1
    for key in diccionarioIn:
        diccionarioInKeys += [key]
    longitudInKeys = len(diccionarioInKeys)
    n = 0
    while longitudInKeys > 1:
        claveA = diccionarioInKeys[n]
        claveB = diccionarioInKeys[n+1]
        valorA = diccionarioIn[claveA]
        valorB = diccionarioIn[claveB]
        if valorA < valorB:
            diccionarioInKeys.remove(claveA)
            longitudInKeys = len(diccionarioInKeys)
        elif valorA > valorB:
            diccionarioInKeys.remove(claveB)
            longitudInKeys = len(diccionarioInKeys)
        elif valorA == valorB:
            clavesIguales = claveA
            diccionarioInKeys.remove(claveA)
            longitudInKeys = len(diccionarioInKeys)
    while clavesIguales != []:
        print(clavesIguales)
        for clave in clavesIguales:
            claveB = diccionarioInKeys[0]
            valorA = diccionarioInKeys[clave]
            valorB = diccionarioInKeys[claveB]
            if valorA < valorB:
                clavesIguales.remove(clave)
            else:
                diccionarioInKeys += clave
                clavesIguales.remove(clave)
#-----------------------------------------------
    diccionarioIn.pop(diccionarioInKeys[0])
    diccionarioInKeys1 =[]
    for key in diccionarioIn:
        diccionarioInKeys1 += [key]
    longitudInKeys = len(diccionarioInKeys1)
    n = 0
    while longitudInKeys > 1:
        claveA = diccionarioInKeys1[n]
        claveB = diccionarioInKeys1[n+1]
        valorA = diccionarioIn[claveA]
        valorB = diccionarioIn[claveB]
        if valorA < valorB:
            diccionarioInKeys1.remove(claveA)
            longitudInKeys = len(diccionarioInKeys1)
        elif valorA > valorB:
            diccionarioInKeys1.remove(claveB)
            longitudInKeys = len(diccionarioInKeys1)
        elif valorA == valorB:
            clavesIguales = claveA
            diccionarioInKeys1.remove(claveA)
            longitudInKeys = len(diccionarioInKeys1)
    while clavesIguales != []:
        for clave in clavesIguales:
            claveB = diccionarioInKeys1[0]
            valorA = diccionarioInKeys1[clave]
            valorB = diccionarioInKeys1[claveB]
            if valorA < valorB:
                clavesIguales.remove(clave)
            else:
                diccionarioInKeys1 += clave
                clavesIguales.remove(clave)

    for key in diccionarioInKeys:
        keys += key
    for key in diccionarioInKeys1:
        keys1 += key
    print('la(s) hora(s) pico fue(ron) a la(s)' + keys + ' y la(s)' + keys1 )

#funcion para la opcion 4

def ingresosTotal():
    #imprime cantidad de ingresos totales
    ingresos = 0
    archivo = open('metro.log' , 'r')
    for line in archivo:
        if 'IN' in line:
            ingresos+= 1
    print('los ingresos totales por concepto de tiquetes fueron: ' + str(ingresos))




#funcion para la opcion 5

def estacionesMax():
    #funcion para la opcion 5 de la opcion 1
    #imprime estaciones en las que mas personas entran y salen

    archivo = chargeFiles2()
    i = 0
    diccionarioIn ={}
    diccionarioOut = {}
    ultima = len(archivo)

    while i < ultima:
        InOut = archivo[i][-4:-1]
        if 'IN' in InOut:
            codigo = archivo[i][:3]
            if codigo in diccionarioIn:
                diccionarioIn[codigo] += 1
                i+= 1

            else:
                diccionarioIn[codigo]=1
                i+=1
        codigo= archivo[i][:3]
        if codigo in diccionarioOut:
            diccionarioOut[codigo]+=1
            i+=1
        else:
            diccionarioOut[codigo] = 1
            i+=1

    def MayorEstacionIn():
        #retorna la estacion en la que mas personas entran
        diccionarioInKeys = []
        clavesIguales= []
        n =0
        for key in diccionarioIn:
            diccionarioInKeys +=[key]
        longitudIn = len(diccionarioInKeys)

        while longitudIn > 1:
            claveA =diccionarioInKeys[n]
            claveB = diccionarioInKeys[n+1]
            valorA = diccionarioIn[claveA]
            valorB = diccionarioIn[claveB]

            if valorA < valorB:
                diccionarioInKeys.remove(claveA)
                longitudIn = len(diccionarioInKeys)
            elif valorA > valorB:
                diccionarioInKeys.remove(claveB)
                longitudIn = len(diccionarioInKeys)
            elif valorA == valorB:
                clavesIguales += [claveA]
                diccionarioInKeys.remove(claveA)
                longitudIn = len(diccionarioInKeys)
        if clavesIguales ==[]:
            return diccionarioInKeys
        for clave in clavesIguales:
            claveB = diccionarioInKeys[0]
            valorA = diccionarioIn[clave]
            valorB = diccionarioIn[claveB]
            if valorA == valorB:
                diccionarioInKeys += [clave]
        return diccionarioInKeys

    def MayorEstacionOut():
        #retorna la estacion en que mas personas salen
        diccionarioOutKeys =[]
        clavesIguales= []
        n =0
        for key in diccionarioOut:
            diccionarioOutKeys +=[key]
        longitudOut = len(diccionarioOutKeys)

        while longitudOut > 1:
            claveA = diccionarioOutKeys[n]
            claveB = diccionarioOutKeys[n+1]
            valorA = diccionarioOut[claveA]
            valorB = diccionarioOut[claveB]

            if valorA < valorB:
                diccionarioOutKeys.remove(claveA)
                longitudOut = len(diccionarioOutKeys)
            elif valorA > valorB:
                diccionarioOutKeys.remove(claveB)
                longitudOut = len(diccionarioOutKeys)
            elif valorA == valorB:
                clavesIguales += [claveA]
                diccionarioOutKeys.remove(claveA)
                longitudOut = len(diccionarioOutKeys)
        if clavesIguales ==[]:
            return diccionarioOutKeys
        for clave in clavesIguales:
            claveB = diccionarioOutKeys[0]
            valorA = diccionarioOut[clave]
            valorB = diccionarioOut[claveB]

            if valorA == valorB:
                diccionarioOutKeys += [clave]
        return diccionarioOutKeys

    traductor = dictionary()
    mayorIn = MayorEstacionIn()
    mayorOut = MayorEstacionOut()
    In = ''
    Out = ''

    indice = str('1')
    for clave in mayorIn:
        indice = ' ' + str(indice) + ' '
        In += indice + traductor[clave][0]
        indice = int(indice) + 1

    indice = str('1')
    for clave in mayorOut:
        indice = ' ' +str(indice) + ' '
        if clave in traductor:
            Out += indice +traductor[clave][0]
            indice = int(indice) + 1

    print('la(s) estacion(es) en la(s) que más ingresan personas es/son ' + In)
    print('la(s) estacion(es) en la(s) que más ingresan personas es/son ' + Out)

#funcion para la opcion 6

def stdistance(origen,destino,M):
    '''
       Recibe dos string con los identificadores de las estaciones origen y destino
       Recibe un diccionario cuya clave es el identificador de la estación y el valor es una tupla con el nombre de la estación
       y las coordenadas geograficas.
       Retorna un float con la distancia en metros del recorrido entre las dos estaciones
    '''


    def geodistance(P1,P2,h):
        pi = 3.141592
        R = 6371009
        theta1 = pi/2 - (P1[0]*pi/180)
        phi1=P1[1]*pi/180
        rho1=R+h

        theta2=pi/2 - (P2[0]*pi/180)
        phi2=P2[1]*pi/180
        rho2=R+h

        x1=rho1*sin(theta1)*cos(phi1)
        x2=rho2*sin(theta2)*cos(phi2)
        y1=rho1*sin(theta1)*sin(phi1)
        y2=rho2*sin(theta2)*sin(phi2)
        z1=rho1*cos(theta1)
        z2=rho2*cos(theta2)

        D=((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**(1/2);
        return D

    if ((origen>'021')or(origen<'001')or(destino>'021')or(destino<'001')):
        D=-1
        return
    D=0
    if(origen>destino):
        step=-1
        dest=int(destino)+1
    elif(origen<destino):
        step=1
        dest=int(destino)-1
    else:
        return
    destino = '0'*(3-len(str(dest)))+str(dest)

    for i in range(int(origen),int(destino),step):
        indx1='0'*(3-len(str(i)))+str(i)
        indx2='0'*(3-len(str(i+step)))+str(i+step)
        D = D + geodistance(M[indx1][1:],M[indx2][1:],1600)

    return D;

def dtPromedio():
    #imprime el tiempo y distancia promedio de viaje
    listarchivo=[]
    ltiempo=[]
    ldistancia = []
    sumaTiempo = 0
    sumaDistancia = 0


    archivo= open('metro.log', 'r')
    for line in archivo:
        listarchivo+= [line]
    listarchivo.remove(listarchivo[0])
    longitud = len(listarchivo)
    while longitud >=2:

        indice = 1
        if 'IN' in listarchivo[0]:
            IdIn = listarchivo[0][4:12]
            origen = listarchivo[0][:3]
            horaIn = listarchivo[0][-10:-5]
            while listarchivo[indice][4:12] !=IdIn :
                indice += 1
            IdOut = listarchivo[indice][4:12]
            destino = listarchivo[indice][:3]
            horaOut = listarchivo[indice][-10:-5]

        else:
            IdOut = listarchivo[0][4:12]
            destino = listarchivo[0][:3]
            horaOut = listarchivo[0][-10:-5]
            while listarchivo[indice][4:12] != IdOut :
                indice +=1
            IdIn = listarchivo[indice][4:12]
            origen =listarchivo[indice][:3]
            horaIn = listarchivo[indice][-10:-5]
        hIn =int(horaIn[:2])*60

        mIn = int(horaIn[-2:])+ hIn
        hOut = int(horaOut[:2])*60
        mOut = int(horaOut[-2:]) +hOut
        tiempoT = mOut - mIn
        ltiempo += [tiempoT]

        diccionario = dictionary()
        distancia = stdistance(origen,destino,diccionario)
        ldistancia +=[distancia]


        listarchivo.remove(listarchivo[indice])
        listarchivo.remove(listarchivo[0])
        longitud = len(listarchivo)




    for time in ltiempo:
        sumaTiempo += time
    longitudltiempo = len(ltiempo)
    Tpromedio = sumaTiempo // longitudltiempo

    for distancia in ldistancia:
        sumaDistancia += distancia
    longitudldistancia = len(ldistancia)
    Dpromedio = sumaDistancia / longitudldistancia
    print('la distancia promedio de viaje fue de: ' + str(Dpromedio)+ ' metros, y el tiempo promedio fue de: ' +str(Tpromedio) + ' minutos')

#----------------------opcion 2 del menu-------------------------------------------------

#opcion 1

def dictionary2():
    #retorna un diccionario con los nombres de las estaciones en minuscula como la clave y sus respectivas identificaciones como dato
    d = open("stations.info","r")
    m={}
    for i in d:
        i = i.split(",")
        if 'ESTACION' not in i:
            est = i[0]
            if 'Niquía' in est:
                m['niquia']= i[1]
            else:
                est = est.lower()
                m[est]=(i[1])
    return m


def cantidadViajesEst(estación):
    #imprime cantidad de viajes en esa estacion
    sumaViajes = 1
    listarchivo = []
    dic = dictionary2()

    if len(str(estación)) > 3:
        estación = estación.lower()
        estación = dic[estación]

    archivo= open('metro.log', 'r')
    for line in archivo:
        if str(estación) in line and 'IN' in line:
            sumaViajes += 1

    print('la cantidad total de viajes fue: ' + str(sumaViajes))

#opcion 2

def Hpico2(estación):
    diccionarioIn = {}
    diccionarioInKeys =[]
    clavesIguales = []
    keys = ''
    keys1 = ''

    archivo = open('metro.log', 'r')
    for line in archivo:
        if  'IN' in line and estación in line:
            hora = line[-11:-8]
            if hora in diccionarioIn:
                diccionarioIn[hora] += 1
            else:
                diccionarioIn[hora] = 1
    for key in diccionarioIn:
        diccionarioInKeys += [key]
    longitudInKeys = len(diccionarioInKeys)
    n = 0
    while longitudInKeys > 1:
        claveA = diccionarioInKeys[n]
        claveB = diccionarioInKeys[n+1]
        valorA = diccionarioIn[claveA]
        valorB = diccionarioIn[claveB]
        if valorA < valorB:
            diccionarioInKeys.remove(claveA)
            longitudInKeys = len(diccionarioInKeys)
        elif valorA > valorB:
            diccionarioInKeys.remove(claveB)
            longitudInKeys = len(diccionarioInKeys)
        elif valorA == valorB:
            clavesIguales = claveA
            diccionarioInKeys.remove(claveA)
            longitudInKeys = len(diccionarioInKeys)
    while clavesIguales != []:
        for clave in clavesIguales:
            claveB = diccionarioInKeys[0]
            valorA = diccionarioInKeys[clave]
            valorB = diccionarioInKeys[claveB]
            if valorA < valorB:
                clavesIguales.remove(clave)
            else:
                diccionarioInKeys += clave
                clavesIguales.remove(clave)
#-----------------------------------------------
    diccionarioIn.pop(diccionarioInKeys[0])
    diccionarioInKeys1 =[]
    for key in diccionarioIn:
        diccionarioInKeys1 += [key]
    longitudInKeys = len(diccionarioInKeys1)
    n = 0
    while longitudInKeys > 1:
        claveA = diccionarioInKeys1[n]
        claveB = diccionarioInKeys1[n+1]
        valorA = diccionarioIn[claveA]
        valorB = diccionarioIn[claveB]
        if valorA < valorB:
            diccionarioInKeys1.remove(claveA)
            longitudInKeys = len(diccionarioInKeys1)
        elif valorA > valorB:
            diccionarioInKeys1.remove(claveB)
            longitudInKeys = len(diccionarioInKeys1)
        elif valorA == valorB:
            clavesIguales = claveA
            diccionarioInKeys1.remove(claveA)
            longitudInKeys = len(diccionarioInKeys1)
    while clavesIguales != []:
        for clave in clavesIguales:
            claveB = diccionarioInKeys1[0]
            valorA = diccionarioInKeys1[clave]
            valorB = diccionarioInKeys1[claveB]
            if valorA < valorB:
                clavesIguales.remove(clave)
            else:
                diccionarioInKeys1 += clave
                clavesIguales.remove(clave)

    for key in diccionarioInKeys:
        keys += key
    for key in diccionarioInKeys1:
        keys1 += key
    print('la(s) hora(s) pico fue(ron) a la(s)' + keys + ' y la(s)' + keys1 )

#opcion 3
def estacionesMax2():
    #imprime estaciones en las que mas personas entran y salen

    archivo = chargeFiles2()
    i = 0
    diccionarioIn ={}
    diccionarioOut = {}
    ultima = len(archivo)

    while i < ultima:
        InOut = archivo[i][-4:-1]
        if 'IN' in InOut:
            codigo = archivo[i][:3]
            if codigo in diccionarioIn:
                diccionarioIn[codigo] += 1
                i+= 1

            else:
                diccionarioIn[codigo]=1
                i+=1
        codigo= archivo[i][:3]
        if codigo in diccionarioOut:
            diccionarioOut[codigo]+=1
            i+=1
        else:
            diccionarioOut[codigo] = 1
            i+=1

    def MayorEstacionIn():
        diccionarioInKeys = []
        clavesIguales= []
        n =0
        for key in diccionarioIn:
            diccionarioInKeys +=[key]
        longitudIn = len(diccionarioInKeys)

        while longitudIn > 1:
            claveA =diccionarioInKeys[n]
            claveB = diccionarioInKeys[n+1]
            valorA = diccionarioIn[claveA]
            valorB = diccionarioIn[claveB]

            if valorA < valorB:
                diccionarioInKeys.remove(claveA)
                longitudIn = len(diccionarioInKeys)
            elif valorA > valorB:
                diccionarioInKeys.remove(claveB)
                longitudIn = len(diccionarioInKeys)
            elif valorA == valorB:
                clavesIguales += [claveA]
                diccionarioInKeys.remove(claveA)
                longitudIn = len(diccionarioInKeys)
        if clavesIguales ==[]:
            return diccionarioInKeys
        for clave in clavesIguales:
            claveB = diccionarioInKeys[0]
            valorA = diccionarioIn[clave]
            valorB = diccionarioIn[claveB]
            if valorA == valorB:
                diccionarioInKeys += [clave]
        return diccionarioInKeys

    def MayorEstacionOut():
        diccionarioOutKeys =[]
        clavesIguales= []
        n =0
        for key in diccionarioOut:
            diccionarioOutKeys +=[key]
        longitudOut = len(diccionarioOutKeys)

        while longitudOut > 1:
            claveA = diccionarioOutKeys[n]
            claveB = diccionarioOutKeys[n+1]
            valorA = diccionarioOut[claveA]
            valorB = diccionarioOut[claveB]

            if valorA < valorB:
                diccionarioOutKeys.remove(claveA)
                longitudOut = len(diccionarioOutKeys)
            elif valorA > valorB:
                diccionarioOutKeys.remove(claveB)
                longitudOut = len(diccionarioOutKeys)
            elif valorA == valorB:
                clavesIguales += [claveA]
                diccionarioOutKeys.remove(claveA)
                longitudOut = len(diccionarioOutKeys)
        if clavesIguales ==[]:
            return diccionarioOutKeys
        for clave in clavesIguales:
            claveB = diccionarioOutKeys[0]
            valorA = diccionarioOut[clave]
            valorB = diccionarioOut[claveB]

            if valorA == valorB:
                diccionarioOutKeys += [clave]
        return diccionarioOutKeys

    traductor = dictionary()
    mayorIn = MayorEstacionIn()
    mayorOut = MayorEstacionOut()
    In = ''
    Out = ''

    indice = str('1')
    for clave in mayorIn:
        indice = ' ' + str(indice) + ' '
        In += indice + traductor[clave][0]
        indice = int(indice) + 1

    indice = str('1')
    for clave in mayorOut:
        indice = ' ' +str(indice) + ' '
        if clave in traductor:
            Out += indice +traductor[clave][0]
            indice = int(indice) + 1

    print('la(s) estacion(es) de origen más comun(es) es/son ' + In)
    print('la(s) estacion(es) de destino más comun(es) es/son ' + Out)
