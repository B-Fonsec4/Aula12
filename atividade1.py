import pandas as pd 


def  deco():
    print(30* '=')
    
dados = {
    'produto': ['Notebook', 'Smartphone', 'Tablet'],
    'codigo': [1, 2, 3],
    'unidades_vendidas': [120, 340, 210],
    'cor': ['preto', 'prata', 'azul'],
    'categoria':['eletrônicos','eletrônico', 'eletrônicos'],
    'preço': [3.500, 2500, 1200.50],
    'faturamento':[42000.0, 850000.0, 252105.0],
    'satisfacao':['alto', 'muito alto','medio']

}
df = pd.DataFrame(dados)
print(df)
# exibindo quantitativo

print('Exibindo unidades vendidas')
print(df['unidades_vendidas'])
deco()

print('exibindo preço')
print(df['preço'])
deco()

print('Exibindo faturamento')
print(df['faturamento'])
deco()

# exibindo qualitativo
print('exibindo produto')
print(df['produto'])
deco()

print('exibindo cor')
print(df['cor'])
deco()

print('exibindo categoria')
print(df['categoria'])
deco()

print('exibindo satisfação')
print(df['satisfacao'])
deco()

print('exibindo codigo')
print(df['codigo'])
deco()