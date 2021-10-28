''' Définition d'un jeu du devin.'''

import random

MIN, MAX = 1, 999    # Limites du jeu du devin

def faire_deviner():
	'''Faire deviner un nombre choisi par la machine.'''

	# choisir un nombre
	choisi: int = random.randint(MIN, MAX)

	# faire deviner ce nombre à l'utilisateur
	abandon: bool = False      # Est-ce qeu le joueur a abandonné ?
	nb_essais: int = 0         # nombre d'essais faits par le joueur
	proposition: int = MIN - 1 # propostion du joueur
			# initialisée pour être sûr de passer dans le while (Répéter)
	while proposition != choisi:
		# Saisir la proposition de l'utilisateur
		proposition = int(input("Votre proposition : "))
		if proposition == 0:
			message: str = 'Voulez-vous vraiment abandonner (o/n) ? '
			reponse = input(message).lower()
			while reponse not in ('o', 'n'):
				print("Je n'ai pas compris...")
				reponse = input(message).lower()
			abandon = reponse == 'o'
			if abandon:
				break

		# incrémenter le nombre d'essai
		nb_essais += 1

		# Évaluer la proposition
		if proposition < choisi:
			print("trop petit")
		elif proposition > choisi:
			print("trop grand")
		else:
			print("trouvé")

	# féliciter le joueur
	if abandon:
		print('La partie a été abandonnée')
	else:
		print("Félicitation, vous avez trouvé", proposition, "en", nb_essais, "coup(s)")


def deviner():
	'''Deviner le nombre choisi par l'utilisateur.'''

	# Demander à l'utilisateur de choisir un nombre
	message = f'Avez-vous choisi un nombre entre {MIN} et {MAX} (o/n) ? '
	reponse = input(message)
	while reponse.strip().lower() != 'o':
		print("J'attends...")
		reponse = input(message)

	nb_essais: int = 0       # nombre de propositions faites
	inf, sup = MIN, MAX      # intervalle dans lequel le nombre se trouve
	propositions = []        # couples (proposition, indice)
	nombre_trouve: bool = False    # Est-ce que le nombre a été trouvé ?
	while not nombre_trouve and inf <= sup:
		# choisir un nombre
		proposition = (inf + sup) // 2

		# proposer ce nombre
		print("Je propose", proposition)

		# demander un indice à l'utilisateur
		ERREUR, TROP_PETIT, TROP_GRAND, TROUVE = range(4)
		indice: int = ERREUR    # indice donné par l'utilisateur
		while indice == ERREUR:
            # demander un indice
			reponse = input("Votre indice (t, p, g) : ").lower()

			# analyser l'indice
			if reponse in ('p', '<'):
				indice = TROP_PETIT
			elif reponse in ('g', '>'):
				indice = TROP_GRAND
			elif reponse in ('t', '='):
				indice = TROUVE
			elif reponse == '0':
				message: str = 'Voulez-vous vraiment abandonner (o/n) ? '
				reponse = input(message).lower()
				while reponse not in ('o', 'n'):
					print("Je n'ai pas compris...")
					reponse = input(message).lower()
				if reponse == 'o':
					print('La partie a été abandonnée')
					return
			else:
				print("Je n'ai pas compris...")
				indice = ERREUR

		nb_essais += 1

		# enregistrer la proposition et l'indice
		propositions.append((proposition, indice))

		# tenir compte de l'évaluation
		if indice == TROP_GRAND:
			sup = proposition - 1
		elif indice == TROP_PETIT:
			inf = proposition + 1
		else:  # indice == TROUVE
			inf = sup = proposition
			nombre_trouve = True

	# féliciter le joueur
	if nombre_trouve:
		print("J'ai trouvé", proposition, "en", nb_essais, "coup(s)")
	else:
		print('Vous avez triché !')
		# Comprendre où il y eu triche (ou erreur)
		#   Demander le nombre choisi
		nombre_a_trouver = int(input("Quel était votre nombre ? "))

		# Contrôler que le nombre était correct
		if not MIN <= nombre_a_trouver <= MAX:
			print(f'Le nombre DEVAIT ÊTRE entre {MIN} et {MAX} !')

		#   Valider les réponses faites au propositions
		nb_erreurs = 0
		for numero, (prop, indice) in enumerate(propositions, 1):
			if (prop > nombre_a_trouver and indice == TROP_GRAND) \
					or (prop < nombre_a_trouver and indice == TROP_PETIT):
				message = 'ok'
			else:
				message = 'ERREUR'
				nb_erreurs += 1
			indice_texte = ('', 'trop petit', 'trop grand', 'trouvé')[indice]
			print(f"{numero:2}: proposition ={prop:4}, indice = {indice_texte} : {message}")

		#   Afficher le nombre d'erreurs
		print("Vous m'avez donné", nb_erreurs, "indice(s) erroné(s)")


def main():
	'''Jouer au jeu du devin.'''

	termine = False
	while not termine:
		# afficher le menu
		print()
		print("1- L'ordinateur choisit un nombre et vous le devinez")
		print("2- Vous choisissez un nombre et l'ordinateur le devine")
		print('0- Quitter')

		# demander le choix
		choix = input('Votre choix : ').strip()

		# traiter le choix
		if choix == '1':
			faire_deviner()
		elif choix == '2':
			deviner()
		elif choix == '0':
			termine = True
		else:
			print("Je n'ai pas compris votre choix !")

if __name__ == "__main__":
	main()