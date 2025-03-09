# idade = 18
# tem_habilitacao = False

# if idade >= 18:
#     if tem_habilitacao:
#         print("Você pode dirigir.")
#     else:
#         print("Você precisa de uma habilitação para dirigir.")
# else:
#     print("Você é menor de idade e não pode dirigir.")


# idade = 20
# mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
# print(mensagem)


idade = int(input("Digite sua idade: "))
tem_carteira = input(
    "Você tem carteira de motorista? (sim/não): ").strip().lower() == "sim"
esta_acompanhado = input(
    "Você está acompanhado de um responsável? (sim/não): ").strip().lower() == "sim"

if (idade >= 18 and tem_carteira) or esta_acompanhado:
    print("Você pode dirigir acompanhado.")
else:
    print("Você não pode dirigir.")
