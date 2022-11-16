'''
Card Class

Functions:
* getCard - return card in string
* setSuit - translate into card suit from number
* getSuit - returns card suit
* setFace - translate into card face from number
* getNumFace - returns card face number (1-13)

Clubs (1-13)
Diamonds (14-26)
Hearts (27-39)
Spades (40-52)

'''

class Card:
    def __init__(self,*args):
        if len(args) == 1:
            if (args[0]<=0 or args[0]>52):
                print("Card must be between 1-52. Try again.")
                exit
            else:
                self.setSuit(args[0])
                self.setFace(args[0])

        else:
            print("Please enter 1 argument only.")

    def getCard(self):
        return "{} of {}".format(self.face,self.suit)
    
    def setSuit(self,num):
        if(num <= 13):
            self.suit = "Clubs"
        elif (num > 13 and num <= 26):
            self.suit = "Diamonds"
        elif (num > 26 and num <= 39):
            self.suit = "Hearts"
        else:
            self.suit = "Spades"

    def getSuit(self):
        return self.suit

    def setFace(self,card):
        if card <= 13:
            num = card-1
        elif (card > 13 and card <= 26):
            num = card-13
        elif (card > 26 and card <= 39):
            num = card-26
        else:
            num = card-39
        
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
