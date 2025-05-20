import unittest
from projeto import Projeto

class TestProjeto(unittest.TestCase):
    def setUp(self):
        self.projeto = Projeto(id=1, nome="e-SUS")
    
    def teste1_cria_projeto(self):
        self.assertEqual(self.projeto.id, 1)
        self.assertEqual(self.projeto.nome, "e-SUS")
        self.assertEqual(self.projeto.funcionarios, [])
    
    def teste2_altera_nome_projeto(self):
        self.projeto.setNome("Jornada do Estudante")

        self.assertEqual(self.projeto.id, 1)
        self.assertEqual(self.projeto.nome, "Jornada do Estudante")
        self.assertEqual(self.projeto.funcionarios, [])
