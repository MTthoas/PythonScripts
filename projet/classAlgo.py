import pygame

class AB:
    
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = [racine]
        self.gauche = gauche
        self.droite = droite

    # Setters et Getters
   
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
            return -1
        else:
            res = 0
            if self.gauche is not None:
                res = self.gauche.hauteur()
            if self.droite is not None:
                res = self.droite.hauteur()
            res+=1
            return res
                
    def estAbr(self):
        var = self.infixe()

        # On vérifie que la liste est triée dans l'ordre croissant
        for i in range(len(var)-1):
            if var[i] > var[i+1]:
                return False
        return True
    
    def estEquilibre(self):
        if self.estVide():
            return True
        else:
            # On vérifie que la hauteur des sous-arbres est inférieure à la hauteur de l'arbre
            if self.gauche is not None:
                if self.gauche.hauteur() > self.hauteur():
                    return False
            if self.droite is not None:
                if self.droite.hauteur() > self.hauteur():
                    return False
            return True

# Noeud intermédiaire créer pour l'interface graphique  
class Node:
    def __init__(self, value):
        self.value = [value]
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def run(self):

        # Initialisation de pygame
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Arbre binaire - Pecquery Matthias")
        background_color = (255, 255, 255)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(background_color)
            self.draw_tree(screen, self.root, 400, 50, 200)
            self.draw_add_button(screen)
            pygame.display.flip()

        pygame.quit()

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        # Permet de se balader à gauche 
        if value < node.get_racine()[0]:
            if node.gauche is None:
                node.gauche = AB(value)
                print("Valeur insérée avec succès.")
                print("Ré-appuyez sur le bouton pour insérer une nouvelle valeur.\n")
            else:
                self._insert(value, node.gauche)
        # Permet de se balader à droite
        elif value > node.get_racine()[0]:
            if node.droite is None:
                node.droite = AB(value)
                print("Valeur insérée avec succès.")
                print("Ré-appuyez sur le bouton pour insérer une nouvelle valeur.\n")
            else:
                self._insert(value, node.droite)
        else:
            print("La valeur est déjà présente dans l'arbre.")
            print("Ré-appuyez sur le bouton pour insérer une nouvelle valeur.\n")
            

    def draw_tree(self, screen, node, x, y, spacing):

        if node is not None:
            font = pygame.font.Font(None, 30)
            # Affichage du noeud avec la valeur de la racine
            text = font.render(str(node.get_racine()[0]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x, y))
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 30)
            screen.blit(text, text_rect)

            # Affichage des fils en fonction de la position du noeud
            left_x = x - spacing
            right_x = x + spacing
            y_offset = 100

            if node.gauche is not None:
                # Espace de 30 pixels entre les noeudsn puis lisaisons entre les noeuds de la précendente taille du noeud, puis 4 pixels de largeur
                pygame.draw.line(screen, (0, 0, 0), (x, y + 30), (left_x, y + y_offset), 4)
                self.draw_tree(screen, node.gauche, left_x, y + y_offset, spacing//2)

            if node.droite is not None:
                pygame.draw.line(screen, (0, 0, 0), (x, y + 30), (right_x, y + y_offset), 4)
                self.draw_tree(screen, node.droite, right_x, y + y_offset, spacing//2)


    def draw_add_button(self, screen):

        font = pygame.font.Font(None, 30)
        text = font.render("Ajouter", True, (0, 0, 0))
        text_rect = text.get_rect()
        button_rect = pygame.Rect(630, 420, 80, 20)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
        screen.blit(text, button_rect)

        # Ajouter un événement pour ajouter un nouveau noeud lorsqu'on clique sur le bouton

        # Une boucle pour vérifier si l'événement est un clic de souris..
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    # Ouvrir une fenêtre de saisie pour ajouter un nouveau noeud
                    value_str = input("\nEntrez la valeur du nouveau noeud : ")
                    try:
                        value = int(value_str)
                        self.insert(value)
                    except ValueError:
                        print("La valeur doit être un entier")
                        print("Ré-appuyez sur le bouton pour insérer une nouvelle valeur.\n")
