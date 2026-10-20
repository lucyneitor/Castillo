import sqlite3 #pq esto???
from models.Empleado import empleado

class Proyecto:
    """
    La clase proyecto representa un proyecto en el que los trabajadores trabajan
    esto despues estara conectado con la base de datos de tiempo para gestionar estos
    """
    
    def _init_(self, nombre:str, descripcion:str, fecha_inicio:str, empleado:empleado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.empleado = empleado
        
    def _str_(self):
        return f"{self.nombre}: {self.descripcion}"

    """Nombre: Representamos el nombre del proyecto"""

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del proyecto no puede estar vacío")
        self._nombre = nombre.strip()
        return self._nombre

    """Descripcion: Representamos la descripcion del proyecto"""

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str) -> None:
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción del proyecto no puede estar vacía")
        self._descripcion = descripcion.strip()
        return self._descripcion

    """Fecha de inicio: Representamos la fecha de inicio del proyecto"""
    
    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: str) -> None:
        if not isinstance(fecha_inicio, str) or not fecha_inicio.strip():
            raise ValueError("La fecha de inicio del proyecto no puede estar vacía")
        self._fecha_inicio = fecha_inicio.strip()
        return self._fecha_inicio