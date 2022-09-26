from random import randrange


def jogar():

    header()
    palavra_aleatoria = escolher_palavra()
    espacos = ['_' for letra in palavra_aleatoria]
    # for letra in palavra_aleatoria:
    #     espacos.append('_')

    tentativas = 7
    enforcou = False
    acertou = False

    forca(tentativas)
    mostrar_espacos(espacos)

    while not acertou and not enforcou:
        print()
        resposta = input('Digite uma letra: ').strip().upper()[0]

        if resposta in palavra_aleatoria:
            exibir_letra_correta(resposta, espacos, palavra_aleatoria)
        else:
            tentativas -= 1
            mostrar_chances(tentativas)

        enforcou = tentativas == 0
        acertou = '_' not in espacos

        forca(tentativas)
        mostrar_espacos(espacos)

        if acertou:
            print()
            mensagem_vencedor()
        elif not acertou and enforcou:
            mensagem_perdedor(palavra_aleatoria)


def escrever_linha():
    linha = '-=' * 20
    print(linha)


def header():
    escrever_linha()
    print('    Bem vindo ao jogo de forca!')
    escrever_linha()


def escolher_palavra():
    arquivo = open('palavras.txt', encoding="utf-8")
    palavras = []

    for palavra in arquivo:
        palavra = palavra.strip()
        palavras.append(palavra)
    arquivo.close()

    indice = randrange(0, len(palavras))
    palavra_aleatoria = palavras[indice].upper()
    return palavra_aleatoria


def mostrar_espacos(espacos):
    print('                ', end='')
    for espaco in espacos:
        print(f'{espaco}', end='')
    print('\n')
    escrever_linha()


def exibir_letra_correta(resposta, espacos, palavra_aleatoria):
    posicao = 0
    for letra in palavra_aleatoria:

        if resposta == letra:
            espacos[posicao] = resposta

        posicao += 1


def mostrar_chances(tentativas):
    print()
    print(f'Você errou! {tentativas} tentativas restantes.')


def mensagem_perdedor(palavra_aleatoria):
    print()
    print('Você foi enforcado! :C')
    print(f'A palavra era {palavra_aleatoria}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def forca(tentativas):
    print()
    print("  _______     ")
    print(" |/      |    ")

    if tentativas == 6:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif tentativas == 5:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif tentativas == 4:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif tentativas == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif tentativas == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif tentativas == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif tentativas == 0:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    else:
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    print(" |            ")
    print("_|___         ")


if __name__ == '__main__':
    jogar()
