class Competencia:
    """Representa uma competência com nome e nível (0–10)."""

    def __init__(self, nome: str, nivel: int):
        self.nome = nome
        self.nivel = nivel

    def __str__(self):
        return f"{self.nome}: {self.nivel}/10"