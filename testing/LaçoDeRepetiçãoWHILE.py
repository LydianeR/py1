# -- While
nome = None

while True:
    print('Digite seu nome, ou X para parar: ')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem-vindo, {nome}')
print('Até logo!')
