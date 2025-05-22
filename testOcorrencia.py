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
        self.funcionario.addOcorrencia(self.ocorrencia)
        
    def teste1_cria_ocorrencia(self):
        self.assertEqual(self.ocorrencia.chave, "TASK-1")
        self.assertEqual(self.ocorrencia.resumo, "Implementar login")
        self.assertEqual(self.ocorrencia.tipo, "tarefa")
        self.assertEqual(self.ocorrencia.prioridade, "alta")
        self.assertEqual(self.ocorrencia.projeto, self.projeto)
        self.assertEqual(self.ocorrencia.responsavel, self.funcionario)
        self.assertEqual(self.ocorrencia.estado, "aberta")
    
    def teste2_fechar_ocorrencia(self):
        self.ocorrencia.fechar()
        
        self.assertEqual(self.ocorrencia.estado, "fechada")
    
    def teste3_mudar_responsavel_ocorrencia_aberta(self):
        novo_funcionario = Funcionario(id=2, nome="Gabriel Gomes", cargo="Desenvolvedor")
        self.projeto.addFuncionario(novo_funcionario)
        
        self.ocorrencia.mudar_responsavel(novo_funcionario)
        
        self.assertEqual(self.ocorrencia.responsavel, novo_funcionario)
    
    def teste4_mudar_responsavel_ocorrencia_fechada_raise_ValueError(self):
        novo_funcionario = Funcionario(id=2, nome="Gabriel Gomes", cargo="Desenvolvedor")
        self.projeto.addFuncionario(novo_funcionario)
        self.ocorrencia.fechar()
        
        with self.assertRaises(ValueError):
            self.ocorrencia.mudar_responsavel(novo_funcionario)
    
    def cria_dez_ocorrencias_para_o_funcionario(self, funcionario):
        lista_ocorrencias = []

        for i in range(10):
            ocorrencia = Ocorrencia(
                chave=f"TASK-{i}", 
                resumo=f"Tarefa {i}", 
                tipo="tarefa", 
                prioridade="media", 
                projeto=self.projeto, 
                responsavel=funcionario
            )
            funcionario.addOcorrencia(ocorrencia)
            lista_ocorrencias.append(ocorrencia)
        return lista_ocorrencias
    
    def teste5_mudar_responsavel_com_10_ocorrencias_raise_ValueError(self):
        novo_funcionario = Funcionario(id=2, nome="Gabriel Gomes", cargo="Desenvolvedor")
        self.projeto.addFuncionario(novo_funcionario)
        
        self.cria_dez_ocorrencias_para_o_funcionario(novo_funcionario)
        
        with self.assertRaises(ValueError):
            self.ocorrencia.mudar_responsavel(novo_funcionario)
    
    
    def teste6_ocorrencias_fechadas_nao_contam_para_limite(self):
        novo_funcionario = Funcionario(id=2, nome="Gabriel Gomes", cargo="Desenvolvedor")
        ocorrencias = self.cria_dez_ocorrencias_para_o_funcionario(novo_funcionario)    
        ocorrencias[0].fechar()
        nova_ocorrencia = Ocorrencia(
            chave="TASK-11", 
            resumo="Tarefa 11", 
            tipo="tarefa", 
            prioridade="media", 
            projeto=self.projeto, 
            responsavel=self.funcionario
        )
        novo_funcionario.addOcorrencia(nova_ocorrencia)

        self.assertEqual(nova_ocorrencia, novo_funcionario.getOcorrenciaByChave("TASK-11"))
    
    def teste7_cria_ocorrencia_com_tipo_valido_tarefa(self):
        tipo = "tarefa"
        ocorrencia = Ocorrencia(chave="TASK-1", resumo="resumo", tipo=tipo, prioridade="media", projeto=self.projeto, responsavel=self.funcionario)

        self.assertEqual(ocorrencia.chave, "TASK-1")
        self.assertEqual(ocorrencia.resumo, "resumo")
        self.assertEqual(ocorrencia.prioridade, "media")
        self.assertEqual(ocorrencia.projeto, self.projeto)
        self.assertEqual(ocorrencia.responsavel, self.funcionario)
        self.assertEqual(ocorrencia.tipo, tipo)
    
    def teste8_cria_ocorrencia_com_tipo_valido_bug(self):
        tipo = "bug"
        ocorrencia = Ocorrencia(chave="TASK-1", resumo="resumo", tipo=tipo, prioridade="media", projeto=self.projeto, responsavel=self.funcionario)

        self.assertEqual(ocorrencia.chave, "TASK-1")
        self.assertEqual(ocorrencia.resumo, "resumo")
        self.assertEqual(ocorrencia.prioridade, "media")
        self.assertEqual(ocorrencia.projeto, self.projeto)
        self.assertEqual(ocorrencia.responsavel, self.funcionario)
        self.assertEqual(ocorrencia.tipo, tipo)

    def teste9_cria_ocorrencia_com_tipo_valido_melhoria(self):
        tipo = "melhoria"
        ocorrencia = Ocorrencia(chave="TASK-1", resumo="resumo", tipo=tipo, prioridade="media", projeto=self.projeto, responsavel=self.funcionario)

        self.assertEqual(ocorrencia.chave, "TASK-1")
        self.assertEqual(ocorrencia.resumo, "resumo")
        self.assertEqual(ocorrencia.prioridade, "media")
        self.assertEqual(ocorrencia.projeto, self.projeto)
        self.assertEqual(ocorrencia.responsavel, self.funcionario)
        self.assertEqual(ocorrencia.tipo, tipo)
    
    def teste10_cria_ocorrencia_com_tipo_invalido_raises_ValueError(self):
        with self.assertRaises(ValueError):
            Ocorrencia(
                chave="INVALID-1", 
                resumo="Tipo inválido", 
                tipo="invalido", 
                prioridade="media", 
                projeto=self.projeto, 
                responsavel=self.funcionario
            )
    
    def teste11_cria_ocorrencia_com_prioridade_valida_baixa(self):
        prioridade = "baixa"
        ocorrencia = Ocorrencia(chave="TASK-1", resumo="resumo", tipo="tarefa", prioridade=prioridade, projeto=self.projeto, responsavel=self.funcionario)

        self.assertEqual(ocorrencia.chave, "TASK-1")
        self.assertEqual(ocorrencia.resumo, "resumo")
        self.assertEqual(ocorrencia.prioridade, prioridade)
        self.assertEqual(ocorrencia.projeto, self.projeto)
        self.assertEqual(ocorrencia.responsavel, self.funcionario)
        self.assertEqual(ocorrencia.tipo, "tarefa")
    
    def teste12_cria_ocorrencia_com_prioridade_valida_media(self):
        prioridade = "media"
        ocorrencia = Ocorrencia(chave="TASK-1", resumo="resumo", tipo="tarefa", prioridade=prioridade, projeto=self.projeto, responsavel=self.funcionario)

        self.assertEqual(ocorrencia.chave, "TASK-1")
        self.assertEqual(ocorrencia.resumo, "resumo")
        self.assertEqual(ocorrencia.prioridade, prioridade)
        self.assertEqual(ocorrencia.projeto, self.projeto)
        self.assertEqual(ocorrencia.responsavel, self.funcionario)
        self.assertEqual(ocorrencia.tipo, "tarefa")

    def teste13_cria_ocorrencia_com_prioridade_valida_alta(self):
        prioridade = "alta"
        ocorrencia = Ocorrencia(chave="TASK-1", resumo="resumo", tipo="tarefa", prioridade=prioridade, projeto=self.projeto, responsavel=self.funcionario)

        self.assertEqual(ocorrencia.chave, "TASK-1")
        self.assertEqual(ocorrencia.resumo, "resumo")
        self.assertEqual(ocorrencia.prioridade, prioridade)
        self.assertEqual(ocorrencia.projeto, self.projeto)
        self.assertEqual(ocorrencia.responsavel, self.funcionario)
        self.assertEqual(ocorrencia.tipo, "tarefa")
    
    def teste14_cria_ocorrencia_com_prioridade_invalida_raises_ValueError(self):
        with self.assertRaises(ValueError):
            Ocorrencia(
                chave="INVALID-1", 
                resumo="Tipo inválido", 
                tipo="tarefa", 
                prioridade="invalida", 
                projeto=self.projeto, 
                responsavel=self.funcionario
            )
    
    def teste15_mudar_prioridade_ocorrencia_aberta(self):
        self.ocorrencia.mudar_prioridade("baixa")

        self.assertEqual(self.ocorrencia.prioridade, "baixa")
        
    def teste16_mudar_prioridade_ocorrencia_fechada_raise_ValueError(self):
        self.ocorrencia.fechar()
        
        with self.assertRaises(ValueError):
            self.ocorrencia.mudar_prioridade("baixa")
            
    def teste17_mudar_para_prioridade_invalida_raise_ValueError(self):
        with self.assertRaises(ValueError):
            self.ocorrencia.mudar_prioridade("invalida")
    
    def teste18_mudar_responsavel_para_funcionario_de_outro_projeto_raise_ValueError(self):
        outro_projeto = Projeto(id=2, nome="Jornada do Estudante")
        funcionario_outro_projeto = Funcionario(id=3, nome="Lorenzo Zanela", cargo="Engenheiro")
        outro_projeto.addFuncionario(funcionario_outro_projeto)
        
        with self.assertRaises(ValueError):
            self.ocorrencia.mudar_responsavel(funcionario_outro_projeto)

    def test19_adicionar_mais_de_dez_ocorrencias_abertas_ao_funcionario_raise_ValueError(self):
        novo_funcionario = Funcionario(id=4, nome="Vitor Philip", cargo="Desempregado")
        self.cria_dez_ocorrencias_para_o_funcionario(novo_funcionario)
        nova_ocorrencia = Ocorrencia(
                chave="TASK-11", 
                resumo="tarefa 11", 
                tipo="tarefa", 
                prioridade="baixa", 
                projeto=self.projeto, 
                responsavel=""
            )

        with self.assertRaises(ValueError):
            novo_funcionario.addOcorrencia(nova_ocorrencia)
    
    def test20_ocorrencia_sem_responsavel_recebe_funcionario_como_responsavel(self):
        novo_funcionario = Funcionario(id=4, nome="Vitor Paz", cargo="Desempregado")
        nova_ocorrencia = Ocorrencia(
                chave="TASK-11", 
                resumo="tarefa 11", 
                tipo="tarefa", 
                prioridade="baixa", 
                projeto=self.projeto, 
                responsavel=""
            )
        
        novo_funcionario.addOcorrencia(nova_ocorrencia)

        self.assertEquals(novo_funcionario, nova_ocorrencia.responsavel)

if __name__ == "__main__":
    unittest.main()