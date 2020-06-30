from user import User

class Dealer(User):

	def __init__(self):
		User.__init__(self)

	#Dealer will continue to hit untin his points go 17 or above
	def dealersDecision(self):
		if self.getPoints()<=17:
			return 1 #means hit
		else:
			return 0 #means stay