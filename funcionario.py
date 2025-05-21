class Funcionario:
    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.projetos = []
        self.ocorrencias = []
    
    def setNome(self, nome):
        self.nome = nome
    
    def setCargo(self, cargo):
        self.cargo = cargo
    
    def addProjeto(self, projeto):
        self.projetos.append(projeto)

    def removeProjeto(self, projeto):
        self.projetos.remove(projeto)
    
    def addOcorrencia(self, ocorrencia):
        if self.hasLimiteDeOcorrencias():
            raise ValueError("Funcionário atingiu o limite de 10 ocorrencias")
        self.ocorrencias.append(ocorrencia)

    def removeOcorrencia(self, ocorrencia):
        self.ocorrencias.remove(ocorrencia)

    def hasLimiteDeOcorrencias(self):
        count = sum(1 for ocorrencia in self.ocorrencias if ocorrencia.estado != "fechada")
        return count >= 10
    
    def getOcorrenciaByChave(self, chave):
        for ocorrencia in self.ocorrencias:
            if chave == ocorrencia.chave:
                return ocorrencia