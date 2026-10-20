import sqlite3
from models.Empleado import empleado

class Tiempo:

    """
    La clase tiempo representa cuanto demoran los trabajadores en realizar un proyecto
    esto despues estara conectado con la base de datos de proyecto para gestionar estos
    """
    
    def _init_(self, fecha:str, tiempo_trabajado:float, descripcion:str, empleado:empleado):
        self.fecha = fecha
        self.tiempo_trabajado = tiempo_trabajado
        self.descripcion = descripcion
        self.empleado = empleado

    def _str_(self):
        return (
            f"Fecha: {self.fecha}\n"
            f"Tiempo trabajado: {self.tiempo_trabajado} horas\n"
            f"Descripción: {self.descripcion}"
        )

    """Fecha: Representamos la fecha del trabajo"""

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha: str) -> None:
        if not isinstance(fecha, str) or not fecha.strip():
            raise ValueError("La fecha no puede estar vacía")
        self._fecha = fecha.strip()
        return self._fecha

    """Tiempo trabajado: Representamos el tiempo trabajado en horas"""

    @property
    def tiempo_trabajado(self):
        return self._tiempo_trabajado

    @tiempo_trabajado.setter
    def tiempo_trabajado(self, tiempo_trabajado:float) -> None:
        if isinstance(tiempo_trabajado, bool) or not isinstance(
            tiempo_trabajado, (int, float)
        ):
            raise ValueError("El tiempo trabajado debe ser un número")
        if tiempo_trabajado < 0:
            raise ValueError("El tiempo trabajado no puede ser negativo")
        self._tiempo_trabajado = tiempo_trabajado
        return self._tiempo_trabajado

    """Descripcion: Representamos la descripcion del trabajo"""

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción no puede estar vacía")
        self._descripcion = descripcion.strip()
        return self._descripcion