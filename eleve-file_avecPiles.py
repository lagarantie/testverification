import sys
sys.path.insert(1, 'D:/travail/devoir carla/piles et listes')

from eleve_pile_liste_c import *

class File:
    '''
    Class File qui gère une structure de File
    '''
    def __init__(self):
        '''
        Constructeur de la File
        La File est gérée par deux piles
        Création d'une file vide
        '''
        self._pileEntree=Pile()
        self._pileSortie=Pile()

    

    def __str__(self):
        '''
        Affichage des éléments qui sont dans la file
        '''
        retour=""
        while not self._pileEntree.est_vide():
            self._pileSortie.empiler(self._pileEntree.depiler())
        while not self._pileSortie.est_vide():
            e=self._pileSortie.depiler()
            retour+=str(e)+" - "
            self._pileEntree.empiler(e)
        return retour

    def est_vide(self):
        return self._pileSortie.est_vide()
       

    def enfiler(self,elt):
        #self._pileSortie.empiler(elt)
        while not self._pileSortie.est_vide():
            self._pileEntree.empiler(self._pileSortie.depiler())
        
        self._pileSortie.empiler(elt)

        while not self._pileEntree.est_vide():
            self._pileSortie.empiler(self._pileEntree.depiler())
    

        

    def defiler(self):
        '''
        Fonction qui renvoie le premier élément entré dans la file
        Cet élément est retiré de la file.
        '''

        """
        if not self._pileSortie.est_vide():
            self._pileSortie.depiler()
        else:
            print("on ne peut pas défiler une file vide")
        """
    
        
        if self._pileSortie.est_vide():
            while not self._pileEntree.est_vide():
                self._pileSortie.empiler(self._pileEntree.depiler())
        if self._pileSortie.est_vide():
            raise IndexError("Impossible de défiler sur une file vide")
        return(self._pileSortie.depiler())

        

    def taille(self):
        '''
        Fonction qui renvoie la taille de la file
        '''
       
        return self._pileEntree.taille()+self._pileSortie.taille()

    def consulter(self):
        return self._pileSortie.consulter()
       # A vous

F=File()
F.enfiler(5)
F.enfiler(6)
F.enfiler(7)
F.enfiler(8)
print(F.est_vide())
print(F.consulter())
print(F)
print("Taille : ",F.taille())
print(F.defiler())
print(F.defiler())
print(F.defiler())
print(F.defiler())
if F.est_vide():
    print("File vide")
else:
    print(F)
print("Taille : ",F.taille())


