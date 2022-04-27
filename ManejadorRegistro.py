import csv
from Registro import Registro

class ManejadorRegistro:
    __listaRegistros=[]
    def __init__(self):
        self.__listaRegistros=[]
    def cargarDias(self,dias):
        for i in range(dias):
            self.__listaRegistros.append([])
    def cargarHoras(self,dia):
        for i in range(24):
            self.__listaRegistros[dia].append(None)
    def agregarRegistro(self,registro,dia,hora):
        if type(registro)==Registro:
            if len(self.__listaRegistros[dia])==0:
                self.cargarHoras(dia)
            self.__listaRegistros[dia][hora]=registro
        else:
            print('Error, no se pudo agregar un registro a la lista, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        nombreArchivo='registroMes.csv'
        archivo=open(nombreArchivo)
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                self.agregarRegistro(Registro(int(fila[2]),int(fila[3]),int(fila[4])),int(fila[0])-1,int(fila[1]))
        archivo.close()
        print('Fin de la carga desde: ',nombreArchivo)
    def mostrarValoresMayoresYMenores(self):
        temperaturaMayor=0
        temperaturaMenor=0
        humedadMayor=0
        humedadMenor=0
        presionMayor=0
        presionMenor=0
        temperaturaHoraMayor=0
        temperaturaDiaMayor=0
        temperaturaHoraMenor=0
        temperaturaDiaMenor=0
        humedadHoraMayor=0
        humedadDiaMayor=0
        humedadHoraMenor=0
        humedadDiaMenor=0
        presionHoraMayor=0
        presionDiaMayor=0
        presionHoraMenor=0
        presionDiaMenor=0
        banderaPrRegistro=True
        for i in range(len(self.__listaRegistros)):
            if len(self.__listaRegistros[i])!=0:
                for j in range(24):
                    if(self.__listaRegistros[i][j])!=None:
                        if banderaPrRegistro:
                            temperaturaMayor=self.__listaRegistros[i][j].getTemperatura()
                            temperaturaMenor=self.__listaRegistros[i][j].getTemperatura()
                            humedadMayor=self.__listaRegistros[i][j].getHumedad()
                            humedadMenor=self.__listaRegistros[i][j].getHumedad()
                            presionMayor=self.__listaRegistros[i][j].getPresion()
                            presionMenor=self.__listaRegistros[i][j].getPresion()
                            banderaPrRegistro=not banderaPrRegistro
                            temperaturaHoraMayor=j
                            temperaturaDiaMayor=i+1
                            temperaturaHoraMenor=j
                            temperaturaDiaMenor=i+1
                            humedadHoraMayor=j
                            humedadDiaMayor=i+1
                            humedadHoraMenor=j
                            humedadDiaMenor=i+1
                            presionHoraMayor=j
                            presionDiaMayor=i+1
                            presionHoraMenor=j
                            presionDiaMenor=i+1
                        else:
                            if temperaturaMayor<self.__listaRegistros[i][j].getTemperatura():
                                temperaturaMayor=self.__listaRegistros[i][j].getTemperatura()
                                temperaturaHoraMayor=j
                                temperaturaDiaMayor=i+1
                            elif temperaturaMenor>self.__listaRegistros[i][j].getTemperatura():
                                temperaturaMenor=self.__listaRegistros[i][j].getTemperatura()
                                temperaturaHoraMenor=j
                                temperaturaDiaMenor=i+1
                            if humedadMayor<self.__listaRegistros[i][j].getHumedad():
                                humedadMayor=self.__listaRegistros[i][j].getHumedad()
                                humedadHoraMayor=j
                                humedadDiaMayor=i+1
                            elif humedadMenor>self.__listaRegistros[i][j].getHumedad():
                                humedadMenor=self.__listaRegistros[i][j].getHumedad()
                                humedadHoraMenor=j
                                humedadDiaMenor=i+1
                            if presionMayor<self.__listaRegistros[i][j].getPresion():
                                presionMayor=self.__listaRegistros[i][j].getPresion()
                                presionHoraMayor=j
                                presionDiaMayor=i+1
                            elif presionMenor>self.__listaRegistros[i][j].getPresion():
                                presionMenor=self.__listaRegistros[i][j].getPresion()
                                presionHoraMenor=j
                                presionDiaMenor=i+1
        print('{0:^10} {1:^10} {2:^10} {3:^10}'.format('','Temperatura','Humedad','Presion'))
        print('{0:^10} {1:^10d} {2:^10d} {3:^10d}'.format('Hora Mayor',temperaturaHoraMayor,humedadHoraMayor,presionHoraMayor))
        print('{0:^10} {1:^10d} {2:^10d} {3:^10d}'.format('Hora Menor',temperaturaHoraMenor,humedadHoraMenor,presionHoraMenor))
        print('{0:^10} {1:^10d} {2:^10d} {3:^10d}'.format('Dia Mayor',temperaturaDiaMayor,humedadDiaMayor,presionDiaMayor))
        print('{0:^10} {1:^10d} {2:^10d} {3:^10d}'.format('Dia Menor',temperaturaDiaMenor,humedadDiaMenor,presionDiaMenor))
    def temperaturaPromedioPorHora(self):
        print('{0:^10} {1:^24}'.format('Hora','Promedio de Temperatura'))
        for i in range(24):
            acumuladorT=0
            cantidad=0
            for dia in self.__listaRegistros:
                if len(dia)!=0:
                    if dia[i]!=None:
                        acumuladorT+= dia[i].getTemperatura()
                        cantidad+=1
            if cantidad!=0:
                print('{0:^10d} {1:^24.2f}'.format(i,acumuladorT/cantidad))
            else:
                print('{0:^10d} {1:^24d}'.format(i,0))
                
    def listarVariablesPorHoras(self,dia):
        if dia< len(self.__listaRegistros):
            if len(self.__listaRegistros[dia])==0:
                print('No se registraron horas del dia ingresado')
            else:
                print('{0:^10} {1:^10} {2:^10} {3:^10}'.format('Hora','Temperatura','Humedad','Presion'))
                for i in range(len(self.__listaRegistros[dia])):
                    if(self.__listaRegistros[dia][i]!=None):
                        print('{0:^10d} {1:^10d} {2:^10d} {3:^10d}'.format(i,self.__listaRegistros[dia][i].getTemperatura(),self.__listaRegistros[dia][i].getHumedad(),self.__listaRegistros[dia][i].getPresion()))
                    else:
                        print('{0:^10d} {1:^10d} {2:^10d} {3:^10d}'.format(i,0,0,0))
        else:
            print('El dia ingresado no es correcto')
    def test(self):
        print('Comienza test ManejadorRegistro')
        manejador=ManejadorRegistro()
        print('Metodo cargarDias()')
        manejador.cargarDias(30)
        print('Metodo cargarDesdeArchivo()')
        manejador.cargarDesdeArchivo()
        print('Metodo agregarRegistro()')
        manejador.agregarRegistro(Registro(5,15,800),22,22)
        manejador.agregarRegistro(Registro(7,20,815),22,23)
        manejador.agregarRegistro(Registro(8,21,820),22,0)
        print('Metodo cargarHoras()')
        manejador.cargarHoras(24) #dia 25
        manejador.agregarRegistro(Registro(50,60,790),24,0)
        print('Metodo mostrarValoresMayoresYMenores()')
        manejador.mostrarValoresMayoresYMenores()
        print('Metodo temperaturaPromedioPorHora()')
        manejador.temperaturaPromedioPorHora()
        print('Metodo listarVariablesPorHoras()')
        manejador.listarVariablesPorHoras(29)
        manejador.listarVariablesPorHoras(22)
        print('Fin test ManejadorRegistro. \n')