''' L'ordinateur est le devin '''
from random import randint


def devinette():
    MIN = 1
    MAX = 999

    proposition = 500
    choix = " "
    nb_essais = 0
    liste_indice = ["t", "p", "g"]
    while choix != "o":
        choix = input("Avez-vous choisi un nombre entre 1 et 999 (o/n) ? ")
        if choix == "o":
            print("Je propose", proposition)
            nb_essais+=1
        else:
            print("J'attends...")
  
    indice = " "  
    while indice!= liste_indice[0]:
        indice = input("Votre indice (t, p, g) : ")
        if indice == liste_indice[1]:
            MIN = proposition +1
            proposition = (proposition + MAX)//2
            print("Je propose",proposition)
            
            nb_essais+=1
            
        elif indice == liste_indice[2]:
            MAX = proposition -1
            proposition = (MIN + proposition)//2
            print("Je propose", proposition)
            nb_essais+=1
            
        else:
            print("J'ai trouvé", proposition, "en", nb_essais, "essai(s)")
        if (indice == "g" and proposition == 501) or (indice == "p" and proposition == 499):
            print("Vous avez triché !")
            break

        


devinette()