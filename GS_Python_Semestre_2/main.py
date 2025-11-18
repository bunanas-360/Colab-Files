from modelos.competencia import Competencia
from modelos.perfil import Perfil
from modelos.carreira import Carreira
from sistema.recomendador import RecomendadorCarreira


def criar_carreiras_padrao():
    return [
        Carreira("Cientista de Dados", {
            "Lógica": 3,
            "Matemática": 3,
            "Criatividade": 1,
            "Análise": 2
        }),
        Carreira("Designer UX/UI", {
            "Criatividade": 3,
            "Comunicação": 2,
            "Empatia": 3
        }),
        Carreira("Desenvolvedor de Software", {
            "Lógica": 3,
            "Adaptabilidade": 2,
            "Colaboração": 1
        }),
        Carreira("Gerente de Projetos", {
            "Colaboração": 3,
            "Comunicação": 3,
            "Organização": 2
        })
    ]


def criar_perfil_usuario():
    print("\n======= Cadastro de Perfil =======")

    nome = input("Digite seu nome: ")
    perfil = Perfil(nome)

    competencias_disponiveis = [
        "Lógica",
        "Matemática",
        "Criatividade",
        "Análise",
        "Colaboração",
        "Comunicação",
        "Empatia",
        "Adaptabilidade",
        "Organização"
    ]

    print("\nAvalie suas competências de 0 a 10.\n")

    for comp in competencias_disponiveis:
        while True:
            try:
                nivel = int(input(f"{comp}: "))
                if 0 <= nivel <= 10:
                    break
                else:
                    print("Digite um número de 0 a 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

        perfil.adicionar_competencia(Competencia(comp, nivel))

    return perfil


def main():
    carreiras = criar_carreiras_padrao()
    recomendador = RecomendadorCarreira(carreiras)

    perfil = None  # Garantimos que a variável sempre existe

    while True:
        print("\n==== Sistema Inteligente de Orientação de Carreiras ====")
        print("1 - Criar perfil")
        print("2 - Analisar carreira recomendada")
        print("3 - Sair")
        opc = input("Escolha: ")

        if opc == "1":
            perfil = criar_perfil_usuario()
            print("\nPerfil criado:")
            print(perfil)

        elif opc == "2":
            if perfil is None:
                print("Crie um perfil primeiro!")
                continue

            resultados = recomendador.recomendar(perfil)
            print("\n=== Recomendações ===")
            for carreira, score in resultados:
                print(f"{carreira}: score {score}")

            melhor = recomendador.recomendar_melhor(perfil)
            print(f"\nCarreira mais indicada: {melhor[0]} (score {melhor[1]})")

        elif opc == "3":
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()