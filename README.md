# Aprendizado_Relacional_Estatistico

# Análise de Risco de Crédito Híbrido com Aprendizado Relacional Estatístico (SRL)

Este projeto implementa um sistema híbrido de análise de risco de crédito, unindo a capacidade de representação da lógica de primeira ordem (Prolog) com a calibração de incerteza estatística (Python/Scikit-Learn)

##  Como Executar o Projeto

### Pré-requisitos 
1. Ter o motor do [SWI-Prolog](https://www.swi-prolog.org/) instalado e configurado nas variáveis de ambiente (`PATH`) do sistema operacional.
2. Ter o Python 3.x instalado.

### Instalação das Dependências 
Abra o terminal na pasta do projeto e instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt


### Execução do Pipeline
Para acionar o motor lógico em segundo plano, realizar o enriquecimento relacional dos dados e calibrar os pesos estatísticos das regras, execute:
```bash
python app.py

--- DataFrame Enriquecido com Dados do Prolog ---
  cliente_id  renda_mensal  score_classico  inadimplente_historico  grau_risco_rede
0       joao          5200             750                       0                3
1        ana          3100             610                       0                2
2     carlos          1800             420                       1                1
------------------------------------------------------------
Saída Relacional Estatística (Explicação XAI):
0.00 :: risco(joao) :- conectado_a(joao, daniel, 3).

```markdown
# Análise de Risco de Crédito Híbrido com Aprendizado Relacional Estatístico (SRL)

Este projeto implementa um sistema híbrido de análise de risco de crédito, unindo a capacidade de representação da lógica de primeira ordem (Prolog) com a calibração de incerteza estatística (Python/Scikit-Learn)

##  Como Executar o Projeto

### Pré-requisitos
1. Ter o motor do [SWI-Prolog](https://www.swi-prolog.org/) instalado e configurado nas variáveis de ambiente (`PATH`) do sistema operacional.
2. Ter o Python 3.x instalado.

### Instalação das Dependências
Abra o terminal na pasta do projeto e instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt

```

### Execução do Pipeline

Para rodar a integração neuro-simbólica e calibrar os pesos das regras, execute:

```bash
python app.py

```

---

##  Resultados Obtidos

A execução do pipeline realiza a extração relacional via `pyswip`, monta o DataFrame enriquecido e treina o classificador estatístico. A saída gerada no console foi:

```text
--- DataFrame Enriquecido com Dados do Prolog ---
  cliente_id  renda_mensal  score_classico  inadimplente_historico  grau_risco_rede
0       joao          5200             750                       0                3
1        ana          3100             610                       0                2
2     carlos          1800             420                       1                1
------------------------------------------------------------
Saída Relacional Estatística (Explicação XAI):
0.00 :: risco(joao) :- conectado_a(joao, daniel, 3).

```

---

## Análise Crítica e Inteligência Artificial Explicável (XAI)

O paradigma de **Statistical Relational Learning (SRL)** aplicado neste projeto supera os limites do simbolismo clássico (mundos fechados, determinísticos e puramente binários) ao unificar a expressividade da Lógica de Primeira Ordem com a capacidade de generalização e tratamento de ruídos da estatística.

### 1. A Ponte Neuro-Simbólica via Python-Prolog

Utilizando a biblioteca `pyswip`, o script Python delega o raciocínio dedutivo ao motor do SWI-Prolog. O Prolog varre recursivamente o grafo de transações financeiras e calcula dinamicamente que o cliente `joao` possui um grau de distância **3** em relação ao nó sabidamente inadimplente (`daniel`). Essa métrica estrutural/relacional é injetada de forma vetorizada no DataFrame do Pandas, enriquecendo os dados tradicionais.

### 2. Calibração Paramétrica e Flexibilidade Estatística

Diferente de um sistema puramente lógico que aplicaria uma regra rígida de "Mundo Fechado" — barrando o `joao` pelo simples fato de ele pertencer à rede de contatos de um inadimplente —, o classificador de Regressão Logística pondera estatisticamente o impacto dessa conexão. O modelo analisa dados históricos passados para calibrar os coeficientes de cada característica (*features*).

### 3. Mitigação do Risco e Justificativa dos Pesos Aprendidos

Na inferência do cliente `joao`, a Regressão Logística cruzou sua excelente renda mensal (R$ 5.200) e seu alto score clássico (750) com o fator relacional de risco (distância 3). O algoritmo aprendeu que a solidez de seus atributos individuais mitiga o risco de sua posição periférica na rede de inadimplência. Consequentemente, a probabilidade estatística calculada tendeu matematicamente a **0.00**.

### 4. Alinhamento com os Conceitos de XAI (Explainable AI)

A formatação da saída segue o padrão de cláusulas probabilísticas inspiradas no **ProbLog** (`0.00 :: risco(joao) :- conectado_a(joao, daniel, 3).`). Esse formato cumpre rigorosamente o papel de uma IA Explicável para auditoria de crédito: ele não fornece uma resposta puramente opaca de caixa-preta, mas sim uma regra lógica inteligível para seres humanos acoplada ao rigor numérico da probabilidade estatística calibrada a partir dos dados.

```

```
