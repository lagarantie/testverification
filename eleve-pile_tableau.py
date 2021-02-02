def creer_pile():
    '''
    La pile est gèrée à l'aide d'une liste python tab
    Renvoie une pile vide
    '''
    return []

def affiche_pile(P):

    for i in range (len(P)-1, -1, -1):
        print(P[i])

    print("\n")
    '''
    Affichage des éléments qui sont dans la pile
    '''
   # à vous

def est_vide(P):
    '''
    Fonction qui retourne True si la pile est vide, False sinon.
    '''
    if len(P)==0:
        return True
    return False

def empiler(P,elt):
    '''
    Fonction qui ajoute l'élément elt dans la pile
    '''
    P.append(elt)

def depiler(P):
    val=0
    if (len(P)>0):
        val=P[len(P)-1]
        P.pop(len(P)-1)

    else:
        print("impossible de dépiler une pile vide")
    
    return val
        

    '''
    Fonction qui renvoie le dernier élément entré dans la pile
    Cet élément est retiré de la pile.
    '''
    # à vous


def taille(P):

    return len(P)
    '''
    Fonction qui renvoie la taille de la pile
    '''
   # à vous


def consulter(P):

    return (P[len(P)-1])
    '''
    Fonction qui renvoie le dernier élément entré dans la pile sans le retirer de la pile
    '''
    # à vous


if __name__=="__main__":
    P=creer_pile()
    empiler(P,5)
    empiler(P,6)
    empiler(P,7)
    empiler(P,8)
    print(consulter(P))
    print("\n")
    affiche_pile(P)
    print(depiler(P))
    print(depiler(P))
    print(depiler(P))
    print(depiler(P))
