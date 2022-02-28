from prettytable import PrettyTable


class Vista(object):

    @staticmethod
    def mostrar_lista(lista):
        print('\n')
        tabla = PrettyTable(['Id', 'Nombres', 'Apellidos', 'Edad', 'Email'])
        print('---LISTA DE USUARIOS---')
        for item in lista:
            tabla.add_row([item.id, item.nombres, item.apellidos, item.edad, item.email])
        print(tabla)
        print('\n')

    @staticmethod
    def mostrar_item(item):
        print('\n')
        print('Usuario encontrado')
        tabla = PrettyTable(['Id', 'Nombres', 'Apellidos', 'Edad', 'Email'])
        tabla.add_row([item.id, item.nombres, item.apellidos, item.edad, item.email])
        print(tabla)
        print('\n')

    @staticmethod
    def error_no_encontrado(nombres):
        print('\n')
        print('No se han encontrado regsitros con el valor ', nombres, ' en el campo nombres')
        print('\n')

    @staticmethod
    def error_duplicado(id, email):
        print('\n')
        print('Ya existe un usuario con el id: ', id, ' O con el email: ', email, ' En la lista ')
        print('\n')

    @staticmethod
    def lista_vacia():
        print('\n')
        print('La lista se encuentra vacia')
        print('\n')

    @staticmethod
    def mostrar_actualizado(id, nombres, apellidos, edad, email):
        print('\n')
        print('Nuevo valores actualizados ', ' Id: ', id, ' Nombres: ', nombres, ' Apellidos: ', apellidos,
              ' Edad: ', edad, ' Email: ', email)
        print('\n')

    @staticmethod
    def mostrar_eliminado(id):
        print('\n')
        print('EL usuario  con numero de Id ', id, ' Ha sido eliminado ')
        print('\n')

    @staticmethod
    def mostrar_agregado(id, nombres, apellidos, edad, email):
        print('\n')
        print('EL usuario ', ' Id: ', id, ' Nombres: ', nombres, ' Apellidos: ', apellidos,
              ' Edad: ', edad, ' Email: ', email, 'Ha sido añadido a la lista')
        print('\n')

    @staticmethod
    def error_id(id):
        print('\n')
        print('No se ha podido encontrar un usuario con el valor ', id, ' como Id ')
        print('\n')

    @staticmethod
    def guardar_db(nombre):
        print('\n')
        print('La lista se ha guardado en el archivo : ',nombre,' correctamente ')


    @staticmethod
    def mostrar_base(dbs):
        print('\n')
        tabla = PrettyTable(['Archivo', 'Fecha de modificación'])
        for index in range(len(dbs)):
            tabla.add_row([dbs[index]["Archivo"], dbs[index]["Fecha"]])
        print(tabla)
        print('\n')

    @staticmethod
    def eror_archivo(nombre_archivo):
        print('\n')
        print('No se encontro el archivo: ', nombre_archivo)
        print('\n')

    @staticmethod
    def eliminar_db(nombre_archivo):
        print('\n')
        print('El archivo : ', nombre_archivo, ' el archivo se elimino satisfactoriamente')

    @staticmethod
    def carga_usuarios():
        print('\n')
        print('Se han cargado los usuarios correctamente')

    @staticmethod
    def vaciar_lista():
        print('\n')
        print('La lista se ha vaciado correctamente')

