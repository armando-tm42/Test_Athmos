import sys
sys.path.append("..")
import unittest
from logic import user_crud
from logic import exceptions
from logic import User


class TestUserCrud(unittest.TestCase):

    def Setup(self):
        pass

    def test_1_crear_usuario(self):
        user_crud.crear_usuario(1, 'jhon', 'doe', 20, 'jhondoe@hotmail.com')
        with self.assertRaises(exceptions.ItemAlreadyStored):
            user_crud.crear_usuario(1, 'jhon', 'doe', 20, 'jhondoe@hotmail.com')

    def test_2_crear_usuarios(self):
        usuarios = [
            {
                "id": 1,
                "nombres": 'jhon',
                "apellidos": 'doe',
                "edad": 20,
                "email": 'jhondoe@hotmail.com'
            },
        ]
        user_crud.crear_usuarios(usuarios)

        self.assertEqual(user_crud.mostrar_usuarios()[0], User(1, 'jhon', 'doe', 20, 'jhondoe@hotmail.com'))

    def test_3_mostrar_usuario(self):
        with self.assertRaises(exceptions.ItemNotStored):
            user_crud.mostrar_usuario('jane')

    def test_4_mostrar_usuarios(self):
        self.assertTrue(hasattr(user_crud.mostrar_usuarios(), '__iter__'))

    def test_5_actualizar_usuario(self):
        user_crud.actualizar_usuario(1, 'jane', 'doe', 23, 'janedoe@gmail.com')
        self.assertEqual(user_crud.mostrar_usuario('jane'), User(1, 'jane', 'doe', 23, 'janedoe@gmail.com'))

    def test_6_eliminar_usuarios(self):
        user_crud.eliminar_usuario(1)
        with self.assertRaises(exceptions.IdNotFound):
            user_crud.eliminar_usuario(1)


if __name__ == '__main__':
    unittest.main()
