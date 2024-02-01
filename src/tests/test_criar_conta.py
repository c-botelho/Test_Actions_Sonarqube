import unittest
from src.banco import criar_conta, filtra_usuarios

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.usuarios = [
            {"nome": "Alice", "data_nascimento": "1990-01-01", "endereco": "123 Street", "cpf": "12345678901"},
            {"nome": "Bob", "data_nascimento": "1980-01-01", "endereco": "456 Avenue", "cpf": "23456789012"},
        ]
        self.contas = [
            {"agencia": "001", "usuario": self.usuarios[0], "numero_conta": 1},
            {"agencia": "002", "usuario": self.usuarios[1], "numero_conta": 2},
        ]

    def test_criar_conta_existing_user(self):
        cpf = "12345678901"
        agencia = "003"
        result = criar_conta(cpf, self.usuarios, self.contas, agencia)
        self.assertEqual(result, "Conta Criada com sucesso!")
        self.assertEqual(self.contas[-1], {"agencia": agencia, "usuario": filtra_usuarios(cpf, self.usuarios), "numero_conta": 3})

    def test_criar_conta_non_existing_user(self):
        cpf = "34567890123"
        agencia = "003"
        result = criar_conta(cpf, self.usuarios, self.contas, agencia)
        self.assertEqual(result, "Usuário não encontrado")
        self.assertEqual(len(self.contas), 2)

if __name__ == '__main__':
    unittest.main()