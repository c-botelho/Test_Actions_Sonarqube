import unittest
from unittest.mock import patch
from banco import main

class TestBanco(unittest.TestCase):
    @patch('builtins.input', side_effect=["1", "100"])
    @patch('builtins.print')
    def test_main_deposito(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Depósito realizado com sucesso!")

    @patch('builtins.input', side_effect=["2", "50"])
    @patch('builtins.print')
    def test_main_saque(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Saque realizado com sucesso!")

    @patch('builtins.input', return_value="3")
    @patch('builtins.print')
    def test_main_extrato(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Seu saldo é: 0")

    @patch('builtins.input', side_effect=["4", "12345678901", "Alice", "1990-01-01", "123 Street"])
    @patch('builtins.print')
    def test_main_criar_usuario(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Usuário criado com sucesso!")

    @patch('builtins.input', side_effect=["5", "12345678901"])
    @patch('builtins.print')
    def test_main_criar_conta(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Conta criada com sucesso!")

    @patch('builtins.input', return_value="6")
    @patch('builtins.print')
    def test_main_retorna_usuarios(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Nenhum usuário cadastrado.")

    @patch('builtins.input', return_value="7")
    @patch('builtins.print')
    def test_main_retorna_contas(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Nenhuma conta cadastrada.")

    @patch('builtins.input', return_value="0")
    def test_main_sair(self, mock_input):
        self.assertIsNone(main())

    @patch('builtins.input', return_value="8")
    @patch('builtins.print')
    def test_main_invalido(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Operação inválida, por favor selecione novamente a operação desejada")

if __name__ == '__main__':
    unittest.main()