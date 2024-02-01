import unittest
from src.banco import filtra_usuarios

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.usuarios = [
            {"nome": "Alice", "data_nascimento": "1990-01-01", "endereco": "123 Street", "cpf": "12345678901"},
            {"nome": "Bob", "data_nascimento": "1980-01-01", "endereco": "456 Avenue", "cpf": "23456789012"},
        ]

    def test_filtra_usuarios_existing(self):
        cpf = "12345678901"
        expected_output = {"nome": "Alice", "data_nascimento": "1990-01-01", "endereco": "123 Street", "cpf": "12345678901"}
        actual_output = filtra_usuarios(cpf, self.usuarios)
        self.assertEqual(actual_output, expected_output)

    def test_filtra_usuarios_non_existing(self):
        cpf = "34567890123"
        expected_output = None
        actual_output = filtra_usuarios(cpf, self.usuarios)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()