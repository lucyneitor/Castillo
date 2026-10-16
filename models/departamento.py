# atributos clave id_departamento, nombre, gerente, presupuesto
class Departamento:
    def __init__(self, id_departamento:int, nombre:str, gerente:str, presupuesto:float):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.gerente = gerente
        self.presupuesto = presupuesto

    @property
    def id_departamento(self)-> int:
        return self._id_departamento

    @id_departamento.setter
    def id_departamento(self, value: int)-> None:
        self._id_departamento = value

    @property
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str)-> None:
        self._nombre = value

    @property
    def gerente(self)-> str:
        return self._gerente
    
    @gerente.setter
    def gerente(self, value: str)-> None:
        self._gerente = value

    @property
    def presupuesto(self)-> float:
        return self._presupuesto

    @presupuesto.setter
    def presupuesto(self, value: float)-> None:
        self._presupuesto = value

    def __repr__(self):
        return f"Departamento(id_departamento='{self.id_departamento}', nombre='{self.nombre}', gerente='{self.gerente}', presupuesto={self.presupuesto})"