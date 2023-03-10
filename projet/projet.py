from classAlgo import *

a1 = AB()
a2 = AB(5)

a3 = AB()
a3.set_racine(5)
a2.set_gauche(a3)

# Initialisation de l'arbre
a5 = AB(5)
a5.set_droite(AB(8))
a5.set_gauche(AB(3))
Atest = AB(10, a5, AB(12))

# Affichage de l'arbre en console
Atest.affichage()

print("Atest est t-'il vide ? :" + str(Atest.estVide()))   
print("Atest taille : " + str(Atest.taille()))
print("Préfixe :" + str(Atest.prefixe()))
print("Infixe :" + str(Atest.infixe()))
print("Postfixe :" + str(Atest.postfixe()))
print("Hauteur :" + str(Atest.hauteur()))
print("Est t-'il un ABR ? :" + str(Atest.estAbr()))
print("Est t-'il équilibré ? :" + str(Atest.estEquilibre()))

# Partie 2 avec affichage
tree = BinaryTree(Atest)
tree.run()





