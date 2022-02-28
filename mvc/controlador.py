from logic import exceptions


class Controlador(object):

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def mostrar_lista(self):
        try:
            lista = self.modelo.leer_items()
            self.vista.mostrar_lista(lista)
        except exceptions.EmptyList as e:
            self.vista.lista_vacia()

    def mostrar_usuario(self, nombres):
        try:
            item = self.modelo.leer_item(nombres)
            self.vista.mostrar_item(item)
        except exceptions.ItemNotStored as e:
            self.vista.error_no_encontrado(nombres)

    def agregar_usuario(self, id, nombres, apellidos, edad, email):
        try:
            self.modelo.crear_item(id, nombres, apellidos, edad, email)
            self.vista.mostrar_agregado(id, nombres, apellidos, edad, email)

        except exceptions.ItemAlreadyStored as e:
            self.vista.error_duplicado(id, email)

    def actualizar_usuario(self, id, nombres, apellidos, edad, email):
        try:
            self.modelo.actualizar_item(id, nombres, apellidos, edad, email)
            self.vista.mostrar_actualizado(id, nombres, apellidos, edad, email)
        except exceptions.ItemNotStored as e:
            self.vista.error_id(id)

    def eliminar_usuario(self, id):
        try:
            self.modelo.eliminar_item(id)
            self.vista.mostrar_eliminado(id)
        except exceptions.IdNotFound as e:
            self.vista.error_id(id)

    def guardar(self, nombre_archivo):
        self.modelo.guardar_db(nombre_archivo)
        self.vista.guardar_db(nombre_archivo)

    def mostrar_archivos(self):
        archivos = self.modelo.mostrar_db()
        self.vista.mostrar_base(archivos)

    def cargar_usuarios(self, nombre_archivo):
        try:
            self.modelo.cargar_db(nombre_archivo)
            self.vista.carga_usuarios()
            return True
        except FileNotFoundError as e:
            self.vista.eror_archivo()

    def eliminar_db(self, nombre_Archivo):
        try:
            self.modelo.eliminar_db(nombre_Archivo)
            self.vista.eliminar_db(nombre_Archivo)
        except FileNotFoundError as e:
            self.vista.eror_archivo(nombre_Archivo)

    def vaciar_lista(self):
        self.modelo.vaciar_lista()
        self.vista.vaciar_lista()
