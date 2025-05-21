import unittest
from ocorrencia import Ocorrencia
from funcionario import Funcionario
from projeto import Projeto

class TestOcorrencia(unittest.TestCase):
    def setUp(self):
        self.projeto = Projeto(id=1, nome="e-SUS")
        self.funcionario = Funcionario(id=1, nome="João Silva", cargo="Desenvolvedor")
        self.projeto.addFuncionario(self.funcionario)
        
        self.ocorrencia = Ocorrencia(chave="TASK-1", resumo="Implementar login", tipo="tarefa", prioridade="alta", projeto=self.projeto, responsavel=self.funcionario)
        
    def teste1_cria_ocorrencia(self):
        self.assertEqual(self.ocorrencia.chave, "TASK-1")
        self.assertEqual(self.ocorrencia.resumo, "Implementar login")
        self.assertEqual(self.ocorrencia.tipo, "tarefa")
        self.assertEqual(self.ocorrencia.prioridade, "alta")
        self.assertEqual(self.ocorrencia.projeto, self.projeto)
        self.assertEqual(self.ocorrencia.responsavel, self.funcionario)
        self.assertEqual(self.ocorrencia.estado, "aberta")

if __name__ == "__main__":
    unittest.main()