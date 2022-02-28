from logic import user_crud
import json
import os
import time


class Modelo(object):

    def __init__(self, users):
        self.crear_items(users)
        self.ruta_db = 'db'

    def crear_item(self, id, nombres, apellidos, edad, email):
        user_crud.crear_usuario(id, nombres, apellidos, edad, email)

    def crear_items(self, usuarios):
        user_crud.crear_usuarios(usuarios)

    def leer_item(self, nombres):
        return user_crud.mostrar_usuario(nombres)

    def leer_items(self):
        return user_crud.mostrar_usuarios()

    def actualizar_item(self, id, nombres, apellidos, edad, email):
        user_crud.actualizar_usuario(id, nombres, apellidos, edad, email)

    def eliminar_item(self, id):
        user_crud.eliminar_usuario(id)

    def vaciar_lista(self):
        user_crud.vaciar_lista()

    def guardar_db(self, nombre_archivo):
        ruta_actual = os.getcwd()
        padre = os.path.dirname(ruta_actual)
        ruta_completa = os.path.join(padre, self.ruta_db, nombre_archivo)
        usuarios = []
        for user in user_crud.mostrar_usuarios():
            temp = {
                "id": user.id,
                "nombres": user.nombres,
                "apellidos": user.apellidos,
                "edad": user.edad,
                "email": user.email
            }
            usuarios.append(temp)
        lista = json.dumps(usuarios)
        archivo = open(ruta_completa, "w")
        archivo.write(lista)
        archivo.close()

    def mostrar_db(self):
        ruta_actual = os.getcwd()
        padre = os.path.dirname(ruta_actual)
        ruta_dbs = os.path.join(padre, self.ruta_db)
        dbs = os.listdir(ruta_dbs)
        archivos = []
        for db in dbs:
            temp = {
                "Archivo": db,
                "Fecha": time.ctime(os.path.getmtime(os.path.join(ruta_dbs, db)))
            }
            archivos.append(temp)
        return archivos

    def cargar_db(self, nombre_archivo):
        ruta_actual = os.getcwd()
        padre = os.path.dirname(ruta_actual)
        ruta_dbs = os.path.join(padre, self.ruta_db)
        ruta_completa = os.path.join(ruta_dbs, nombre_archivo)
        archivo = open(ruta_completa, "r")
        lista = json.loads(archivo.read())
        usuarios = []
        for i in lista:
            usuarios.append(i)
        user_crud.crear_usuarios(lista)
        archivo.close()

    def eliminar_db(self, nombre_archivo):
        ruta_actual = os.getcwd()
        padre = os.path.dirname(ruta_actual)
        ruta_dbs = os.path.join(padre, self.ruta_db)
        ruta_completa = os.path.join(ruta_dbs, nombre_archivo)
        os.remove(ruta_completa)
