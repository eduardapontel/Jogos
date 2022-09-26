from random import randint
from time import sleep


def jogar():
    linha = '-=' * 20
    print(linha)
    print('    Bem vindo ao jogo de advinhação!')
    print(linha)
    sleep(1)
    print()

    numero_aleatorio = randint(1, 100)
    # numero_aleatorio = randrange(1, 101)

    nivel = 0
    pontos = 1000

    print('Níveis: ')
    sleep(1)
    print('(1) Fácil')
    sleep(1)
    print('(2) Intermediário')
    sleep(1)
    print('(3) Difícil')
    sleep(1)
    while nivel not in [1, 2, 3]:

        nivel = ''
        while type(nivel) != int:
            try:
                sleep(1)
                nivel = int(input('Digite o nível de dificuldade escolhido: '))
                sleep(1)
            except:
                sleep(1)
                print('Por favor digite um número inteiro!')

    # if nivel == 1:
    #     tentativas = 15
    # elif nivel == 2:
    #     tentativas = 10
    # else:
    #     tentativas = 5

    match nivel:
        case 1:
            tentativas = 15
        case 2:
            tentativas = 10
        case 3:
            tentativas = 5

    print()
    for rodada in range(1, tentativas + 1):
        sleep(1)
        print(linha)
        print()
        sleep(1)
        print(f'Tentativa n° {rodada} de {tentativas}')
        print()

        chute_int = ''
        while type(chute_int) != int:
            try:
                sleep(1)
                chute_int = int(input('Digite um número entre 1 e 100: '))
            except:
                sleep(1)
                print('Por favor digite um número inteiro!')

        sleep(1)
        print(f'Você digitou o número {chute_int}')
        print()

        acertou = numero_aleatorio == chute_int
        maior = numero_aleatorio > chute_int
        menor = numero_aleatorio < chute_int

        if chute_int < 1 or chute_int > 100:
            sleep(1)
            print('Você deve digitar um número entre 1 e 100')
            # para pular para próxima iteração do for

            if rodada == tentativas:
                sleep(1)
                print('Não foi dessa vez... Você errou!')
                sleep(1)
                print(f'O número secreto era {numero_aleatorio}. ', end='')
                pontos -= abs(numero_aleatorio - chute_int)
                if pontos > 0 and acertou:
                    sleep(1)
                    print(f'E você fez {pontos} pontos')
                else:
                    sleep(1)
                    print(f'E você fez 0 pontos')
                break

            print()
            continue

        if acertou:
            sleep(1)
            print(linha)
            print()
            sleep(1)
            print('PARÁBENS! VOCÊ ACERTOU!')
            if pontos > 0:
                sleep(1)
                print(f'Você fez {pontos} pontos')
            else:
                sleep(1)
                print(f'Você fez 0 pontos')
            break
        else:
            sleep(1)
            print('Não foi dessa vez... Você errou!')
            if rodada == tentativas:
                sleep(1)
                print(f'O número secreto era {numero_aleatorio}. E você fez 0 pontos')
            elif maior:
                sleep(1)
                print('O valor do número aleatório é maior do que o número digitado')
            elif menor:
                sleep(1)
                print('O valor do número aleatório é menor do que o número digitado')
            pontos -= abs(numero_aleatorio - chute_int)
            print()
    print()
    sleep(1)
    print('{:-^40}'.format(' FIM DO JOGO '))


if __name__ == '__main__':
    jogar()
