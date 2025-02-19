def categorias_severidade(valor):
    if valor == 1:
        return "Baixa"
    elif valor == 2:
        return "Média-Baixa"
    elif valor == 3:
        return "Média"
    else:
        return "Alta"


df["Severidade"] = df["Severity"].apply(categorias_severidade)
