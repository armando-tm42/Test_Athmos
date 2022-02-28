import sys
sys.path.append("..")
import unittest
from logic import User
from logic import exceptions


class TestUser(unittest.TestCase):

    def SetUp(self):
        pass

    def test_init(self):
        usuario = User(1, 'jhon', 'doe', 20, 'jhondoe@hotmail.com')
        self.assertEqual(usuario.id, 1)
        self.assertEqual(usuario.nombres, 'jhon')
        self.assertEqual(usuario.apellidos, 'doe')
        self.assertEqual(usuario.edad, 20)
        self.assertEqual(usuario.email, 'jhondoe@hotmail.com')

    def test_type_id(self):
        with self.assertRaises(TypeError):
            usuario = User('1', 'jhon', 'doe', 20, 'jhondoe@hotmail.com')

    def test_value_id(self):
        with self.assertRaises(ValueError):
            usuario = User(-1, 'jhon', 'doe', 20, 'jhondoe@hotmail.com')

    def test_type_nombres(self):
        with self.assertRaises(TypeError):
            usuario = User(1, 123, 'doe', 20, 'jhondoe@hotmail.com')

    def test_long_nombres(self):
        with self.assertRaises(exceptions.ValueTooLargeError):
            usuario = User(1, 'adasdasdasdasfsdgfdgfhgfhsfsafdasdasdgfdghgfhfhfghgfh', 'doe', 20, 'jhondoe@hotmail.com')

    def test_type_apellidos(self):
        with self.assertRaises(TypeError):
            usuario = User(1, 'jhon', 123, 20, 'jhondoe@hotmail.com')

    def test_long_apellidos(self):
        with self.assertRaises(exceptions.ValueTooLargeError):
            usuario = User(1, 'jhon', 'adasdasdasdasfsdgfdgfhgfhsfsafdasdasdgfdghgfhfhfghgfh', 20,
                           'jhondoe@hotmail.com')

    def test_type_edad(self):
        with self.assertRaises(TypeError):
            usuario = User(1, 'jhon', 'doe', '20', 'jhondoe@hotmail.com')

    def test_value_edad(self):
        with self.assertRaises(ValueError):
            usuario = User(1, 'jhon', 'doe', -20, 'jhondoe@hotmail.com')

    def test_equal(self):
        usuario = User(1, 'jhon', 'doe', 20, 'jhondoe@hotmail.com')
        self.assertTrue(usuario == User(1, 'jhon', 'doe', 20, 'jhondoe@hotmail.com'))


if __name__ == '__main__':
    unittest.main()
