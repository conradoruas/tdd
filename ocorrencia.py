class Ocorrencia:
    TIPOS_VALIDOS = ["tarefa", "bug", "melhoria"]
    PRIORIDADES_VALIDAS = ["alta", "media", "baixa"]

    def __init__(self, chave, resumo, tipo, prioridade, projeto, responsavel):
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido. Tipos válidos: {', '.join(self.TIPOS_VALIDOS)}")

        if prioridade not in self.PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridade inválida. Prioridades válidas: {', '.join(self.PRIORIDADES_VALIDAS)}")
        
        self.chave = chave
        self.resumo = resumo
        self.tipo = tipo
        self.prioridade = prioridade
        self.projeto = projeto
        self.responsavel = responsavel
        self.estado = "aberta"
    
    def fechar(self):
        self.estado = "fechada"
    
    def mudar_responsavel(self, novo_responsavel):
        if self.estado == "fechada":
            raise ValueError("Não é possível mudar responsável de ocorrência fechada")

        if novo_responsavel not in self.projeto.funcionarios:
            raise ValueError("Novo responsável deve estar no projeto da ocorrência")

        if novo_responsavel.hasLimiteDeOcorrenciasAbertas():
            raise ValueError("Não é possível adicionar uma ocorrencia a um responsável que já tem 10 ocorrencias")
        
        self.responsavel.removeOcorrencia(self)
        novo_responsavel.addOcorrencia(self)
        self.responsavel = novo_responsavel
    
    def mudar_prioridade(self, nova_prioridade):
        if self.estado == "fechada":
            raise ValueError("Não é possível mudar prioridade de ocorrência fechada")
            
        if nova_prioridade not in self.PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridade inválida. Prioridades válidas: {', '.join(self.PRIORIDADES_VALIDAS)}")
            
        self.prioridade = nova_prioridade
    
    def setResponsavel(self, responsavel):
        self.responsavel = responsavel