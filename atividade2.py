import pandas as pd 


produtos = ['notebook', 'smartphone', 'tablet', 'smartwatch', 'camera']
quantidade_estoque = [15, 30, 20, 10, 25]

estoque = pd.Series(quantidade_estoque, index=produtos)

print('Serie estoque de produto')
print(estoque)
# selecionando um valor espcifico pelo indice
print('\n quantidades de notebooks em estoque')
print(estoque['notebook'])

print('\n estoque de notebooks e camera: ')
print(estoque[['notebook', 'camera']].values)

print('\n Produtos com estoque abaixo de 20 unidades: ')
print(estoque[estoque < 20])

print('\n Aumentando o estoque em 5 unidades para todos os produtos: ')
print(estoque + 5)

precos = pd.Series([3500, 2500, 1200, 900, 1500], index=produtos)

print('\n valor total do estoque por produto (preço * quantidade): ')
print(precos + estoque)

