import csv

from Medicamentos import med
class man():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def leer(self):
        archivo=open("medicamentos.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for fila in reader:
            if(band==False):
                band=True
            else:
                unmedicamento=med(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__lista.append(unmedicamento)
        archivo.close()
    def buscar(self,va):
        print ("Medicamento\monodroga\tPresentacion\tCantidad\tPrecio\n")
        total=0
        for i in range (len(self.__lista)):
            if (self.__lista[i].id==va):
                total=total+int(self.__lista[i].prec())
                print ("{}\t{}\t{}\t",self.__lista[i].mono(),self.__lista[i].pre(),self.__lista[i].prec())
