import unittest
from unittest.mock import patch
from src.banco import saque

class TestSaque(unittest.TestCase):
    def setUp(self):
        self.saldo = 1000
        self.valor_saque = 200
        self.lista_extrato = []
        self.numero_saques = 0
        self.limite_saques = 3
        self.limite = 500

    def test_saque_success(self):
        new_saldo = saque(saldo=self.saldo, valor_saque=self.valor_saque, lista_extrato=self.lista_extrato, 
                          numero_saques=self.numero_saques, limite_saques=self.limite_saques, limite=self.limite)
        self.assertEqual(new_saldo, self.saldo - self.valor_saque)
        self.assertEqual(self.lista_extrato, [["Saque", self.valor_saque]])

    @patch('builtins.print')
    def test_saque_exceeds_limite(self, mock_print):
        saque(saldo=self.saldo, valor_saque=600, lista_extrato=self.lista_extrato, 
              numero_saques=self.numero_saques, limite_saques=self.limite_saques, limite=self.limite)
        mock_print.assert_called_once_with("ERRO: Limite de saque é de R$500 reais")

    @patch('builtins.print')
    def test_saque_exceeds_limite_saques(self, mock_print):
        saque(saldo=self.saldo, valor_saque=self.valor_saque, lista_extrato=self.lista_extrato, 
              numero_saques=3, limite_saques=self.limite_saques, limite=self.limite)
        mock_print.assert_called_once_with("ERRO: Limite de números de saques atingido")

    @patch('builtins.print')
    def test_saque_insufficient_saldo(self, mock_print):
        saque(saldo=100, valor_saque=self.valor_saque, lista_extrato=self.lista_extrato, 
              numero_saques=self.numero_saques, limite_saques=self.limite_saques, limite=self.limite)
        mock_print.assert_called_once_with("Saldo insuficiente")

if __name__ == '__main__':
    unittest.main()