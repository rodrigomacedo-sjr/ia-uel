from numpy.random import randint
import pandas as pd
from haversine import haversine

# Carrega os dados de todas as cidades
dataframe = pd.read_csv("worldcities.csv")

# Filtra apenas as cidades do Paraná
data_cidades_parana = dataframe[dataframe.admin_name == "Paraná"]

dicionario_vizinhos = {}

for index, row in data_cidades_parana.iterrows():
    cidade = row["city"]

    # Seleciona n vizinhos aleatórios
    n = randint(2, 6)
    vizinhos = data_cidades_parana.sample(n=n)

    # Calcula distâncias e guarda nomes ordenados
    origem = (row["lat"], row["lng"])
    distancias = []
    for _, vizinho in vizinhos.iterrows():
        destino = (vizinho["lat"], vizinho["lng"])
        distancia = haversine(origem, destino)
        distancias.append({"vizinho": vizinho["city"], "distancia": distancia})

    distancias.sort(key=lambda x: x["distancia"])
    dicionario_vizinhos[cidade] = [item["vizinho"] for item in distancias]

# Converte o dicionário em DataFrame e salva em CSV
df_output = pd.DataFrame(
    {
        "cidade": list(dicionario_vizinhos.keys()),
        "vizinhos": [", ".join(v) for v in dicionario_vizinhos.values()],
    }
)
df_output.to_csv("output.csv", index=False, encoding="utf-8")
