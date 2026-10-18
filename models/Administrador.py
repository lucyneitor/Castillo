class administrador:
    def __init__(self, id_usuario:int,user:str,contrasenia:str,rut:str):
        self._id_usuario = id_usuario
        self._user = user
        self._contrasenia = contrasenia
        self._rut = rut

@property
def id_usuario(self)-> str:
    return self._id_usuario
@id_usuario.setter
def id_usuario(self,valor:int) -> None:
    self._id_usuario = valor

@property
def user(self) -> str:
    return self._user
@user.setter
def user(self,valor:str)-> None:
    self._user = valor

@property
def contrasenia(self)-> str:
    return self._contrasenia
@contrasenia.setter
def contrasenia(self,valor:str):
    self._contrasenia = valor

@property
def rut(self)-> str:
    return self._rut
@rut.setter
def rut(self,valor:str)->None:
    self._rut = valor