class Carreira:
    """Carreira com competências relevantes e pesos de importância."""

    def __init__(self, nome: str, competencias_relevantes: dict):
        self.nome = nome
        self.competencias_relevantes = competencias_relevantes

    def __str__(self):
        return self.nome