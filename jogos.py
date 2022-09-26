from Jogos_Alura.jogos import adivinhacao, forca


def escolher_jogo():
    print('-=' * 20)
    print('    Escolha o seu jogo!')
    print('-=' * 20)

    print('(1) Forca')
    print('(2) Adivinhação')

    jogo = int(input('Digite o jogo escolhido: '))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()


if __name__ == '__main__':
    escolher_jogo()

