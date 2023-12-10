#!/usr/bin/env python3
"""Implementation of the class Cellule"""

class Cellule:
    """Liste enchainee, class Cellule"""
    def __init__(self, val=None, suiv=None):
        self.val = None
        self.suiv = None

class CelluleDouble:
    """Cellule avec prec"""
    def __init__(self, val=None, prec=None, suiv=None):
        self.val = val
        self.prec = prec
        self.suiv = suiv

class ListeSimple:
    """Liste de Cellules"""
    def __init__(self):
        self.tete = Cellule("?", None)
 
class ListeDouble:
    """Liste de Cellule_double"""
    def __init__(self):
        self.tete = CelluleDouble("?", None, None)
        self.queue = CelluleDouble("?", self.tete, None)
        self.tete.suiv = self.queue

    def remplir(self, tab):
        """Remplir la liste avec les valeurs dans tab"""
        for i in tab:
            self.ajout_en_queue(i)
    
    def ajout_en_tete(self, val):
        """Ajout en tete"""
        i = self.tete.suiv
        new_cell = CelluleDouble(val, self.tete, i)
        self.tete.suiv = new_cell
        i.prec = new_cell

    def ajout_en_queue(self, val):
        """Ajout en queue"""
        i = self.queue.prec
        new_cell = CelluleDouble(val, i, self.queue)
        self.queue.prec = new_cell
        i.suiv = new_cell
    
    def inverse(self):
        # cour = self.tete.suiv
        # i = None
        # while cour.val != "?":
        #     i = cour.suiv
        #     echanger(cour)
        pass

def echanger(cell):
    """Echange cell et cell.suiv"""
    a = cell.prec
    b = cell.suiv
    suite = cell.suiv.suiv
    cell.suiv = suite
    cell.prec = b
    b.prec = a
    b.suiv = cell
    a.suiv = b
    suite.prec = cell
    
