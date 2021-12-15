import random

#Ace =1, Two = 2, Three = 3, Four = 4, Five = 5.... T = 10, J = 11, Q = 12, K = 13
deck=[]
player1Deck=[]
menuItems = ['Play','Display Scores','Display Cards','Win Percentage','Quit']
mapCards=['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','J','Q','K']
stats=[0,0,0] #number 0f games,computer wins, user wins
global flag
flag=False # winning flag that determines if a match has been won
def menu():
    for i in range (0,5):
        print("\t{}. {}".format((i+1),menuItems[i]))
    while True:
        choice=input('Enter a menu entry: ')
        if choice.isdigit():
            return int(choice)
        else:
            print('Enter an integer value from the menu!')
def initializeDeck():
    deck.clear()
    player1Deck.clear()
    for i in range(0,4):
        deck.extend(range(1,14))
        #print(deck)

def shuffleDeck():
    """ to create a random deck select a random index and move it to a new index while deleting its previous position """
    for i in deck:#loop 52 times
        changeIndex=random.randrange(0,52)
        newIndex=random.randrange(0,52)
        changeValue=deck[changeIndex]
        del deck[changeIndex]
        deck.insert(newIndex,changeValue)

def splitDeck():
    """ to split the deck every item from 0 to 1 is moved to a new list """
    for i in range(0,26):
        player1Deck.insert(i,deck[i])
        del deck[i]

def displayStatistics():
    """ the percentage is number of (wins/total battles)*100 """
    print('Number of games played:',stats[0])
    print('Number of battles won by computer:',stats[1])
    print('Number of battles won by user:',stats[1])
    nDashes=33
    dashes(nDashes)
    print('| Player \t| Percentage\t|')
    dashes(nDashes)
    print("| User \t\t| {:.1f}%\t\t|".format((stats[2]/stats[0])*100))
    print("| Computer\t| {:.1f}%\t\t|".format((stats[1]/stats[0])*100))
    dashes(nDashes)

def dashes(n):
    dash='-'
    for i in range(0,n):
        print(dash,end='')
    print('')
def printDeck():
    """ function to print the contents of current deck """
    print('#comp',deck)
    print('#user',player1Deck)
    maxLen=len(deck) if len(deck)>len(player1Deck) else len(player1Deck)
    sortDeck()
    nDashes=25
    dashes(nDashes)
    print('| Computer\t| User\t|')
    dashes(nDashes)
    for i in range(0,maxLen):
        if i>=len(deck) or i>=len(player1Deck):
            if i>=len(deck):
                card2=sortedPlayerDeck[i]-1
                print("| \t\t| {}\t|".format(mapCards[card2]))        
            elif i>=len(player1Deck):
                card1=sortedDeck[i]-1
                print("| {}\t\t| \t|".format(mapCards[card1]))        
            continue
        card1=sortedDeck[i]-1
        card2=sortedPlayerDeck[i]-1
        print("| {}\t\t| {}\t|".format(mapCards[card1],mapCards[card2]))
    dashes(nDashes)    

sortedDeck=[]
sortedPlayerDeck=[]
def sortDeck():
    for i in deck:
        sortedDeck.append(i)
    for i in player1Deck:
        sortedPlayerDeck.append(i)
    sortedDeck.sort()
    sortedPlayerDeck.sort()

def displayScore():
    nDashes=33
    dashes(nDashes)
    print('| Computer\t| User\t\t|')
    dashes(nDashes)
    print("| {} cards\t| {} cards\t|".format(len(deck),len(player1Deck)))
    dashes(nDashes) 

def war():
    if len(deck)<4 or len(player1Deck)<4:
        global flag
        flag=True
        print("user" if len(deck)<4 else "computer"," has few cards hence can't wage a war")
        winner("computer" if len(deck)<4 else "user")
        return
    #print four cards of each player
    nDashes=25
    dashes(nDashes)
    print('| Computer\t| User\t|')
    dashes(nDashes)
    for i in range (0,4):
        computerCard=deck[i]
        userCard=player1Deck[i]
        print("| {}\t\t| {}\t|".format(mapCards[computerCard-1],mapCards[userCard-1]))
    dashes(nDashes)
    #compare the 4th element of each array and delete accordingly
    if deck[3]>player1Deck[3]:
        print('Computer wins')
        stats[1]=stats[1]+1
        for i in range(0,4):
            deck.append(player1Deck[0])
            player1Deck.pop(0)
    else:
        print('User wins')
        stats[2]=stats[2]+1
        for i in range(0,4):
            player1Deck.append(deck[0])
            deck.pop(0)
    

def battle():
    """ card at index 0 is top deck """
    if len(deck)==0 or len(player1Deck)==0:
        global flag
        flag=True
        winner("user" if len(deck)==0 else "computer")
        return
    computerCard=deck[0]
    userCard=player1Deck[0]
    nDashes=25
    dashes(nDashes)
    print('| Computer\t| User\t|')
    dashes(nDashes)
    print("| {}\t\t| {}\t|".format(mapCards[computerCard-1],mapCards[userCard-1]))
    dashes(nDashes)
    if computerCard>userCard:
        print("Computer wins")
        stats[1]=stats[1]+1
        distributeCards('computer')
    elif computerCard==userCard:
        print('\t WAR')
        war()
    elif userCard>computerCard:
        print('User wins')
        stats[2]=stats[2]+1
        distributeCards('user')

def distributeCards(winner):
    """ finall index is the final card """
    if winner=='computer':
        deck.append(player1Deck[0])
        player1Deck.pop(0)
        deck.append(deck[0])
        deck.pop(0)
    elif winner=='user':
        player1Deck.append(deck[0])
        deck.pop(0)
        player1Deck.append(player1Deck[0])
        player1Deck.pop(0)

def winner(x):
    if flag:
        print('\t--------------------\n\t| WE HAVE A WINNER |\n\t--------------------')
        print("\t|     {} wins    |".format(x))
        print('\t--------------------')
        print('Have a good day')
pauseFlag=0

exitMainLoop=False
automate=True #Set to false to automate the game
while True:
    if exitMainLoop:
        break
    option=menu()
    if option==1:
        if pauseFlag==0:
            print("Starting game...")
            flag=False
            initializeDeck()
            stats[0]=0
            stats[1]=0
            stats[2]=0
            #Before shuffling#print(deck)
            shuffleDeck()
            #After shuffling#print(deck)
            #print('original deck length: ',len(deck)) #->Length of deck before splitting
            splitDeck()
            #print('Length of player 1 deck:',len(player1Deck),'& length of modified deck:',len(deck))
            #print('Player 1 deck',player1Deck) #->print half the deck
            #print('new deck',deck) #->print new deck
        else:
            print("continue game.")
        while True:
            if automate:
                char=input('Enter any character to play a card or \'pp\' to open menu or \'qq\' to quit: ')
                if char=='qq':
                    confirmation=input('Are you sure you want to exit the game, all progress will be lost \"Y/N\": ')
                    if confirmation=='y':
                        pauseFlag=0
                        exitMainLoop=True
                        break
                    else:
                        continue
                elif char=='pp':
                    pauseFlag=1
                    print('paused game')
                    break
            battle()
            stats[0]=stats[0]+1
            if flag:
                break
    elif option==2:
        displayScore()
    elif option==3:
        printDeck()
    elif option==4:
        displayStatistics()
    elif option==5:
        if pauseFlag==1:
            confirmation=input('Are you sure you want to exit the game, all progress will be lost \"Y/N\": ')
            if confirmation=='y':
                print("Closing game...")
                break
            else:
                continue
        else:
            break
    else:
        print('\nInvalid menu entry, Try again.')