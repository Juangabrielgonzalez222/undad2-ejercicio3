from ManejadorRegistro import ManejadorRegistro
from Menu import Menu

if __name__== '__main__':
    manejador=ManejadorRegistro()
    diasMes=int(input('Ingrese la cantidad de dias del mes:'))
    if diasMes<1:
        print('Cantidad de dias invalido')
    else:
        manejador.cargarDias(diasMes)
        manejador.cargarDesdeArchivo()
        menu=Menu()
        menu.lanzarMenu(manejador)