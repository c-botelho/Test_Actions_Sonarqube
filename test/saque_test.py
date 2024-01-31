import unittest
from banco import saque

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.saldo = 1000
        self.lista_extrato = []
        self.numero_saques = 0
        self.limite_saques = 3
        self.limite = 500

    def test_saque_within_limits(self):
        valor_saque = 200
        new_saldo = saque(saldo=self.saldo, valor_saque=valor_saque, lista_extrato=self.lista_extrato, numero_saques=self.numero_saques, limite_saques=self.limite_saques, limite=self.limite)
        self.assertEqual(new_saldo, self.saldo - valor_saque)
        self.assertEqual(self.lista_extrato, [["Saque", valor_saque]])

    def test_saque_exceeds_limit(self):
        valor_saque = 600
        new_saldo = saque(saldo=self.saldo, valor_saque=valor_saque, lista_extrato=self.lista_extrato, numero_saques=self.numero_saques, limite_saques=self.limite_saques, limite=self.limite)
        self.assertEqual(new_saldo, None)
        self.assertEqual(self.lista_extrato, [])

    def test_saque_exceeds_number_of_withdrawals(self):
        self.numero_saques = 3
        valor_saque = 200
        new_saldo = saque(saldo=self.saldo, valor_saque=valor_saque, lista_extrato=self.lista_extrato, numero_saques=self.numero_saques, limite_saques=self.limite_saques, limite=self.limite)
        self.assertEqual(new_saldo, None)
        self.assertEqual(self.lista_extrato, [])

    def test_saque_exceeds_balance(self):
        valor_saque = 1200
        new_saldo = saque(saldo=self.saldo, valor_saque=valor_saque, lista_extrato=self.lista_extrato, numero_saques=self.numero_saques, limite_saques=self.limite_saques, limite=self.limite)
        self.assertEqual(new_saldo, None)
        self.assertEqual(self.lista_extrato, [])

if __name__ == '__main__':
    unittest.main()