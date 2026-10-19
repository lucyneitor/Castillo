from datetime import date
from models.persona import persona


class empleado(persona):
    def __init__(self,area_trabajo:str,sueldo:int,inicio_contraro:date,rut:str,
                 nombre:str,direccion:str,telefono:str,correo:str):
        super().__init__(rut,nombre,direccion,telefono,correo)
        self._area_trabajo = area_trabajo
        self._sueldo = sueldo
        self._inicio_contrato = inicio_contraro
        
    @property
    def area_trabajo(self)-> str:
        return self._area_trabajo
    @area_trabajo.setter
    def area_trabajo (self,valor:str)-> None:
        self._area_trabajo = valor
    
    @property
    def sueldo(self)->int:
        return self._sueldo
    @sueldo.setter
    def sueldo (self, valor:int)-> None:
        self._sueldo = valor
    
    @property
    def inicio_contrato (self)-> str:
        return self._inicio_contrato
    @inicio_contrato.setter
    def inicio_contrato(self,valor:date) -> None:
        self._inicio_contrato = valor
    
    def __repr__(self) -> str:
            return f"Empleado:(area_trabajo={self._inicio_contrato}, sueldo={self._sueldo},inicio_contrado{self._inicio_contrato})"