import unittest
from banco import extrato
from io import StringIO
import sys

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.saldo = 1000
        self.lista_extrato = [["Depósito", 500], ["Saque", 200]]

    def test_extrato(self):
        expected_output = "\n".join([
            "===========Extrato===========",
            "\nDepósito - R$ 500.00",
            "\nSaque - R$ 200.00",
            "\nSaldo atual: R$ 1000.00",
            "==============================",
            ""
        ])
        actual_output = extrato(self.saldo, self.lista_extrato)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()