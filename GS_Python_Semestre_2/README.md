# Sistema de Recomendação de Carreiras  
Projeto desenvolvido em Python utilizando Orientação a Objetos

## 🌟 Propósito do Projeto
Este sistema foi criado para analisar o perfil profissional de um usuário com base em diversas competências, tanto técnicas quanto comportamentais. A ideia é aproximar programação e desenvolvimento pessoal, oferecendo uma recomendação de carreiras que combina com o estilo e habilidades do usuário.

O programa atua como uma ferramenta simples de orientação profissional, simulando um sistema inteligente capaz de apoiar escolhas de carreira no contexto do futuro do trabalho.

------------------------------

## 🧠 O que o sistema faz
- Permite criar um perfil com nome e avaliação de competências.
- Armazena informações usando listas e dicionários.
- Analisa o perfil comparando as competências do usuário com os requisitos das carreiras.
- Gera uma lista de recomendações com pontuações.
- Indica a carreira mais compatível.
- Funciona totalmente pelo terminal (CLI) com menus interativos.

------------------------------

## 🛠 Tecnologias e Conceitos Utilizados
- **Python 3**
- **Programação Orientada a Objetos (POO)**
- Estruturas de dados: listas e dicionários
- Modularização de código
- Sistema de recomendação simples baseado em pesos

------------------------------

Cada pasta possui arquivos responsáveis por partes específicas do sistema, deixando o projeto organizado e fácil de entender.

------------------------------

## 🧩 Descrição das Classes

### **Competencia**
Representa cada habilidade com um nome e um nível de 0 a 10.

### **Perfil**
Agrupa todas as competências atribuídas pelo usuário.

### **Carreira**
Define profissões e lista quais competências são mais importantes para cada uma.

### **RecomendadorCarreira**
Compara o perfil criado com as carreiras disponíveis e calcula a pontuação de compatibilidade.

------------------------------

## ▶️ Como executar o projeto

1. Abra o projeto no PyCharm ou outro ambiente Python.
2. Execute o arquivo principal:
   ```bash
   python main.py