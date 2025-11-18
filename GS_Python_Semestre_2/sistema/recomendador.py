class RecomendadorCarreira:
    """Analisa o perfil e calcula a carreira mais adequada."""

    def __init__(self, carreiras):
        self.carreiras = carreiras

    def recomendar(self, perfil):
        resultados = []

        for carreira in self.carreiras:
            score = 0
            for comp, peso in carreira.competencias_relevantes.items():
                nivel_perfil = perfil.competencias.get(comp)
                if nivel_perfil:
                    score += nivel_perfil.nivel * peso
            resultados.append((carreira.nome, score))

        resultados.sort(key=lambda x: x[1], reverse=True)
        return resultados

    def recomendar_melhor(self, perfil):
        return self.recomendar(perfil)[0]