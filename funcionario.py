class Funcionario:
    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.projetos = []
    
    def setNome(self, nome):
        self.nome = nome
    
    def setCargo(self, cargo):
        self.cargo = cargo