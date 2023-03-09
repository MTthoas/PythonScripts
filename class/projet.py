class AB:
    
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = [racine]
        self.gauche = gauche
        self.droite = droite

    def set_racine(self, racine):
        self.racine = racine

    def set_gauche(self, gauche):
        self.gauche = gauche

    def set_droite(self, droite):
        self.droite = droite
    
    def get_racine(self):
        return self.racine
    
    def get_gauche(self):
        return self.gauche
    
    def get_droite(self):
        return self.droite
    
    def estVide(self):
        return self.racine == None
    
    def affichage(self):
        if self.gauche:
            self.gauche.affichage()
        print( self.racine),
        if self.droite:
            self.droite.affichage()
        
    def taille(self):
        var = 1
        if self.gauche is not None:
            var += self.gauche.taille()
        if self.droite is not None:
            var += self.droite.taille()
        return var

    def prefixe(self):
        if self.estVide():
            return []
        else:
            # Commence par la racine
            res = [self.racine]
            # Puis les sous-arbres gauche
            if self.gauche is not None:
                res += self.gauche.prefixe()
            # Puis les sous-arbres droit
            if self.droite is not None:
                res += self.droite.prefixe()
            return res
    
    def infixe(self):
        if self.estVide():
            return []
        else:
            res = []
            # Gauche
            if self.gauche is not None:
                res += self.gauche.infixe()
            # Racine
            res += [self.racine]
            # Droite
            if self.droite is not None:
                res += self.droite.infixe()
            return res

    def postfixe(self):
        if self.estVide():
            return []
        else:
            res = []
            # Gauche
            if self.gauche is not None:
                res += self.gauche.postfixe()
            # Droite
            if self.droite is not None:
                res += self.droite.postfixe()
            # Racine
            res += [self.racine]
            return res

    def hauteur(self):
        if self.estVide():
            return []
        else:
            res = 1
            if self.gauche is not None:
                res = self.gauche.hauteur()
            if self.droite is not None:
                res = self.droite.hauteur()
            res+=1
            return res
                
    def estAbr(self):
        var = self.infixe()

        for i in range(len(var)-1):
            if var[i] > var[i+1]:
                return False
        return True
    
    def estEquilibre(self):
        if self.estVide():
            return True
        else:
            if self.gauche is not None:
                if self.gauche.hauteur() > self.hauteur():
                    return False
            if self.droite is not None:
                if self.droite.hauteur() > self.hauteur():
                    return False
            return True


a1 = AB()
a2 = AB(5)
print("a1 est t-'il vide ? :" + str(a1.estVide()))   
print("a2 est t-'il vide ? :" + str(a2.estVide()))   

a3 = AB()
a3.set_racine(5)
a2.set_gauche(a3)

a5 = AB(5)
a5.set_droite(AB(8))
a5.set_gauche(AB(3))
Atest = AB(10, a5, AB(12))

Atest.affichage()

print("Atest est t-'il vide ? :" + str(Atest.estVide()))   
print("Atest taille : " + str(Atest.taille()))
print("Préfixe :" + str(Atest.prefixe()))
print("Infixe :" + str(Atest.infixe()))
print("Postfixe :" + str(Atest.postfixe()))
print("Hauteur :" + str(Atest.hauteur()))
print("Est t-'il un ABR ? :" + str(Atest.estAbr()))
print("Est t-'il équilibré ? :" + str(Atest.estEquilibre()))





