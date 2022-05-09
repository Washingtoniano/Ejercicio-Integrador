class med():
    __idcama=int
    __idmed=int
    __nombre=str
    __monodroga=str
    __presentacion=str
    __cantidad=int
    __precio=int
    def __init__(self,idcama,idmed,nombre,monodroga,presentacion,cantidad,precio):
        self.__idcama=idcama
        self.__idmed=idmed
        self.__nombre=nombre
        self.__monodroga=monodroga
        self.__presentacion=presentacion
        self.__cantidad=cantidad
        self.__precio=precio
    def id(self):
        return(self.__idcama)
    def mono(self):
        return self.__monodroga
    def pre(self):
        return self.__presentacion
    def prec(self):
        return self.__precio

