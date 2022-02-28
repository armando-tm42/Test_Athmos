class Error(Exception):
    """Clase base para las excepciones personalizadas"""
    pass


class EmptyValueError(Error):
    """Se invoca cuando el campo esta vacio"""
    pass

class ValueTooLargeError(Error):
    """Se invoca cuando el campo excede el tamaño permitido"""
    pass

class ItemAlreadyStored(Error):
    """Se invoca cuando se intenta añadir un usuario duplicado"""
    pass

class ItemNotStored(Error):
    """Se invoca cuando se intenta añadir un usuario duplicado"""
    pass

class IdNotFound(Error):
    """Se invoca cuando se intenta eliminar un id que no se encuentra en lista"""
    pass

class EmptyList(Error):
    """Se invoca cuando la lista de usuarios esta vacia"""
    pass