# Projeto SERS - Análise e Previsão de Consumo Energético

## Descrição

Este projeto realiza **análise e previsão do consumo de energia elétrica** no Brasil, utilizando dados de consumo por setor econômico e UF.  
Ele fornece:

- Estatísticas e gráficos do consumo por setor.
- Estimativa de desperdício energético (10% do consumo).
- Modelo de regressão linear para previsão de consumo por setor.
- Relatórios em Markdown e CSVs com resultados.

Esta versão **não utiliza dashboards** e é executada diretamente pelo terminal.

-------

## 🛠 Pré-requisitos

Python 3.8 ou superior.

Instale as bibliotecas necessárias:

bash
pip install pandas matplotlib seaborn scikit-learn tabulate

-------

## Execução

### Análise de Consumo

Executa análise estatística, gera gráfico de consumo por setor e calcula desperdício estimado.

bash
python analise_consumo.py

-----

### Saídas:

consumo_por_setor_N[número do setor].png → gráfico de barras do consumo por setor.

relatorio_analise.md → relatório em Markdown com consumo e desperdício.

O terminal exibe o consumo total por setor e o desperdício estimado.

-------

## Modelo de Previsão

Treina um modelo de regressão linear para prever consumo por setor econômico.

python modelo_precisao.py

-------

## Resultados

Gráficos e relatórios permitem identificar os setores que consomem mais energia.

O modelo de previsão ajuda a estimar o consumo futuro por setor.

A estimativa de desperdício (10%) fornece um parâmetro inicial para eficiência energética.

-----

### Saídas:

previsao_por_setor.csv → previsões do consumo por setor.

O terminal exibe o DataFrame com as previsões.

-------

## Observações

O CSV de entrada (consumo_energia_simulado.csv) deve conter, pelo menos, as seguintes colunas:

Data, TipoConsumidor, Sistema, UF, Setor Econômico - N1, Setor Econômico - N2, Setor Econômico - N3, 
Tipo Tensão - N1, Tipo Tensão - N2, Tipo Tensão - N3, Faixa de Consumo N1, Faixa de Consumo N2, 
Consumidores, Consumo

Linhas com valores faltantes em Consumidores ou Consumo são descartadas automaticamente.

Todos os gráficos e relatórios são salvos nas mesmas pastas onde os scripts são executados.

-------

## Créditos & Fonte dos Dados

Dados simulados baseados em:
- **Brazil’s Energy Consumption – Kaggle**

Integrantes:
Auro Vanetti de Moura Andrade   | RM: 563761
Enzo Hideki Kobayashi Nishida   | RM: 565052
Francisco Batista Nogueira Neto | RM: 565868