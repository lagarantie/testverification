class Cellule:
    '''structure d'une cellule de la liste chainée'''
    def __init__(self,valeur,suivant):
        self.val=valeur
        self.suiv=suivant

class Liste:
    '''
    structure d'une liste définie par sa cellule de tête
    '''
    def __init__(self):
        self.tete=None

    def taille(self):
        '''
        fonction qui retourne la taille de la liste
        L est la liste
        retourne un nombre entier
        '''
        if self.tete is None:
            return 0
        taille=1
        L=self.tete
        while (L.suiv is not None):
            taille+=1
            L=L.suiv
        return(taille)

    def inserer(self,e,i):
        '''
        fonction qui insère un élment dans une liste
        L la liste à compléter
        e est l'élément à insérer
        i est un entier qui correspond à la position de l'insertion de l'élément
        retourne la liste modifiée
        précondition : l'indice est compris entre 1 et la taille du tableau+1
        précondition : la liste n'est pas pleine
        '''
        if i<1:
            raise IndexError("Indice invalide")
        else:
            if i==1:
                cel=Cellule(e,self.tete)
                self.tete=cel
            else:
                L=self.tete
                for j in range(i-2):
                    if L==None:
                        raise IndexError("Indice invalide")
                    L=L.suiv
                suite=L.suiv
                cel=Cellule(e,suite)
                L.suiv=cel

    def afficher(self):
        if self.tete is not None:
            Liste._afficherR(self.tete)

    def _afficherR(L):
        if L.suiv is not None:
            print(L.val,end=" - ")
            Liste._afficherR(L.suiv)
        else:
            print(L.val)

    def rechercher(self,e):
        indice=1
        if self.tete is None:
            
            return None
        
        L=self.tete
        while (L.val!=e and L.suiv is not None):
            L=L.suiv
            indice+=1
        if(L.val==e):
            return indice
        else:
            return None
        


        '''
        fonction qui recherche un élément dans une liste
        L est la liste
        e est l'élément à recherché
        retourne le rang (indice) de l'élément e
        précondition : la liste ne comporte pas deux fois le même élément
        '''
       # A vous

    def supprimer(self,i):
        L=self.tete
        for j in range (i, self.taille()+1):
            print(j)
            if(j<self.taille()):
                L.val=L.suiv.val
                L=L.suiv
            else:
                L.val=None
            
            
        '''
        fonction qui supprime un élément de la liste situé au rang i
        L la liste à modifier
        i le rang de l'élément à supprimer
        retourne la liste modifiée
        précondition : l'indice est compris entre 1 et la taille du tableau
        '''
        # A vous

    def lire(self,i):

        L=self.tete
        
        for j in range(1, self.taille()+1):
            
            if(j==i):
                return L.val
            L=L.suiv

        return None

        '''
        Fonction qui lit l'élément de la liste L situé au rang i
        L la liste à lire
        i l'indice ou le rang où se situe l'élément
        retourne un élément e
        précondition : l'indice est compris entre 1 et la taille du tableau
        '''
        # A vous

    def modifier(self,e,i):

        L=self.tete
       
        for j in range(1, self.taille()+1):
            if(i==j):
                L.val=e
            L=L.suiv

       
        '''
        Fonction qui remplace une valeur de la liste situé à l'indice i par une élément e
        L est la liste à modifier
        i est l'indice où la valeur va être modifiée
        e est l'élément à mettre à la place
        retourne la liste modifiée
        précondition : l'indice est compris entre 1 et la taille du tableau
        '''
        # A vous

L=Liste()
L.inserer(12,1)
L.inserer(1,2)
L.inserer(2,3)
L.inserer(3,4)
L.inserer(5,5)
L.inserer(4,4)
L.inserer(7,7)
L.inserer(8,3)
L.afficher()


for ind in range(1,L.taille()+1):
    print(L.lire(ind),end="  ")
    assert(L.rechercher(L.lire(ind))==ind)
    print("OK")


L.modifier(13,1)
L.modifier(12,7)
L.modifier(11,5)
L.modifier(8,8)
L.afficher()
L.supprimer(1)
L.supprimer(3)
L.supprimer(L.taille())
L.afficher()
