# Beggar my neighbour.
## I code it in december 2023 during my firtst weeks of my Python larning.
### Just add stopping condition (if the game takes too long) just before upload it to my github.


colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards=[]
aCard={}

for color in colors:
    for n in range(len(figures)):
        aCard=figures[n].copy()
        aCard.setdefault('Color',color)
        allCards.append(aCard)
      
aCard={}
import random
random.shuffle(allCards)  #cards shuffling
print(allCards,'\n')
player1=[]     #declaration empty lists for two players
player2=[]

for n in range(len(allCards)):      #cards dealing for players
    if n%2==0:
        player1.append(allCards[n])
    else:
        player2.append(allCards[n])        
print('player 1 have %d, cards are:' %(len(player1)), player1,'\n')
print('player 2 have %d, cards are:' %(len(player2)), player2,'\n')

i=0    #variable for iterations counting
stack=[] #declaring empty cards stock

while (len(player1)*len(player2))!=0: #check if any player have no cards
    if i<10000: #max number of iterations
        stack.append(player1.pop(0)) #we take one card from player 1
        stack.append(player2.pop(0)) #we take one card from player 2
        print('iteration ',i,': \t Card 1:',stack[0].get('Figure'), stack[0].get('Color'),'\t vs \t Card 2:',stack[1].get('Figure'), stack[1].get('Color'))  #displaying number of iteration and which cards are playing

        if stack[0].get('Power')>stack[1].get('Power'):  #player1 card is stronger
            player1.append(stack.pop(0))
            player1.append(stack.pop(0))
            print('Player 1 point.\t\t Result:\t', len(player1),'\t vs \t',len(player2),'\n')
        elif stack[0].get('Power')<stack[1].get('Power'): #player2 card is stronger
            player2.append(stack.pop(0))
            player2.append(stack.pop(0))
            print('Player 2 point.\t\t Result:\t', len(player1),'\t vs \t',len(player2),'\n')
        else:
            print('\nBATTLE!') #both cards have the same power
            battleIteration=1

            #below starts battle loop
            while (stack[len(stack)-2].get('Power'))==(stack[len(stack)-1].get('Power')):
                print("\nBattle iteration %d" %battleIteration) #displaying the number of battle iteration

                if len(player1)<2: #here we check if player1 have more than 2 cards
                    player2.extend(stack)
                    player2.extend(player1)
                    print('Player 1 does not have enough cards.')
                    player1=[]
                    stack=[]
                    break
                elif len(player2)<2: #here we check if player2 have more than 2 cards
                    player1.extend(stack)
                    player1.extend(player2)
                    print('Player 2 does not have enough cards.')
                    player2=[]
                    stack=[]
                    break
                else: #now if both players have more than 2 cards, we took 2 cards from each
                    stack.append(player1.pop(0)) #we took 1 card from player 1 for burn
                    stack.append(player2.pop(0)) #we took 1 card from player 2  for burn
                    print('Burned cards: \t\t Card 1:',stack[len(stack)-2].get('Figure'), stack[len(stack)-2].get('Color'),'\t & \t Card 2:',stack[len(stack)-1].get('Figure'), stack[len(stack)-1].get('Color'))
                    stack.append(player1.pop(0)) #second is to play
                    stack.append(player2.pop(0)) #second is to play
                    print('Battle between: \t Card 1:',stack[len(stack)-2].get('Figure'), stack[len(stack)-2].get('Color'),'\t vs \t Card 2:',stack[len(stack)-1].get('Figure'), stack[len(stack)-1].get('Color'))

                    if (stack[len(stack)-2].get('Power'))>(stack[len(stack)-1].get('Power')):
                        player1.extend(stack)

                    elif (stack[len(stack)-2].get('Power'))<(stack[len(stack)-1].get('Power')):
                        player2.extend(stack)
                    else:
                        battleIteration+=1
                        continue #if cards are equal again- then battle-loop is going again
                stack=[] #here we are clearing the stack
                print('\nResult:\t', len(player1),'\t vs \t',len(player2),'\n')
                break





    else:
        print(f"There were {i} iterations- probably no one wins till the end of the world :)")
        break
    i+=1
    # below we code the condition for displaying the winner
if i==10000:
    print("It's a draw! Play again ;)")
else:
    if len(player1) == 0:
        print('Player 2 WINS!\n')
    else:
        print('Player 1 WINS!\n')



    