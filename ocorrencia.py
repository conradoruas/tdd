class Ocorrencia:
    def __init__(self, chave, resumo, tipo, prioridade, projeto, responsavel):
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
        self.responsavel = novo_responsavel