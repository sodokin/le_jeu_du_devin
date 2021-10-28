''' Jouer au jeu du devin. '''
from random import randint


def devin_ordinateur():
    MIN = 1
    MAX = 999

    proposition = 500
    choix = " "
    nb_essais = 0
    indice = " "
    while choix != "o":
        # Demander à l'utilisateur de choisir un nombre
        choix = input("Avez-vous choisi un nombre entre 1 et 999 (o/n) ? ")
        if choix == "o":
            # Faire deviner le nombre à l'utilisateur
            print("Je propose", proposition)
            # Compter le nombre d'éssais
            nb_essais+=1
        else:
            print("J'attends...")
  
    # Analyser les réponses de l'utilisateur  
    while indice!= "t":
        # Saisir les indices
        indice = input("Votre indice (t, p, g) : ")
        
        if indice != "p":
            MIN = proposition + 1
            proposition = (proposition + MAX)//2
            # Faire deviner à nouveau si le nombre est trop petit
            print("Je propose",proposition)
            
            nb_essais+=1
            
        elif indice == "g":
            MAX = proposition - 1
            proposition = (MIN + proposition)//2
            # Faire deviner à nouveau si le nombre est trop grand
            print("Je propose", proposition)
            nb_essais+=1
            
        # indiquer à l'ordinateur s'il a trouvé le nombre 
        else:
            print("J'ai trouvé", proposition, "en", nb_essais, "essai(s)")
            
        # Indiquer à l'utilisateur s'il a triché  
        if (indice == "g" and proposition == 501) or (indice == "p" and proposition == 499):
            print("Vous avez triché !")
            break
        
if __name__ == "__main__":
    devin_ordinateur()