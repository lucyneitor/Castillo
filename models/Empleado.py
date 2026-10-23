from datetime import date
from models.persona import persona

ESTADO = ["activo", "inactivo", "vacaciones", "suspendido"] 

class empleado(persona):
    def __init__(self,id_departamento:int,sueldo:int,inicio_contrato:date,rut:str,
                 nombre:str,direccion:str,telefono:str,correo:str,user:str,password:str, rol_admin:bool, estado:str):
        super().__init__(rut,nombre,direccion,telefono,correo,
                         user,password)
        self._id_departamento = id_departamento
        self._sueldo = sueldo
        self._inicio_contrato = inicio_contrato
        self._rol_admin = rol_admin
        self._estado = estado  # Estado inicial del empleado
        
    @property
    def id_departamento(self)-> int:
        return self._id_departamento
    
    @id_departamento.setter
    def id_departamento (self,valor:int)-> None:
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("Identificador de area de trabajo debe ser un número positivo")
        self._id_departamento = valor
    
    @property
    def sueldo(self)->int:
        return self._sueldo
    
    @sueldo.setter
    def sueldo (self, valor:int)-> None:
        if not isinstance(valor,int) or valor < 0:
            raise ValueError("El sueldo debe ser un numero y no debe ser negativo")
        self._sueldo = valor

    @property
    def inicio_contrato (self)-> date:
            return self._inicio_contrato
        
    @inicio_contrato.setter
    def inicio_contrato(self,valor:date) -> None:
        if not isinstance(valor,date):
            raise ValueError("El dato ingresado debe ser una fecha")
        self._inicio_contrato = valor

    @property
    def rol_admin(self)->bool:
        return self._rol_admin

    @rol_admin.setter
    def rol_admin(self, valor:bool)-> None:
        if not isinstance(valor, bool):
            raise ValueError("El rol de administrador debe ser un booleano")
        self._rol_admin = valor

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, valor: str) -> None:
        if isinstance(valor,str) and valor in ESTADO:
            self._estado = valor
        else:
            raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(ESTADO)}")
    
    def __repr__(self) -> str:
            return f"Empleado:(area_trabajo={self._area_trabajo}, sueldo={self._sueldo}, inicio_contrato={self._inicio_contrato}, rol_admin={self._rol_admin}, estado={self._estado})"