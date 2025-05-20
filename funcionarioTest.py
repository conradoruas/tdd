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
    
    def teste2_altera_nome_funcionario(self):
        self.funcionario.setNome("Abraão Medeiros")

        self.assertEqual(self.funcionario.id, 1)
        self.assertEqual(self.funcionario.nome, "Abraão Medeiros")
        self.assertEqual(self.funcionario.cargo, "Desenvolvedor")
        self.assertEqual(self.funcionario.projetos, [])

if __name__ == "__main__":
    unittest.main()