import random 
import os
def cards():
    card2 = ['azul', 'agua', 'verde', 'carro']
    random.shuffle(card2)
    card2 = (card2[0].upper())
    print(card2)

    card3 = ['azul', 'agua', 'verde', 'carro']
    random.shuffle(card3)
    card3 = (card3[0].upper())

    if card3 == card2:
        random.shuffle(card3)
        card3 = (card3[0].upper())
        print(card3)

    else:
         print(card3)

    card4 = ['azul', 'agua', 'verde', 'carro']
    random.shuffle(card4)
    card4 = (card4[0].upper())

    if card4 == card2:
        random.shuffle(card4)
        card4 = (card4[0].upper())
        print(card4)
    elif card4 == card3:
        random.shuffle(card4)
        card4 = (card4[0].upper())
        print(card4)
    else:
         print(card4)     


def escolher_grupo(group):
   if group == '1':
       print('Seu grupo agora é Azul')
   elif group == '2':
        print('Seu grupo agora é Branco')
   else: 
       print('Por favor escolha entre 1 ou 2')

def selecionar_palavra(palavra, card2):
    if card2 == palavra:
        print(f'Essa palavra pertence ao grupo Azul')

def start():
    print('ola, essas são as palavras do jogo')
    cards()
    group =  input(f' Escolha seu time. 1Azul{os.linesep}[1]-Branco{os.linesep}')
    escolher_grupo(group)
    palavra = input(f'Qual palavra você deseja escolher?')
    selecionar_palavra(palavra, cards)

if __name__ == '__main__':
    start()