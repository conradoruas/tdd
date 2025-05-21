class Empresa:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.projetos = []
        self.funcionarios = []
    
    def addFuncionarios(self, funcionarios: list):
        for funcionario in funcionarios:
            self.funcionarios.append(funcionario)
    
    def addProjetos(self, projetos: list):
        for projeto in projetos:
            self.projetos.append(projeto)