import unittest
from unittest.mock import patch
from src.banco import menu

class TestBanco(unittest.TestCase):
    @patch('builtins.input', return_value="1")
    def test_menu_depositar(self, input):
        self.assertEqual(menu(), "1")

    @patch('builtins.input', return_value="2")
    def test_menu_sacar(self, input):
        self.assertEqual(menu(), "2")

    @patch('builtins.input', return_value="3")
    def test_menu_extrato(self, input):
        self.assertEqual(menu(), "3")

    @patch('builtins.input', return_value="4")
    def test_menu_cadastrar_usuario(self, input):
        self.assertEqual(menu(), "4")

    @patch('builtins.input', return_value="5")
    def test_menu_criar_conta(self, input):
        self.assertEqual(menu(), "5")

    @patch('builtins.input', return_value="6")
    def test_menu_lista_usuarios(self, input):
        self.assertEqual(menu(), "6")

    @patch('builtins.input', return_value="7")
    def test_menu_lista_contas(self, input):
        self.assertEqual(menu(), "7")

    @patch('builtins.input', return_value="0")
    def test_menu_sair(self, input):
        self.assertEqual(menu(), "0")

if __name__ == '__main__':
    unittest.main()