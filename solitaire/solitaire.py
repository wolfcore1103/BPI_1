#!/usr/bin/env python3


"""Jeu du solitaire."""


import subprocess
import sys
import plateau
import random
import copy 
import time
# moves available
# key is an empty space, or destination
# each key leads to a set of accessible move can be made.
# [destination, middle, start]
valid_move = {
    0 : [[3,1,0], [5,2,0]],
    1 : [[6,3,1], [8,4,1]],
    2 : [[7,4,2], [9,5,2]],
    3 : [[0,1,3], [5,4,3], [12,7,3], [10,6,3]],
    4 : [[11,7,4], [13,8,4]],
    5 : [[0,2,5], [3,4,5], [12,8,5], [14,9,5]],
    6 : [[1,3,6], [8,7,6]],
    7 : [[2,4,7], [9,8,7]],
    8 : [[1,4,8], [6,7,8]],
    9 : [[2,5,9], [7,8,9]],
    10 : [[3,6,10], [12,11,10]],
    11 : [[4,7,11], [13,12,11]],
    12 : [[10,11,12], [3,7,12], [5,8,12], [14,13,12]],
    13 : [[4,8,13], [11,12,13]],
    14 : [[5,9,14], [12,13,14]]
}
is_started = False
def calcule_solution(plat):
    """Renvoie la suite des coups à jouer **à l'envers** pour gagner.

    Renvoie la suite des coups à jouer sous la forme d'une list, ordonnée
    à l'envers. Par exemple, après exécution de la ligne :

    coups = calcule_solution(plat)

    on aura coups[0] qui contient le **dernier** coup à jouer pour gagner,
    coups[1] l'avant-dernier, ..., et coups[-1] le **premier** coup à jouer
    à partir de l'état actuel du plateau plat.

    Renvoie None si le plateau n'est pas gagnant et on a essayé (en vain)
      tous les coups possibles.
    """
    """
    A loop that create a copy of plat everytime, then it will calculate based on 
    the copied version 
    """
    while True:
        plat_copy = copy.deepcopy(plat)
        i = next_move(plat_copy, [12], [])
        if plateau.est_gagnant(plat_copy):
            plateau.affiche(plat_copy, False)
            return i
        plateau.affiche(plat_copy, False) #Decomment to see effect
        time.sleep(0.1)                   #Decomment to see effect

def next_move(plat: plateau, empty_cases: list, res):
    """Generate next move"""
    global is_started
    found = False
    move = None
    if plateau.est_gagnant(plat):
        return res
    else:
        # Create a copy of a list of empty cases,
        # Randomly pull out an element of it, then
        # randomly select a possible move towards that empty case
        # If verify condition, move is replace by the new found move
        # If not continue loop, if no possible move found, move is None
        l1 = empty_cases.copy()
        while l1:
            random_case = random_process(l1)
            l2 = valid_move[random_case].copy()
            while l2:
                random_move = random_process(l2)
                if plat.cases[random_move[0]] == plat.cases[random_move[1]] == 1 and plat.cases[random_move[2]] == 0:
                    move = random_move
                    found = True
                    break
            if found:
                break
        if not move:
            return res
        process_a_move(plat, move, empty_cases, res)
        return next_move(plat, empty_cases, res)

def random_process(l):
    """
    Take a list, retrieve a random element out of the list
    then remove that element from that list
    """
    res = l[random.randint(0, len(l)-1)]
    l.remove(res)
    return res
    

def process_a_move(plat, move, empty_cases, res):
    """
    When a possible move is founded, update values
    and modify the board
    """
    empty_cases.append(move[0])
    empty_cases.append(move[1])
    empty_cases.remove(move[2])
    plateau.joue_coup(plat,move)
    res.append(move)

def demande_coup(plat):
    """Demande quel coup jouer à l'utilisateur."""
    try:

        # Demande la case à jouer
        print("tapez ^C pour arrêter et lancer la résolution")
        depart = int(input("ou alors \n  donnez une case de départ: "))
        if plat.cases[depart] == plateau.VIDE:
            print("  case de départ invalide")
            raise ValueError

        # Demande la case d'arrivée
        arrivee = int(input("  donnez une case d'arrivée: "))
        if plat.cases[arrivee] == plateau.PION:
            print("  case d'arrivée invalide")
            raise ValueError

        # On vérifie que le mouvement est valide, c'est à dire
        # qu'il y a un pion entre le départ et l'arrivée.
        # Le FAMEUX "for else" de Python : c'est QUOi CE TRUC ??
        for direction, milieu in enumerate(plateau.VOISINS[depart]):
            if milieu is not None:
                apres_milieu = plateau.VOISINS[milieu][direction]
                if apres_milieu is not None and apres_milieu == arrivee:
                    break
        else:
            print("  mouvement invalide")
            raise ValueError
        # Nous (mais pas pylint) savons qu'ici milieu est défini
        # pylint: disable=undefined-loop-variable
        if plat.cases[milieu] == plateau.VIDE:
            print("  mouvement invalide")
            raise ValueError
        return depart, milieu, arrivee

    # Ici on fait suivre l'exception
    except KeyboardInterrupt:
        raise

    # Ici on redemande à l'utilisateur car il
    # a joué un coup invalide.
    # pylint, laisse nous tranquille, on gère !
    except:  # pylint: disable=bare-except
        return demande_coup(plat)


def main():
    """Lance une partie de solitaire."""

    # On determine si on est dans terminology ou non
    # pour savoir comment afficher le plateau :
    # SVG ou textuel ?
    try:
        subprocess.check_call(["tycat"])
        in_terminology = True
    except subprocess.CalledProcessError:  # Si le programme n'a pas renvoyé zéro
        in_terminology = False
    except FileNotFoundError:  # Si le programme n'est pas trouvé dans le PATH
        in_terminology = False

    # On joue tant que ^C n'est pas tapé ou qu'on a pas gagné
    plat = plateau.Plateau()
    while not plateau.est_gagnant(plat):
        plateau.affiche(plat, in_terminology)
        try:
            coup = demande_coup(plat)
        except KeyboardInterrupt:  # sur ^C
            break
        print(f"on joue de {coup[0]} a {coup[2]}")
        plateau.joue_coup(plat, coup)

    # Si le joueur humain a gagné, on s'arrête
    if plateau.est_gagnant(plat):
        print("Gagné !!!")
        sys.exit(0)

    # Sinon on demande la solution pour finir à notre
    # intelligence artificielle (fallait le placer ce
    # terme dans le cours BPI quand même !)
    suite = calcule_solution(plat)
    print()
    if suite:
        print("suite de coups possible pour terminer :")
        for debut, _, arrivee in reversed(suite):
            print("(", debut, ", ", arrivee, ")", sep="", end=" ")
        sys.exit(0)
    else:
        print("pas moyen d'aller plus loin !!!")
        sys.exit(1)


if __name__ == "__main__":
    main()