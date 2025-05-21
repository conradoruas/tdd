class Ocorrencia:
    TIPOS_VALIDOS = ["tarefa", "bug", "melhoria"]

    def __init__(self, chave, resumo, tipo, prioridade, projeto, responsavel):
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido. Tipos válidos: {', '.join(self.TIPOS_VALIDOS)}")
        
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

        if novo_responsavel.hasLimiteDeOcorrencias():
            raise ValueError("Não é possível adicionar uma ocorrencia a um responsável que já tem 10 ocorrencias")
        
        self.responsavel.removeOcorrencia(self)
        novo_responsavel.addOcorrencia(self)
        self.responsavel = novo_responsavel