from pyswip import Prolog
import pandas as pd
from sklearn.linear_model import LogisticRegression

# 1. Inicializa o motor do Prolog e carrega as regras lógicas
prolog = Prolog()
prolog.consult("rede_social.pl")

# 2. Carrega a tabela clássica usando o Pandas
df = pd.read_csv("dados_financeiros.csv")

# 3. Função que consulta o Prolog para extrair o grau de risco na rede
def obter_grau_risco(nome):
    query = list(prolog.query(f"risco_conexao({nome}, daniel, Grau)"))
    if query:
        return query[0]["Grau"]  # Captura o grau numérico calculado pelo Prolog
    return 999  # Caso não haja conexão na rede

# Cria a nova feature unindo os dados relacionais ao DataFrame
df['grau_risco_rede'] = df['cliente_id'].apply(obter_grau_risco)

print("--- DataFrame Enriquecido com Dados do Prolog ---")
print(df)
print("-" * 60)

# 4. Divide as features e o alvo para treinar a estatística
X = df[['renda_mensal', 'score_classico', 'grau_risco_rede']]
y = df['inadimplente_historico']

# 5. Treina o classificador de Regressão Logística
modelo = LogisticRegression()
modelo.fit(X, y)

# 6. Inferência Neuro-Simbólica (Formata a regra estilo ProbLog)

novo_cliente = pd.DataFrame([[5200, 750, 3]], columns=['renda_mensal', 'score_classico', 'grau_risco_rede'])
probabilidade = modelo.predict_proba(novo_cliente)[0][1]

print("Saída Relacional Estatística (Explicação XAI):")
print(f"{probabilidade:.2f} :: risco(joao) :- conectado_a(joao, daniel, 3).")