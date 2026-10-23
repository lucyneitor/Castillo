from abc import ABC, abstractmethod

class persona(ABC):
    def __init__(self,rut:str,nombre:str,direccion:str,telefono:str,
                 correo:str,user:str,password:str):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.user = user
        self.password = password

# Obtencion de atributo mediante un metodo
    @property 
    def rut(self) -> str:
        return self._rut
    # guardar un valor del objeto METODO
    @rut.setter
    def rut(self, valor: str)-> None:
        self._rut = valor

    @property
    def nombre(self) -> str: 
        return self._nombre
    @nombre.setter
    def nombre(self, valor:str)-> None:
        self._nombre = valor
        
    @property
    def direccion(self)-> str:
        return self._direccion
    @direccion.setter
    def direccion(self, valor:str):
        self._direccion = valor
        
    @property
    def telefono(self)->str:
        return self._telefono 
    @telefono.setter
    def telefono(self,valor:str)->None:
        self._telefono = valor

    @property
    def correo(self)->str:
        return self._correo
    @correo.setter
    def correo(self, valor: str)->None:
        self._correo = valor

    def __repr__(self) -> str:
        return f"Persona:(rut={self.rut}, Nombre={self.nombre}, Direccion={self.direccion}, telefono={self.telegono}, correo={self.correo})"

    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass