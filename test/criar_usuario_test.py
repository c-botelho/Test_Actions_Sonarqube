import unittest
from banco import criar_usuario

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.usuarios = [
            {"nome": "Alice", "data_nascimento": "1990-01-01", "endereco": "123 Street", "cpf": "12345678901"},
            {"nome": "Bob", "data_nascimento": "1980-01-01", "endereco": "456 Avenue", "cpf": "23456789012"},
        ]

    def test_criar_usuario_new(self):
        nome = "Carlos"
        data_nascimento = "2000-01-01"
        cpf = "34567890123"
        endereco = "789 Boulevard"
        result = criar_usuario(nome, data_nascimento, cpf, endereco, self.usuarios)
        self.assertEqual(result, "Usuário Criado!")
        self.assertEqual(self.usuarios[-1], {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})

    def test_criar_usuario_existing(self):
        nome = "Bob"
        data_nascimento = "1980-01-01"
        cpf = "23456789012"
        endereco = "456 Avenue"
        result = criar_usuario(nome, data_nascimento, cpf, endereco, self.usuarios)
        self.assertEqual(result, "Usuário com CPF já existente")
        self.assertEqual(len(self.usuarios), 2)

if __name__ == '__main__':
    unittest.main()