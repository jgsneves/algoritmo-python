class ProcessoSeletivo:
    inscritos = []
    aprovados = []
    reprovados = []

    def __init__(self) -> None:
        pass

    def getApprovedList(self):
        for candidato in self.inscritos:
            if candidato.isApproved():
                self.aprovados.append(candidato.nome)
            else:
                self.reprovados.append(candidato.nome)
        return self.aprovados