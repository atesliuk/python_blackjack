from random import shuffle

class Deck():

	def __init__(self):
		self.reset()

	def __str__(self):
		return (f"Current decks is {self.cards}")

	def reset(self):
		cards = []
		for i in [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']:
			for num in range(4):
				cards.append(i)
		shuffle(cards)
		self.cards = (cards)

	def nextCard(self):
		return self.cards.pop(0)
	