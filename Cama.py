class cama():
    __idcama=int
    __habitacion=int
    __estado=False
    __paciente=None
    __diagnostico=str
    __internacion=str
    __alta=None
    def __init__(self,id,habitacion,estado,paciente,diagnostico,internacion,alta):
        self.__idcama=id
        self.__habitacion=habitacion
        self.__estado=estado
        self.__paciente=paciente
        self.__diagnostico=diagnostico
        self.__internacion=internacion
        self.__alta=alta
    def nom(self):
        return(self.__paciente)
    def alta(self,fecha):
        self.__alta=fecha
    def id (self):
        return(self.__idcama)

    def __str__(self):
        return ("Paciente:{}\tCama:{}\tHabitacion:{}\nDiagonostico:{}\tFecha de internacion:{}\nFecha de Alta:{}".format(self.__paciente,self.__idcama,self.__habitacion,self.__diagnostico,self.__internacion,self.__alta))



