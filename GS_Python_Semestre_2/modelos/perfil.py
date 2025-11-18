class Perfil:
    """Perfil profissional composto por diversas competências."""

    def __init__(self, nome: str):
        self.nome = nome
        self.competencias = {}  # {nome: Competencia}

    def adicionar_competencia(self, competencia):
        self.competencias[competencia.nome] = competencia

    def obter_nivel(self, nome_comp):
        return self.competencias.get(nome_comp, None)

    def __str__(self):
        texto = f"\nPerfil de {self.nome}\nCompetências:\n"
        for c in self.competencias.values():
            texto += f"  - {c}\n"
        return texto