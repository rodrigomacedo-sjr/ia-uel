# Exercício 01: world-cities

## Descrição

O arquivo `worldcities.csv` é um conjunto de dados averto com alguns dados de cidades de inúmeros países e usaremos esse conjunto de dados para alguns exercícios. Portanto, é necessário prepará-lo.

Faça as seguintes etapas:

### Pré-processar os dados

Utilizando o arquivo `worldcities.csv`, filtre os dados para uma estrutura (tal como, Dataframe Pandas) apenas com cidades que sejam do estado do Paraná (Brasill).

### Modele os dados

- Selecionar aleatoriamente a quantidade de cidades vizinhas com estradas que as interligam (quantidade deve ser entre 2 ou 6 cidades)
- Calcular as n cidades mais próximas (n foi selecionado no item anterior) usando a fórmula de Haversine (sugestão, use o pacote haversine do Python)
- Fazer uma estrutura (utilizando dicionário) que represente as conexões (estradas) entre as cidades.

### Salve a estrutura

Salve os dados em um arquivo `JSON` ou `CSV` e submeta junto com o código utilizado para gerá-los.

## Instalação e Execução

## Minha Resoulução

1. Importar csv

2. Filtrar apenas cidades parana brasil
   https://www.youtube.com/watch?v=aV50X8oH83o

3. Selecionar aleatoriamente 2 a 6 cidades vizinhas
   https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
   https://stackoverflow.com/questions/73733987/select-random-value-from-pandas-dataframe-present-it-to-the-user-and-then-dele
   https://stackoverflow.com/questions/16476924/how-can-i-iterate-over-rows-in-a-pandas-dataframe

4. Calcular as n cidades mais próximas utilizando a fórmula de Haversine
   https://pypi.org/project/haversine/

5. Fazer um dicionário representando as estradas entre as cidades (ordenado pelas mais próximas)
   https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html

6. Salvar os dados em um JSON ou CSV
   https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

### Mais anotações

Utilizar o pacote `haversine` do python
Utilizar a biblioteca `NetworkX`
Não entendi onde entra a biblioteca `NetworkX` no exercício.
