class User():

	def __init__(self):
		self.cards=[]

	def addCards(self, cards):
		self.cards.append(cards)

	def getCards(self):
		return self.cards

	#Calculates BlackJack points
	def getPoints(self):
		totalPoints=0
		for s in self.cards:
			try:
				totalPoints+=int(s)
			except:
				if s=='J' or s=='Q' or s=='K':
					totalPoints+=10
				else:
					if totalPoints+11 <= 21:
						totalPoints += 11
					else:
						totalPoints+=1
		return totalPoints

	#Reset all variables
	def reset(self):
		self.cards=[]

	def __str__(self):
		return (f"Cards of the user: {self.cards}\t points: {self.getPoints()}")
