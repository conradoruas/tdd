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
    
    def teste3_adiciona_unico_funcionario_ao_inves_de_lista_de_funcionarios_raise_TypeError(self):
        func_1 = Funcionario(id=1, nome="João Silva", cargo="Desenvolvedor")
        
        with self.assertRaises(TypeError):
            self.empresa.addFuncionarios(func_1)
    
    def teste4_adiciona_grupo_projetos(self):
        proj_1 = Projeto(id=1, nome="e-SUS")
        proj_2 = Projeto(id=2, nome="Jornada do Estudante")
        listaProjetos = [proj_1, proj_2]

        self.empresa.addProjetos(listaProjetos)

        self.assertEqual(self.empresa.id, 1)
        self.assertEqual(self.empresa.nome, "W")
        self.assertEqual(self.empresa.funcionarios, [])
        self.assertIn(proj_1, self.empresa.projetos)
        self.assertIn(proj_2, self.empresa.projetos)
    
    def teste5_adiciona_unico_projeto_ao_inves_de_lista_de_projetos_raise_TypeError(self):
        proj_1 = Projeto(id=1, nome="e-SUS")
        
        with self.assertRaises(TypeError):
            self.empresa.addProjetos(proj_1)
    
    def teste6_adiciona_funcionario(self):
        func_1 = Funcionario(id=1, nome="João Silva", cargo="Desenvolvedor")
        
        self.empresa.addFuncionario(func_1)

        self.assertEqual(self.empresa.id, 1)
        self.assertEqual(self.empresa.nome, "W")
        self.assertIn(func_1, self.empresa.funcionarios)
        self.assertEqual(self.empresa.projetos, [])
    
    def teste7_adiciona_projeto(self):
        proj_1 = Projeto(id=1, nome="e-SUS")
        
        self.empresa.addProjeto(proj_1)

        self.assertEqual(self.empresa.id, 1)
        self.assertEqual(self.empresa.nome, "W")
        self.assertEqual(self.empresa.funcionarios, [])
        self.assertIn(proj_1, self.empresa.projetos)

if __name__ == "__main__":
    unittest.main()
