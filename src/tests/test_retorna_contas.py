import unittest
import textwrap
import io
import sys
from src.banco import retorna_contas

class TestRetornaContas(unittest.TestCase):
    def setUp(self):
        self.contas = [
            {
                'agencia': '001',
                'usuario': {'nome': 'Alice'},
                'numero_conta': '1'
            },
            {
                'agencia': '002',
                'usuario': {'nome': 'Bob'},
                'numero_conta': '2'
            }
        ]

    def test_retorna_contas(self):
        expected_output = textwrap.dedent(f""" 
            Agencia: {self.contas[0]['agencia']}
            Títular: {self.contas[0]['usuario']['nome']} 
            Número da conta: {self.contas[0]['numero_conta']}\n
        """) + "=" * 100 + "\n" + textwrap.dedent(f""" 
            Agencia: {self.contas[1]['agencia']}
            Títular: {self.contas[1]['usuario']['nome']} 
            Número da conta: {self.contas[1]['numero_conta']}\n
        """) + "=" * 100 + "\n"

        stdout = sys.stdout  # Keep track of the previous value.
        sys.stdout = io.StringIO()  # Redirect stdout to a StringIO object.
        retorna_contas(self.contas)
        output = sys.stdout.getvalue()  # This will get the "printed" text.
        sys.stdout = stdout  # Restore stdout.
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()