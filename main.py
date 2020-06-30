from deck import Deck
from col import Col
from player import Player
from dealer import Dealer
import os

col = Col()
deck = Deck()
player = Player(100)
dealer = Dealer()




#This function resets global variables
def resetVariables():
	global deck, player, dealer
	deck.reset()
	player.reset()
	dealer.reset()

def arrayToString(ar):
	st=''
	for s in ar:
		st+='   '+str(s)
	return st

def printCards(show):
	if show:
		print (col.green("Dealer's cards: \t")+col.red(f"{arrayToString(dealer.getCards())}\t")+col.green("Total: "+col.red(str(dealer.getPoints()))))		
	else:
		print (col.green("Dealer's cards: \t")+col.red(f"{dealer.getCards()[0]}   X"))
	print (col.green("Your cards: \t\t")+col.red(f"{arrayToString(player.getCards())}\t")+col.green("Total: "+col.red(str(player.getPoints()))+'\n'))

def printBalance():
	print(col.green("Your balance:\t")+col.red(str(player.getBalance()))+"\n")






#Game itself
while True:
	os.system('cls')
	print(col.green("Start a new game? Your abalance is " + col.red(str(player.getBalance())))+'\n')
	startGame = input("Press any key to play BlackJack\t\t\t\t Type 'q' to quit the game\n")
	if startGame=='q':
		os.system('cls')
		print(col.green("Thanks for the game! See you soon!"))
		break

	resetVariables()
	os.system('cls')
	bet=0
	while True:		
		printBalance()
		try:
			bet = int(input(col.yellow('Place your bet: ')))
			if(bet>player.getBalance()):
				os.system('cls')
				print(col.red("You do not have enough balance!\n"))
			elif bet<=0:
				os.system('cls')
				print(col.red("You can't make 0 or negative bets!\n"))
			else:
				break
		except:
			os.system('cls')
			print(col.red("Input a number!\n"))		
		
	os.system('cls')


	dealer.addCards(deck.nextCard())
	dealer.addCards(deck.nextCard())

	player.addCards(deck.nextCard())
	player.addCards(deck.nextCard())

	printCards(False)
	
	if dealer.getPoints()==21 and player.getPoints()==21:
		os.system('cls')
		printCards(True)
		print(col.green("Draw! You both have a BlackJack!\n"))
		input('Press any key to continue ')
		continue
	elif dealer.getPoints()==21:
		os.system('cls')
		printCards(True)
		print(col.green("Dealer has a BlackJack...\n"))
		player.setBalance(player.getBalance()-bet)
		printBalance()
		input('Press any key to continue ')
		continue
	elif player.getPoints()==21:
		os.system('cls')
		printCards(True)
		print(col.green("You have a BlackJack!!!\n"))
		player.setBalance(player.getBalance()+bet)
		printBalance()
		input('Press any key to continue ')
		continue

	
	#Player can Hit or Stay
	hitStay=''
	bust=False
	while hitStay!='s' and bust==False:
		hitStay=''
		while hitStay!='h' and hitStay!='s':
			os.system('cls')
			printCards(False)
			hitStay = input(col.yellow("Type 'H' to hit\tType 'S' to stay   ")).lower()
		
		if hitStay=='h':
			player.addCards(deck.nextCard())
			if player.getPoints()>21:
				bust=True
				

	if bust:
		os.system('cls')
		printCards(True)
		print(col.red("BUST! Unfortunatelly, you lost this game...\n"))
		player.setBalance(player.getBalance()-bet)
		printBalance()
		input("Press any key to continue ")
		continue

	dealerBust=False
	#Dealer's actions - if he has 17 or more, he stays. If less, he hits
	while dealer.getPoints()<17 and dealerBust==False:
		dealer.addCards(deck.nextCard())
		if dealer.getPoints()>21:
			dealerBust=True

	if dealerBust:
		os.system('cls')
		printCards(True)
		print(col.green("Dealer went BUST! Congratulations, you won this game!\n"))
		player.setBalance(player.getBalance()+bet)
		printBalance()
		input("Press any key to continue ")
		continue

	#Noone bust
	os.system('cls')
	printCards(True)
	if dealer.getPoints()>player.getPoints():
		print(col.red("Unfortunatelly, you lost this game! Dealer have more points.\n"))
		player.setBalance(player.getBalance()-bet)
		printBalance()
		input("Press any key to continue ")

	elif dealer.getPoints()==player.getPoints():
		print(col.green(f"Draw! You both have {player.getPoints()} points!\n"))
		printBalance()
		input("Press any key to continue ")

	else:
		print(col.green("Congratulations, you won this game!\n"))
		player.setBalance(player.getBalance()+bet)
		printBalance()
		input("Press any key to continue ")

	




		