import pandas as pd
from sklearn.linear_model import LinearRegression
import os

# Caminho do CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "consumo_energia_simulado.csv")

# Ler CSV
try:
    df = pd.read_csv(DATA_PATH, sep=";", encoding="latin1", on_bad_lines="skip")
except:
    df = pd.read_csv(DATA_PATH, sep=",", encoding="latin1", on_bad_lines="skip")

# Selecionar colunas importantes
colunas_desejadas = ["Setor Econômico - N1", "Consumo"]
df = df[colunas_desejadas]

df["Consumo"] = pd.to_numeric(df["Consumo"], errors="coerce")

# Criar codificação numérica do setor
df["SetorCod"] = df["Setor Econômico - N1"].astype("category").cat.codes

# Remover linhas com NaN
df = df.dropna(subset=["Consumo", "SetorCod"])

# Preparar dados para o modelo
X = df[["SetorCod"]]
y = df["Consumo"]

# Treinar modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)

# Gerar previsões por setor
setores = df["Setor Econômico - N1"].unique()
setores = df["Setor Econômico - N1"].unique()
setor_codigos = df.groupby("SetorCod").first().index.values.reshape(-1, 1)

setor_codigos_df = pd.DataFrame(setor_codigos, columns=["SetorCod"])
previsoes = modelo.predict(setor_codigos_df)

res = pd.DataFrame({
    "Setor Econômico - N1": setores,
    "Previsao_Consumo_MWh": previsoes
})

# Salvar previsões
os.makedirs("outputs", exist_ok=True)
res.to_csv("outputs/previsao_por_setor.csv", index=False)

print("\nPrevisões salvas em outputs/previsao_por_setor.csv")
print(res)
