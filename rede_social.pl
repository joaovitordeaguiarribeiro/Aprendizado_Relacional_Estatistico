transacao_entre(joao, ana, 1500).
transacao_entre(ana, carlos, 800).
transacao_entre(carlos, daniel, 50).

inadimplente(daniel).

risco_conexao(X, Y, 1) :- transacao_entre(X, Y, _).
risco_conexao(X, Y, 1) :- transacao_entre(Y, X, _).
risco_conexao(X, Y, Grau) :- 
    transacao_entre(X, Z, _), 
    risco_conexao(Z, Y, GrauAnterior), 
    Grau is GrauAnterior + 1.