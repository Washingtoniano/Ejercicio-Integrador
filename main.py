from Manejador_de_medicamentos import man
import os
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
    op=int(input( "Desea buscar otro paciente\n1-si 2-no\n"))
    if op==1:
        os.system('cls')
        while op==1:
            Nom=input ("Ingrese el nombre del paciente que desea buscar")
            id=unmaneC.buscar(Nom)
            unmaneM.buscar(id)
            op=int(input( "Desea buscar otro paciente\n1-si 2-no\n"))

