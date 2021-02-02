class Cellule:
    '''
    Une cellule de la liste chainée
    '''
    def __init__(self,valeur,suivant):
        self.val=valeur
        self.suiv=suivant

class Pile:
    '''
    Class Pile qui gère une structure de Pile
    '''
    def __init__(self):
        '''
        Constructeur de la Pile
        La pile est géré à l'aide d'une liste chainée de Cellules
        Création d'une pile vide
        '''
        self.length=0
        self.sommet=None


    def __str__(self):
        '''
        Affichage des éléments qui sont dans la pile
        '''
        retour=""
        C=self.sommet
        if C is None:
            return retour
        while C.suiv !=None:
            retour+=str(C.val)+" - "
            C=C.suiv
        retour+=str(C.val)
        return retour

    def est_vide(self):
        '''
        Fonction qui retourne True si la pile est vide, False sinon.
        '''
        return self.sommet is None

    def empiler(self,elt):
        '''
        Fonction qui ajoute l'élément elt dans la pile
        '''
        self.sommet=Cellule(elt, self.sommet)
        self.length+=1

    def depiler(self):
        '''
        Fonction qui renvoie le dernier élément entré dans la pile
        Cet élément est retiré de la pile.
        '''
        if (self.length)>0:
            valeur_retour=self.sommet.val
            self.sommet=self.sommet.suiv
            self.length-=1
            return valeur_retour
        else:
            print("La pile est vide")
        

    def taille(self):
        return self.length
       



    def consulter(self):
        '''
        Fonction qui renvoie le dernier élément entré dans la pile sans le retirer de la pile
        '''
        if(self.length>0):
            return self.sommet.val
        else:
            return None


def creer_Pile():
    return Pile()

if __name__=="__main__":
    P=creer_Pile()
    P.empiler(5)
    P.empiler(6)
    P.empiler(7)
    P.empiler(8)
    print(P.consulter())
    print(P)
    print("taille de la pile : ",P.taille())
    print(P.depiler())
    print(P.depiler())
    print(P.depiler())
    print(P.depiler())
    print(P.consulter())
    print("taille de la pile :",P.taille())
