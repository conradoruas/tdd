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
    
    def teste2_adiciona_grupo_funcionarios(self):
        func_1 = Funcionario(id=1, nome="João Silva", cargo="Desenvolvedor")
        func_2 = Funcionario(id=2, nome="Pedro Amorim", cargo="QA")
        listaFuncionarios = [func_1, func_2]

        self.empresa.addFuncionarios(listaFuncionarios)

        self.assertEqual(self.empresa.id, 1)
        self.assertEqual(self.empresa.nome, "W")
        self.assertIn(func_1, self.empresa.funcionarios)
        self.assertIn(func_2, self.empresa.funcionarios)
        self.assertEqual(self.empresa.projetos, [])
    
    def teste3_adiciona_unico_funcionario_como_grupo_raise_TypeError(self):
        func_1 = Funcionario(id=1, nome="João Silva", cargo="Desenvolvedor")
        
        with self.assertRaises(TypeError):
            self.empresa.addFuncionarios(func_1)

if __name__ == "__main__":
    unittest.main()
