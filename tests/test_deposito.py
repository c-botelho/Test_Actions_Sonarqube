import unittest
from banco import deposito

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.saldo = 100
        self.lista_extrato = []

    def test_deposito_positive(self):
        valor_deposito = 50
        new_saldo = deposito(self.saldo, valor_deposito, self.lista_extrato)
        self.assertEqual(new_saldo, 150)
        self.assertEqual(self.lista_extrato, [["Depósito", valor_deposito]])

    def test_deposito_zero(self):
        valor_deposito = 0
        new_saldo = deposito(self.saldo, valor_deposito, self.lista_extrato)
        self.assertEqual(new_saldo, self.saldo)
        self.assertEqual(self.lista_extrato, [])

    def test_deposito_negative(self):
        valor_deposito = -50
        new_saldo = deposito(self.saldo, valor_deposito, self.lista_extrato)
        self.assertEqual(new_saldo, self.saldo)
        self.assertEqual(self.lista_extrato, [])

if __name__ == '__main__':
    unittest.main()