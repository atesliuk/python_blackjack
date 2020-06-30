from user import User

class Player(User):

	balance=0

	def __init__(self, balance):
		User.__init__(self)
		self.setBalance(balance)

	def setBalance(self, balance):
		self.balance=balance

	def getBalance(self):
		return self.balance

