# Dicionarios

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicionário possui {len(elemento)} elementos')

# Atualizar um entrada
elemento['grupo'] = 'Alcalinos'
print(elemento)

# Adicionar uma entrada
elemento['período'] = 1
print(elemento)

# # Exclusõ de itens em dicionários
# del elemento['período']
# print(elemento)

# # Apagar todo conteúdo
# elemento.clear()
# print(elemento)

print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f'{i}: {j}')
