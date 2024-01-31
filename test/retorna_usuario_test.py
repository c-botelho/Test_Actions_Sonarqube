import unittest
import textwrap
import io
import sys
from banco import retorna_usuarios

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.usuarios = [
            {"nome": "Alice", "data_nascimento": "1990-01-01", "endereco": "123 Street", "cpf": "12345678901"},
            {"nome": "Bob", "data_nascimento": "1980-01-01", "endereco": "456 Avenue", "cpf": "23456789012"},
        ]

    def test_retorna_usuarios(self):
        expected_output = textwrap.dedent(f""" 
            CPF: {self.usuarios[0]['cpf']}
            Nome: {self.usuarios[0]['nome']}
            Data de Nascimento: {self.usuarios[0]['data_nascimento']}
            Endereço {self.usuarios[0]['endereco']}\n
        """) + "=" * 100 + "\n" + textwrap.dedent(f""" 
            CPF: {self.usuarios[1]['cpf']}
            Nome: {self.usuarios[1]['nome']}
            Data de Nascimento: {self.usuarios[1]['data_nascimento']}
            Endereço {self.usuarios[1]['endereco']}\n
        """) + "=" * 100 + "\n"

        stdout = sys.stdout  # Keep track of the previous value.
        sys.stdout = io.StringIO()  # Redirect stdout to a StringIO object.
        retorna_usuarios(self.usuarios)
        output = sys.stdout.getvalue()  # This will get the "printed" text.
        sys.stdout = stdout  # Restore stdout.
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()