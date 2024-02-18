import random 

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

def start():
    print('ola')
    cards()

if __name__ == '__main__':
    start()