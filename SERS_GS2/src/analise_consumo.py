import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Caminho do CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "consumo_energia_simulado.csv")

try:
    df = pd.read_csv(DATA_PATH, sep=";", encoding="latin1", on_bad_lines="skip")
except:
    df = pd.read_csv(DATA_PATH, sep=",", encoding="latin1", on_bad_lines="skip")

colunas_desejadas = [
    "Data",
    "TipoConsumidor",
    "Sistema",
    "UF",
    "Setor Econômico - N1",
    "Setor Econômico - N2",
    "Setor Econômico - N3",
    "Tipo Tensão - N1",
    "Tipo Tensão - N2",
    "Tipo Tensão - N3",
    "Faixa de Consumo N1",
    "Faixa de Consumo N2",
    "Consumidores",
    "Consumo"
]

df.columns = [c.strip() for c in df.columns]
df = df[colunas_desejadas]

# Converter colunas numéricas
df["Consumidores"] = pd.to_numeric(df["Consumidores"], errors="coerce")
df["Consumo"] = pd.to_numeric(df["Consumo"], errors="coerce")

# Criar pastas de saída
os.makedirs("outputs", exist_ok=True)
os.makedirs("docs", exist_ok=True)


# Função auxiliar para gráfico por setor
def gerar_grafico_setor(coluna_setor, nome_saida):
    consumo = df.groupby(coluna_setor)["Consumo"].sum().sort_values(ascending=False)

    print(f"\nConsumo total por {coluna_setor}:")
    print(consumo)

    # Criar DataFrame para o gráfico
    df_plot = consumo.reset_index()
    df_plot.columns = ["Setor", "Consumo"]

    # Plot
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Setor", y="Consumo", data=df_plot)

    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Consumo (MWh)")
    plt.title(f"Consumo Total por {coluna_setor}")
    plt.tight_layout()

    caminho = f"outputs/{nome_saida}"
    plt.savefig(caminho)
    plt.close()

    print(f"Gráfico salvo em: {caminho}")
    return consumo


# Gráficos e análises
consumo_n1 = gerar_grafico_setor("Setor Econômico - N1", "consumo_por_setor_N1.png")
consumo_n2 = gerar_grafico_setor("Setor Econômico - N2", "consumo_por_setor_N2.png")
consumo_n3 = gerar_grafico_setor("Setor Econômico - N3", "consumo_por_setor_N3.png")

# Estimativa de desperdício (10%)
df["Desperdicio_estimado"] = df["Consumo"] * 0.10
desperdicio_total = df["Desperdicio_estimado"].sum()
print(f"\nDesperdício total estimado: {desperdicio_total:.2f} MWh")

# Relatório em Markdown
with open("docs/relatorio_analise.md", "w", encoding="utf-8") as f:
    f.write("# Relatório de Análise Energética\n\n")

    f.write("## Consumo total por Setor Econômico - N1\n")
    f.write(consumo_n1.to_markdown() + "\n\n")

    f.write("## Consumo total por Setor Econômico - N2\n")
    f.write(consumo_n2.to_markdown() + "\n\n")

    f.write("## Consumo total por Setor Econômico - N3\n")
    f.write(consumo_n3.to_markdown() + "\n\n")

    f.write("## Desperdício estimado\n")
    f.write(f"{desperdicio_total:.2f} MWh\n")

print("\nRelatório salvo em docs/relatorio_analise.md")
