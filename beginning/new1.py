import random


def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']

    # Computador escolhe aleatoriamente
    escolha_computador = random.choice(opcoes)

    # Jogador faz sua escolha
    escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    # Verifica se a escolha do jogador é válida
    if escolha_jogador not in opcoes:
        print("Escolha inválida!")
        return

    print(f"Você escolheu: {escolha_jogador}")
    print(f"O computador escolheu: {escolha_computador}")

    # Verifica o resultado
    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_jogador == 'papel' and escolha_computador == 'pedra') or \
         (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
        print("Você venceu!")
    else:
        print("Você perdeu!")


# Executa o jogo
jogar()
