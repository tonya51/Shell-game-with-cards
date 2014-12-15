import random
import time

replay = 'y'

while replay=='y' or replay=='yes':

    lista=[random.randint(1,12) for i in range(3)]
    i = random.randint(0,2)
    lista[i] = 'K'

    for j in range(3):
        if lista[j]==11:
            lista[j] = 'J'
        elif lista[j]==12:
            lista[j] = 'Q'

    print('The King is here...')
    time.sleep(2)
    print('...the King is there...')
    time.sleep(2)
    print('...Where is the King?')
    time.sleep(1)

    print('''\nPick a card!
.---.   .---.   .---.
|   |   |   |   |   |
| A |   | B |   | C |
|   |   |   |   |   |
'---'   '---'   '---' ''')

    x = input().upper()
    while x not in 'ABC':
        print('You didn\'t pick a card, pick again!')
        x = input().upper()

    if x=='A':
        chosenCard = 0
    elif x=='B':
        chosenCard = 1
    elif x=='C':
        chosenCard = 2

    time.sleep(1)
    print('\nWell, well...')
    time.sleep(1)
    
    if chosenCard==i:
        print('\nYou found the King!')
    else:
        print('\nYou didn\'t find the King...')
    print('You picked ', lista[chosenCard])

    time.sleep(1)
    print('\nA: ', lista[0], '\nB: ', lista[1], '\nC: ', lista[2])

    time.sleep(1)
    print('\nWould you like to play again? y or n?')
    replay = input().lower()
    while replay not in 'y yes n no':
        print('Was that y or n? Choose again.')
        replay = input().lower()
    
    if replay=='n' or replay=='no':
        break
    else:
        print('\n--------------------------------\n')
