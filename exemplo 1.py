import pandas as pd 


data ={
    'nome':['Ana', 'João' , 'Maria'],
    'idade':[23, 35, 29],
    'gênero':['F', 'M', 'F'],
    'altura':[1.70, 1.80, 1.65]
}
df = pd.DataFrame(data)
print(f'\n {df}')
# Printando variaveis quantitativa
# Idade
print('Exibindo idade')
print(df['idade'])

# Altura
print('exibindo altura')
print(df['altura'])
# qualitativa
# Genero
print('Exibindo Genero')
print(df['gênero'])