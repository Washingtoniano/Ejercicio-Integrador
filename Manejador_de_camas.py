
from Cama import cama
import csv
class manejador():
    __arreglo=[]
    def __init__(self):
        self.__arreglo=[]
    def leer (self):
        archivo=open("camas.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band =False
        for fila in reader:
            if band==False:
                band=True
            else:
                unacama=cama(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__arreglo.append(unacama)
        archivo.close()
    def buscar(self,pa):
        band=False
        va=None
        for cama in self.__arreglo:
            if str.lower(cama.nom())==str.lower(pa):
                band=True
                fecha= input("Ingrese la fecha de alta del paciente")
                cama.alta(fecha)
                print (cama)
                va=int (cama.id())
                #print (type(va))
        if band==False:
            print ("Paciente no encotrado\n")
        else:
            return va
    def mostrar(self):
        for cam in self.__arreglo:
            print (cam)

