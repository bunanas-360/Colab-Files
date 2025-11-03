from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplina = {}

    def matricular(self, disciplina: Disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            self.notas_por_disciplina[disciplina.nome] = []
            print(f"{self.nome} matriculado em {disciplina.nome}.")
        else:
            print(f"{self.nome} já está matriculado em {disciplina.nome}.")

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        if disciplina.nome not in self.notas_por_disciplina:
            print(f"{self.nome} não está matriculado em {disciplina.nome}.")
            return
        self.notas_por_disciplina[disciplina.nome].append(nota)
        print(f"Nota {nota} adicionada em {disciplina.nome} para {self.nome}.")

    def media_em(self, disciplina: Disciplina) -> float:
        notas = self.notas_por_disciplina.get(disciplina.nome, [])
        if not notas:
            return 0.0
        return sum(notas) / len(notas)

    def media_geral(self) -> float:
        medias = [self.media_em(d) for d in self.disciplinas if self.media_em(d) > 0]
        return sum(medias) / len(medias) if medias else 0.0

    def exibir_boletim(self):
        print(f"\nAluno: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}")
        if not self.disciplinas:
            print("Sem disciplinas matriculadas.")
            return
        for d in self.disciplinas:
            notas = self.notas_por_disciplina.get(d.nome, [])
            media = self.media_em(d)
            print(f"\n--- {d.nome} ---")
            print(f"Professor: {d.professor}")
            print(f"Notas: {notas if notas else '—'}")
            print(f"Média: {media:.1f}")
        print(f"\nMÉDIA GERAL: {self.media_geral():.1f}")

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.curso}"