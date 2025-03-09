import random

# print('Gerar cinco números aleatórios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1, 50)
#     print(f'Número gerado: {n}')

# --------------------------------------------------------

# valor = random.random()
# print(f'Número gerado: {round(valor * 10, 2)}')

# ---------------------------------------------------------

# valor = random.uniform(1, 100)
# print(f'Número: {round(valor, 4)}')

# ----------------------------------------------------------

# L = [2, 4, 6, 9, 23, 87.98, 65, 34, 63, 56, 90, 81, 23, 24]
# n = random.choice(L)
# print(f'Número escolhido: {n}')

# -----------------------------------------------------------

# L = [2, 4, 6, 9, 23, 87, 98, 65, 34, 63, 56, 90, 81, 23, 24]
# n = random.sample(L, 3)
# print(f'Os itens extraídos foram: {n}')

# -------------------------------------------------------------

# -Embaralhar
L = [2, 4, 6, 9, 23, 87.98, 65, 34, 63, 56, 90, 81, 23, 24]
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibi-la: ')
n = random.shuffle(L)
print(L)
