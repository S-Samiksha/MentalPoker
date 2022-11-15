'''
Card Class

Functions:
* getCard - return card in string
* setSuit - translate into card suit from number
* getSuit - returns card suit
* setFace - translate into card face from number
* getNumFace - returns card face number (1-13)

Clubs (2-14)
Diamonds (15-27)
Hearts (28-40)
Spades (41-53)

'''

class Card:
    def __init__(self,*args):
        if len(args) == 1:
            if (args[0]<=1 or args[0]>53):
                print("Card must be between 2-53. Try again.")
                exit
            else:
                self.setSuit(args[0])
                self.setFace(args[0])

        else:
            print("Please enter 1 argument only.")

    def getCard(self):
        return "{} of {}".format(self.face,self.suit)
    
    def setSuit(self,num):
        if(num <= 14):
            self.suit = "Clubs"
        elif (num > 14 and num <= 27):
            self.suit = "Diamonds"
        elif (num > 27 and num <= 40):
            self.suit = "Hearts"
        else:
            self.suit = "Spades"

    def getSuit(self):
        return self.suit

    def setFace(self,card):
        if card <= 14:
            num = card-1
        elif (card > 14 and card <= 27):
            num = card-14
        elif (card > 27 and card <= 40):
            num = card-27
        else:
            num = card-40
        
        self.numFace = num

        if (num == 1):
            self.face = "Ace"
        elif (num == 2):
            self.face = "Two"
        elif (num == 3):
            self.face = "Three"
        elif (num == 4):
            self.face = "Four"
        elif (num == 5):
            self.face = "Five"
        elif (num == 6):
            self.face = "Six"
        elif (num == 7):
            self.face = "Seven"
        elif (num == 8):
            self.face = "Eight"
        elif (num == 9):
            self.face = "Nine"
        elif (num == 10):
            self.face = "Ten"
        elif (num == 11):
            self.face = "Jack"
        elif (num == 12):
            self.face = "Queen"
        elif (num == 13):
            self.face = "King"

    def getNumFace(self):
        return self.numFace
