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
        band =False

        for medicamento in self.__lista:
            if int(medicamento.id())==va:
                band=True
        if band==True:
            print ("Medicamento\monodroga\tPresentacion\tCantidad\tPrecio\n")
            total=0
            for medicamento in  (self.__lista):
                if int(medicamento.id())==va:
                    total=total+(int(medicamento.prec())*int(medicamento.can()))
                    print ("{}".format(medicamento))
            print ("Total: ${}".format(total))
        else:
            print ("medicamento no encontrado")
    def mostrar(self):
        for medicamento in self.__lista:
            print (medicamento)
