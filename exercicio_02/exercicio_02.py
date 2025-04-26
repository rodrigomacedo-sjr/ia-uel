import pandas as pd
from collections import deque


def importar_dados(nome_arquivo):
    data_frame = pd.read_csv(nome_arquivo)
    lista_adjacencia = {}
    for _, row in data_frame.iterrows():
        lista_adjacencia[row["cidade"]] = row["vizinhos"].split(", ")
    return lista_adjacencia


def bfs(lista_adjacencia, origem, destino):
    visitado = set()
    pai = {}

    fila = deque([origem])
    visitado.add(origem)

    while fila:
        atual = fila.popleft()
        if atual == destino:
            caminho = []
            no = destino
            while no != origem:
                # Percorre a lista de nós "antes"
                caminho.append(no)
                no = pai[no]
            caminho.append(origem)
            caminho.reverse()
            return caminho

        for vizinho in lista_adjacencia.get(atual, []):
            if vizinho not in visitado:
                # Guarda o nó que veio antes
                visitado.add(vizinho)
                pai[vizinho] = atual
                fila.append(vizinho)

    return []


def exercicio_02(origem, destino):
    lista_adjacencia = importar_dados("dados.csv")
    return bfs(lista_adjacencia, origem, destino)


# Exemplo onde exite caminho: Londrina - Cambé
# Exemplo onde não exite caminho: Londrina - Marechal
print(exercicio_02("Londrina", "Cambé"))
