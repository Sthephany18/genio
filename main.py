from random import randint

print('#### Iníciando Jogo ####')

random = randint(0, 10)
chute = 0;
chances = 3;
while chute != random:
    chute = input('Chute um número entre 0 a 10: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('')
            print('Parabéns, você venceu! O número era {} '.format(random))

            break;
        else:
            print('')
            if chute > random:
                print('Você errou!!! Dica: É um número menor.')
            else:
                print('Você errou!!! Dica: É um número maior.')
            print('Você ainda possui {} chances.'.format(chances))
            print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram, você perdeu!')
            print('')
            break;

print('#### Fim do Jogo ####')


