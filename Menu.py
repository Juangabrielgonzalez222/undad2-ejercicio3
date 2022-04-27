from Registro import Registro


class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.test,
            '5':self.salir
        }
    def lanzarMenu(self,manejador):
        #Menu opciones
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para mostrar de cada variable el día y hora de menor y mayor valor.')
            print('-Ingrese 2 para indicar la temperatura promedio mensual por cada hora.')
            print('-Ingrese 3 para dado un número de día listar los valores de las tres variables para cada hora.')
            print('-Ingrese 4 para ejecutar un test.')
            print('-Ingrese 5 para salir.')
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion=='1' or opcion=='2' or opcion=='3' or opcion=='4':
                ejecutar(manejador)
            else:
                ejecutar()
    def opcion1(self,manejador):
        manejador.mostrarValoresMayoresYMenores()
    def opcion2(self,manejador):
        manejador.temperaturaPromedioPorHora()
    def opcion3(self,manejador):
        numeroDia=int(input('Ingrese numero de dia: '))
        if numeroDia<1:
            print('El numero ingresado no es valido')
        else:
            manejador.listarVariablesPorHoras(numeroDia-1)
    def test(self,manejador):
        manejador.test()
        registro=Registro(10,10,1000)
        registro.test()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')