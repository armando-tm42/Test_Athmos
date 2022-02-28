import sys
sys.path.append("..")
import unittest
import os
from mvc import Modelo


class TestModel(unittest.TestCase):

    def setUp(self):
        self.ruta_db = os.path.join(os.path.dirname(os.getcwd()), 'db')

    def test_1_guardar_db(self):
        usuarios = [
            {
                "id": 1,
                "nombres": 'jhon',
                "apellidos": 'doe',
                "edad": 20,
                "email": 'jhondoe@hotmail.com'
            },
        ]
        modelo = Modelo(usuarios)
        modelo.guardar_db('Test.json')
        self.assertTrue(os.path.exists(os.path.join(self.ruta_db, 'Test.json')))

    def test_2_mostrar_db(self):
        usuarios = [
            {
                "id": 1,
                "nombres": 'jhon',
                "apellidos": 'doe',
                "edad": 20,
                "email": 'jhondoe@hotmail.com'
            },
        ]
        modelo = Modelo(usuarios)
        lista = modelo.mostrar_db()
        self.assertTrue(hasattr(lista, '__iter__'))

    def test_3_cargar_db(self):
        usuarios = [

        ]
        modelo = Modelo(usuarios)
        modelo.cargar_db('Test.json')
        self.assertTrue(modelo.mostrar_db())

    def test_4_eliminar_db(self):
        usuarios = [

        ]
        modelo = Modelo(usuarios)
        modelo.eliminar_db('Test.json')
        self.assertFalse(os.path.exists(os.path.join(self.ruta_db, 'Test.json')))


if __name__ == '__main__':
    unittest.main()
