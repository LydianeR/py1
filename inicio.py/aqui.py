# nome = input("Digite seu nome:")
# idade = int(input("Digite sua idade:"))
# peso = float(input("Digite o seu peso:"))

# print(nome)
# print(type(idade))
# print(type(peso))


# soma = 1 + 1
# multiplicacao = 4 * 4
# divisao = 30 / 3
# potencia = 7 ** 2

# print("soma", soma)
# print("multiplicação", multiplicacao)
# print("divisão", divisao)
# print("potência", potencia)


# idade = int(input("Informe sua idade"))

# if idade >= 18:
#     print("PERMITIDO!")
# else:
#     print("BARRADO!")


# salario = float(input("Informe seu salário:"))

# if salario <= 3000:
#     print("Programador júnior.")
# elif salario > 3000 and salario <= 6000:
#     print("Programador pleno")
# elif salario > 6000 and salario <= 15000:
#     print("Programador senior")
# else:
#     print("Gerente de projetos")


# lista_numeros = [1, 2, 3]

# print(lista_numeros[0])
# print(lista_numeros[1])
# print(lista_numeros[2])


# numeros = [10, 9, 8, 7, 6]

# print("Total:", len(numeros))
# print("menor valor:", min(numeros))
# print("maior valor:", max(numeros))


# notas = []

# for x in range(3):
#     codigo_aluno = input("RM: ")
#     nota = float(input("Nota: "))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)

# print("Quantidade de notas", len(notas))

# for n in notas:
#     codigo_aluno = n[0]
#     nota = n[1]
#     print("O RM", codigo_aluno, "tirou a nota:", nota)

notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    # alternativa: contador += 1
    contador = contador + 1
print("quantidade de notas", len(notas))
