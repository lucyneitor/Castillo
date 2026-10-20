# Informe (id_informe, fecha, tipo, formato)
from datetime import date
from models.Empleado import empleado


class Informe:
    def __init__(self, id_informe:int, fecha:date, tipo:str, formato:str, empleado:empleado):
        self.id_informe = id_informe
        self.fecha = fecha
        self.tipo = tipo
        self.formato = formato
        self.empleado = empleado

    @property
    def id_informe(self)-> int:
        return self._id_informe

    @id_informe.setter
    def id_informe(self, value: int)-> None:
        self._id_informe = value

    @property
    def fecha(self)-> date:
        return self._fecha

    @fecha.setter
    def fecha(self, value: date)-> None:
        self._fecha = value

    @property
    def tipo(self)-> str:
        return self._tipo

    @tipo.setter
    def tipo(self, value: str)-> None:
        self._tipo = value

    @property
    def formato(self)-> str:
        return self._formato

    @formato.setter
    def formato(self, value: str)-> None:
        self._formato = value

    def __repr__(self):
        return f"Informe(id_informe='{self.id_informe}', fecha='{self.fecha}', tipo='{self.tipo}', formato='{self.formato}')"