from aluno import Aluno
from disciplina import Disciplina

class SistemaCRM:
    def __init__(self):
        self.alunos = []
        self.disciplinas = []

    def adicionar_aluno(self):
        nome = input("Nome do aluno: ")
        matricula = input("Matrícula: ")
        curso = input("Curso: ")
        aluno = Aluno(nome, matricula, curso)
        self.alunos.append(aluno)
        print(f"Aluno {nome} adicionado ao sistema.")

    def adicionar_disciplina(self):
        nome = input("Nome da disciplina: ")
        professor = input("Nome do professor: ")
        disciplina = Disciplina(nome, professor)
        self.disciplinas.append(disciplina)
        print(f"Disciplina {nome} cadastrada.")

    def buscar_aluno(self, matricula):
        for a in self.alunos:
            if a.matricula == matricula:
                return a
        print("Aluno não encontrado")
        return None

    def buscar_disciplina(self, nome):
        for d in self.disciplinas:
            if d.nome.lower() == nome.lower():
                return d
        print("Disciplina não encontrada.")
        return None

    def exibir_alunos(self):
        print("\n=== Alunos Cadastrados ===")
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in self.alunos:
            print(aluno)

    def exibir_disciplinas(self):
        print("\n=== Disciplinas Oferecidas ===")
        if not self.disciplinas:
            print("Nenhuma disciplina cadastrada.")
        for disc in self.disciplinas:
            print(disc)

    def matricular_aluno(self):
        matricula = input("Informe a matrícula do aluno: ")
        aluno = self.buscar_aluno(matricula)
        if not aluno:
            return
        nome_disc = input("Informe o nome da disciplina: ")
        disciplina = self.buscar_disciplina(nome_disc)
        if not disciplina:
            return
        aluno.matricular(disciplina)

    def adicionar_nota(self):
        matricula = input("Informe a matrícula do aluno: ")
        aluno = self.buscar_aluno(matricula)
        if not aluno:
            return
        nome_disc = input("Informe o nome da disciplina: ")
        disciplina = self.buscar_disciplina(nome_disc)
        if not disciplina:
            return
        try:
            nota = float(input("Digite a nota: "))
        except ValueError:
            print("Nota inválida.")
            return
        aluno.adicionar_nota(disciplina, nota)

    def exibir_boletim_aluno(self):
        matricula = input("Informe a matrícula do aluno: ")
        aluno = self.buscar_aluno(matricula)
        if aluno:
            aluno.exibir_boletim()

    def menu(self):
        while True:
            print("\n--- MINI-CRM ACADÊMICO ---")
            print("1 - Cadastrar aluno")
            print("2 - Cadastrar disciplina")
            print("3 - Matricular aluno em disciplina")
            print("4 - Adicionar nota")
            print("5 - Exibir boletim de aluno")
            print("6 - Listar alunos")
            print("7 - Listar disciplinas")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.adicionar_aluno()
            elif opcao == "2":
                self.adicionar_disciplina()
            elif opcao == "3":
                self.matricular_aluno()
            elif opcao == "4":
                self.adicionar_nota()
            elif opcao == "5":
                self.exibir_boletim_aluno()
            elif opcao == "6":
                self.exibir_alunos()
            elif opcao == "7":
                self.exibir_disciplinas()
            elif opcao == "0":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    sistema = SistemaCRM()
    sistema.menu()