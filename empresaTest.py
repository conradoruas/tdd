import unittest
from projeto import Projeto
from funcionario import Funcionario
from empresa import Empresa

class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa(id=1, nome="W")
    
    def teste1_cria_empresa(self):
        self.assertEqual(self.empresa.id, 1)
        self.assertEqual(self.empresa.nome, "W")
        self.assertEqual(self.empresa.funcionarios, [])
        self.assertEqual(self.empresa.projetos, [])
    

if __name__ == "__main__":
    unittest.main()
