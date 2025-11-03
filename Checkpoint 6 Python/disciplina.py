class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_informacoes(self):
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")

    def __str__(self):
        return f"{self.nome} ({self.professor})"