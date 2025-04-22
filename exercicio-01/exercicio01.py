import pandas as pd

dataframe = pd.read_csv("worldcities.csv")

data_cidades_parana = dataframe[dataframe.admin_name == "Paraná"]

print(data_cidades_parana)
