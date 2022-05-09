from Manejador_de_medicamentos import man
from Manejador_de_camas import manejador
if __name__ == '__main__':
    unmaneC=manejador()
    unmaneC.leer()
    unmaneM=man()
    unmaneM.leer()
    unmaneM.mostrar()
    unmaneC.mostrar()
    Nom=input ("Ingrese el nombre del paciente que desea buscar")
    id=unmaneC.buscar(Nom)
    unmaneM.buscar(id)
