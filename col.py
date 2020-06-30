from colorama import Fore

class Col():

	def __init__(self):
		pass

	def red(self, s):
		return (Fore.RED + s + Fore.WHITE)

	def blue(self, s):
		return (Fore.BLUE + s + Fore.WHITE)

	def green(self, s):
		return (Fore.GREEN + s + Fore.WHITE)

	def yellow(self, s):
		return (Fore.YELLOW + s + Fore.WHITE)

	def magenta(self, s):
		return (Fore.MAGENTA + s + Fore.WHITE)

	def cyan(self, s):
		return (Fore.CYAN + s + Fore.WHITE)
