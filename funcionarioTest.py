import unittest
from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    def setUp(self):
        self.funcionario = Funcionario(id=1, nome="João Silva", cargo="Desenvolvedor")
    
    def teste1_cria_funcionario(self):
        self.assertEqual(self.funcionario.id, 1)
        self.assertEqual(self.funcionario.nome, "João Silva")
        self.assertEqual(self.funcionario.cargo, "Desenvolvedor")
        self.assertEqual(self.funcionario.projetos, [])