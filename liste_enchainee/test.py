#!/usr/bin/env python3
"""Test functions for all class"""

from random import randint
from cellules import *

def test_ListeDouble():
    """test functions for liste double"""
    test = 2
    def test_1():
        """test for ajout_en_tete()"""
        liste = ListeDouble()
        liste.ajout_en_tete(3)
        liste.ajout_en_tete(5)
        assert liste.tete.suiv.val == 5, f'5 expected, got {liste.tete.suiv.val}'
        assert liste.tete.suiv.suiv.val == 3, f'3 expected, got {liste.tete.suiv.suiv.val}'
        print("Test function ajout_en_tete() : passed\n")

    def test_2():
        """test for ajout_en_queue()"""
        liste = ListeDouble()
        liste.ajout_en_queue(3)
        liste.ajout_en_queue(5)
        assert liste.tete.suiv.val == 3, f'5 expected, got {liste.tete.suiv.val}'
        assert liste.tete.suiv.suiv.val == 5, f'3 expected, got {liste.tete.suiv.suiv.val}'
        print("Test function ajout_en_queue() : passed\n")
    
    def test_3():
        """test for remplir()"""
        print("Function remplir() :")
        liste = ListeDouble()
        tab = [randint(0,9) for _ in range(5)]
        liste.remplir(tab)
        cour = liste.tete.suiv
        for i in tab:
            print(f"Expected {i}, got {cour.val}")
            assert i == cour.val, f"Error ! {i} expected, got {cour.val}"
            cour = cour.suiv
        print("Test passed !\n")
    
    def test_4():
        """test for echange()"""
        print("Test for echange() : ")
        liste = ListeDouble()
        liste.ajout_en_queue(1)
        liste.ajout_en_queue(2)
        echanger(liste.tete.suiv)
        assert liste.tete.suiv.val == 2, f"Error ! 2 expected, got {liste.tete.suiv.val}"
        assert liste.tete.val == liste.queue.val == "?", "Error, head or tail changed !"
        print("Test passed !\n")
        
    def test_5():
        """test for inverse"""
        liste = ListeDouble()
        liste.ajout_en_queue(1)
        liste.ajout_en_queue(2)
        print(liste.tete.val)
        print(liste.tete.suiv.val)
        print(liste.tete.suiv.suiv.val)
        
    test_1()
    test_2()
    test_3()    
    test_4()   
test_ListeDouble()
    
        
    