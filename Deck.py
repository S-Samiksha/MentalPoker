'''
Deck Class

Functions:
* init - forms deck of 52 cards
* createDeck - forms deck of 52 cards
* getDeck - returns deck in list
* shuffle - shuffles deck of cards
* pickCards -  picks 5 cards for self or opponent

'''
import random

class Deck:
    def __init__(self,*args):
        if len(args) == 0:
            self.createDeck()
        elif len(args) == 1:
            newDeck = args[0]
            self.setDeck(newDeck)
        else:
            print("Too many arguments. Please try again.")
    
    def createDeck(self):
        deck = [i for i in range(54)]
        deck.remove(0)
        deck.remove(1)
        self.deck = deck

    def setDeck(self,newDeck):
        if (len(newDeck) != 52):
            print("Number of cards must be 52. Please try again.")
        else:
            self.deck = newDeck
            print("Deck is updated.")

    def getDeck(self):
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)
        print("Deck is shuffled.")

    def pickCards(self):
        pickedNums = []
        i = 0
        deckSize = len(self.deck)
        while (i<5):
            x = input("Enter a number from 1-{} to pick a card: ".format(deckSize))

            if x.isdigit() == False:
                print("Error: Please enter an integer!")
            else:
                x = int(x)
                if (x in pickedNums):
                    print("Error: Card has already been picked!")

                elif (x < 1 or x > deckSize):
                    print("Error: Out of range. Please enter an integer from 1-{}!".format(deckSize))

                else:
                    pickedNums.append(x)
                    pickedNums.sort()
                    i += 1
                    if (5-i) == 1:
                        print("You have {} pick left.".format(5-i))
                    else:
                        print("You have {} picks left.".format(5-i))
                    print("Picked numbers: {}\n".format(pickedNums))
        
        pickedCards = []
        cards = []
        for num in pickedNums:
            card = self.deck[num-1]
            pickedCards.append(card)
        for card in pickedCards:
            self.deck.remove(card)
        print("Your picked cards are {}\n".format(pickedCards))
        return pickedCards