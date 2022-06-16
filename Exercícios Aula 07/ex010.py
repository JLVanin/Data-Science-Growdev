# 10)Implemente um programa onde o usuário deve adivinhar as letras de uma
# palavra por meio de palpites. A palavra deve ser mostrada inicialmente com
# as letras substituídas por underlines, conforme exemplo abaixo.

# dados => _ _ _ _ _

# O usuário deve então palpitar sobre as letras que ele julga estarem na frase.
# A cada letra que errar, ele perde 1 ponto. A cada letra que ele acertar a
# mesma deve ser exibida na tela, exemplo:

# Palpite: d
# Saída: d _ d _ _

# Se completar a frase o usuário ganha o jogo, se sua pontuação zerar ele
# perde o jogo. Ao iniciar o jogo, a pontuação é de 4 pontos.

def main():
    palpite = 1
    palavra = 'dados'
    underlines = '_' * len(palavra)
    letras_erradas = []
    pontuacao = 4
    print(underlines)
    while palpite < 6:
        if pontuacao > 0:
            escolha = input('\nPalpite: ')
            if escolha in letras_erradas:
                print(f'\n{escolha} já foi utilizada, tente outra letra')
            elif escolha in palavra:
                print(f'\nAcertou!')
                pos = palavra.index(escolha)
                underlines = underlines[:pos] + escolha + underlines[pos+1:]
                print(underlines)
                if '_' not in underlines:
                    print('\nParabéns! Você ganhou o jogo!')
                    break
            else:
                print(f'\nLetra incorreta!')
                letras_erradas.append(escolha)
                pontuacao -= 1
                print(f'Você ainda tem {pontuacao} pontos.')
                print(underlines)
        else:
            print('Você zerou seus pontos!')
            break
        palpite += 1
    print('\nObrigado por jogar!')
main()