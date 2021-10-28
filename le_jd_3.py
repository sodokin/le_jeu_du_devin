'''Le jeu du devin.'''

from le_jd_1 import devin_utiliateur
from le_jd_2 import devin_ordinateur


def devinette():

	quitter = False
	while not quitter:
		# Proposer les trois options
		print()
		print("1- L'ordinateur choisit un nombre et vous le devinez")
		print("2- Vous choisissez un nombre et l'ordinateur le devine")
		print('0- Quitter')

		# Faire choisir une option
		option = input('Votre choix : ').strip()

		# traiter le choix 
		if option == '1':
			devin_utiliateur()
		elif option== '2':
			devin_ordinateur()
		elif option == '0':
			quitter = True
		else:
			print("Je n'ai pas compris votre choix !")

if __name__ == "__main__":
	devinette()