from models.Empleado import empleado

# atributos clave id_departamento, nombre, gerente, presupuesto
class Departamento:
    def __init__(self, id_departamento:int, nombre:str, gerente:str, presupuesto:int):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.gerente = gerente
        self.presupuesto = presupuesto
        self.empleado = empleado 

    @property
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str)-> None:
        if not isinstance(value, str) or len(value.strip())>3:
            raise ValueError("El nombre debe ser al menos 3 caracteres")
        self._nombre = value

    @property
    def gerente(self)-> str:
        return self._gerente
    
    @gerente.setter
    def gerente(self, value: str)-> None:
        if not isinstance (value,str) or len(value.strip())<3:
            raise ValueError("el nombre del gerente debe ser al menos de 3 caracteres")
        self._gerente = value

    @property
    def presupuesto(self)-> int:
        return self._presupuesto

    @presupuesto.setter
    def presupuesto(self, value: int)-> None:
        if not isinstance(value, int):
            raise ValueError("El valor debe ser un numero")
        self._presupuesto = value

    def __repr__(self):
        return f"Departamento(id_departamento='{self.id_departamento}', nombre='{self.nombre}', gerente='{self.gerente}', presupuesto={self.presupuesto})"