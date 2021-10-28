''' L'utilisateur est le devin '''
MIN, MAX = 1, 999    

def devin_utiliateur():

	# Choisir un nombre dans l'intervalle min et max
	choix = int(input("J'ai choisi ").strip())

	# Faire deviner un nombre à l'utilisateur
	nb_essai = 0   # Nombre d'essais faits par le joueur
	proposition = int()  # Propostion de l'utilisateur
 
	# Initialiser une boucle pour répéter proposition  
	while proposition != choix:
		# Saisir la proposition
		proposition = int(input("Votre proposition : ").strip())

		# Incrémenter le nombre d'essai
		nb_essai += 1

		# Analyser la proposition
		if proposition< choix:
			print("Trop petit")
		elif proposition > choix:
			print("Trop grand")
		else:
			print("Trouvé")

	# Indiquer le nombre d'essai(s) à l'utilisateur
	print("Félicitation, vous avez trouvé", proposition, "en", nb_essai, "essai(s)")
if __name__ == "__main__":
     devin_utiliateur()
     
     









# def devinette():
#     counter = 0
#     seer_choice= ""
#     master_choice = int(input("J'ai choisi "))
#     while master_choice != seer_choice:
#         seer_choice = int(input("Votre proposition : "))
#         counter += 1
    
#         if seer_choice > master_choice:
#             print("Trop grand")
#         elif seer_choice < master_choice:
#             print("Trop petit")
#         else:
#             print("Trouvé")
#     print("Felicitation, vous avez trouvé", master_choice, "en", counter, "essai(s)")
    
# devinette()
