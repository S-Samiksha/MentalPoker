'''
Winner Class

Functions:
* getWinner - return winner
* sameRank - find winner if both have same rank

'''
import Hand

class Winner:
    def __init__(self,*args):
        if len(args) != 2:
            print("Please enter 2 arguments!")
        else:
            self.alice = Hand.Hand(args[0])
            self.bob = Hand.Hand(args[1])


    def getWinner(self):
        print("Alice has {}".format(self.alice.rankMeaning()))
        print("Bob has {}".format(self.bob.rankMeaning()))
        print()
        if self.alice.rank() > self.bob.rank():
            return 1
        elif self.alice.rank() == self.bob.rank():
            print("Comparing...")
            return self.sameRank()
        else:
            return 2

    def sameRank(self):
        if self.alice.rank() == 1 or self.alice.rank() == 9:
            if self.alice.bestCard() > self.bob.bestCard():
                return 1
            else:
                return 2
    
        elif self.alice.rank() == 2 or self.alice.rank() == 3:
            if self.alice.bestSet(2) > self.bob.bestSet(2):
                return 1
            else:
                return 2

        elif self.alice.rank() == 4 or self.alice.rank() == 7:
            if self.alice.bestSet(3) > self.bob.bestSet(3):
                return 1
            else:
                return 2

        elif self.alice.rank() == 8:
            if self.alice.bestSet(4) > self.bob.bestSet(4):
                return 1
            else:
                return 2

        elif self.alice.rank() == 6 or self.alice.rank() == 5:
            if self.alice.bestSuit() > self.bob.bestSuit():
                return 1
            elif self.alice.bestSuit() == self.bob.bestSuit():
                if self.alice.bestCard() > self.bob.bestCard():
                    return 1
                else:
                    return 2 
            else:
                return 2