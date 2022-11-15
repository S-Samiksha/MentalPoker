'''
Hand Class

Functions:
* setHand - sets hand of 5 cards
* getHand - gets hand of cards as a list
* getNumHand - gets hand in list with cards [suit,numFace]
* rankMeaning - defines rank
* rank - return rank
* bestCard - return best card
* bestSuit - return best suit
* bestSet - return best set if pair/triple/fourofakind
* isStraightFlush - return true if straight flush
* isStraight - return true if straight
* checkDupRanks - return true if pair/triple/fourofakind
* isFlush - return true if flush
* isTwoPair - return true if 2 pairs

'''
import Card
import operator as op

class Hand:
	def __init__(self,*args):
		if len(args) == 1:
			self.setHand(args[0])
		else:
			print("Please enter 1 argument only.")

	def setHand(self,hand):
		numHand = []
		newHand = []
		numNums = []
		for card in hand:
			numNums.append(int(card))
		self.numNums = numNums
		numNums.sort()
		for card in numNums:
			newCard = Card.Card(int(card))
			numCard = [newCard.getSuit(),newCard.getNumFace()]
			numHand.append(numCard)
			newHand.append(newCard.getCard())
		self.numHand = numHand
		self.hand = newHand
	
	def getHand(self):
		return self.hand

	def getNumHand(self):
		return self.numHand

	def rankMeaning(self):
		num = self.rank()
		if num == 9:
			return("Straight Flush")
		elif num == 8:
			return("Four of a kind")
		elif num == 7:
			return("Full house")
		elif num == 6:
			return("Flush")
		elif num == 5:
			return("Straight!")
		elif num == 4:
			return("Three of a kind!")
		elif num == 3:
			return("Two pairs!")
		elif num == 2:
			return("Pair!")
		else:
			return("No combo!")

	def rank(self):
		if self.isStraightFlush():
			return 9
		elif self.checkDupRanks(4):
			return 8
		elif self.checkDupRanks(3) and self.checkDupRanks(2):
			return 7
		elif self.isFlush():
			return 6
		elif self.isStraight():
			return 5
		elif self.checkDupRanks(3):
			return 4
		elif self.isTwoPair():
			return 3
		elif self.checkDupRanks(2):
			return 2
		else:
			return 1

	def bestCard(self):
		i = self.numNums.index(max(self.numNums))
		return self.hand[i]

	def bestSuit(self):
		suit = self.numHand[4][0]
		if suit == "Clubs":
			return 1
		elif suit == "Diamonds":
			return 2
		elif suit == "Hearts":
			return 3
		elif suit == "Spades":
			return 4
		return self.numHand[4][0]
	
	def bestSet(self,count):
		faces = []
		bestCard = -1
		for card in self.numHand:
			faces.append(card[1])
		for card in self.numHand:
			if op.countOf(faces,card[1]) == count:
				if card[1] > bestCard:
					bestCard = card[1]
		return bestCard
	
	def isStraightFlush(self):
		if self.isStraight() and self.isFlush():
			return True
		else:
			return False

	def isStraight(self):
		faces = []
		for card in self.numHand:
			faces.append(card[1])
		minFace = min(faces)
		maxFace = max(faces)
		if (minFace + 4 == maxFace) and self.checkDupRanks(2) == False:
			return True
		else:
			return False

	def checkDupRanks(self,num):
		faces = []
		for card in self.numHand:
			faces.append(card[1])
		for card in self.numHand:
			if op.countOf(faces,card[1]) == num:
				return True
		return False

	def isFlush(self):
		suit = self.numHand[0][0]
		for card in self.numHand:
			if card[0] != suit:
				return False
		return True

	def isTwoPair(self):
		hand = self.numHand
		firstCard = -1
		count = 0
		for card in hand:
			if op.countOf(hand,card[1]) == 2 and card != firstCard:
				firstCard = card
				count += 1
		if count == 2:
			return True
		return False
				
		 
