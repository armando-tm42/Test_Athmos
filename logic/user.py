import regex as re
from .exceptions import ValueTooLargeError


class User(object):

    def __init__(self, id, nombres, apellidos, edad, email):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if type(id) is not int:
            raise TypeError("El id debe ser un entero")
        if id < 0:
            raise ValueError("El ide no puede ser menor que 0")
        self.__id = id

    @property
    def nombres(self):
        return self.__nombres

    @nombres.setter
    def nombres(self, nombres):

        if type(nombres) is not str:
            raise TypeError("Los nombres deben ser una cadena de caracteres")

        if len(nombres) > 52:
            raise ValueTooLargeError("Los nombres excedieron el largo permitido")

        self.__nombres = nombres

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):

        if type(apellidos) is not str:
            raise TypeError("Los Apellidos deben ser una cadena de caracteres")

        if len(apellidos) > 52:
            raise ValueTooLargeError("Los apellidos excedieron el largo permitido")

        self.__apellidos = apellidos

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):

        if type(edad) is not int:
            raise TypeError("La edad debe ser un numero entero")

        if edad < 0:
            raise ValueError("La edad no puede ser 0 o negativa")

        self.__edad = edad

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):

        valid_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if type(email) is not str:
            raise TypeError("El email debe ser una cadena de carateres")

        if len(email) > 256:
            raise ValueTooLargeError("El email excede el largo permitido")

        if re.fullmatch(valid_email, email) is None:
            raise ValueError("Email no valido")

        self.__email = email

    def __eq__(self, otro):
        if self.email == otro.email or self.id == otro.id:
            return True
        else:
            return False
