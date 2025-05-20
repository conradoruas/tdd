class Projeto:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.funcionarios = []
    
    def setNome(self, nome):
        self.nome = nome
    
    def addFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)