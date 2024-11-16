import pygame


class Food: #classe MAMAN
    """
    Classe de base pour représenter un aliment avec les points qu'il apporte.
    """
    def __init__(self, image_path, x, y, size=(50, 50), points=0):
        """
        Initialise un aliment.

        Args:
            image_path (str): Chemin de l'image de l'aliment.
            x (int): Position initiale sur l'axe X.
            y (int): Position initiale sur l'axe Y.
            size (tuple): Taille de l'image (largeur, hauteur).
            points (int): Points associés à cet aliment (positif ou négatif).
        """
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.x = x
        self.y = y
        self.points = points  # Points associés à l'aliment
        self.is_pushed = False # true si lancée
    def draw(self, screen):
        """
        Affiche l'aliment sur l'écran.
        
        Args:
            screen (Surface): Surface Pygame où dessiner l'aliment.
        """
        screen.blit(self.image, (self.x, self.y))

    def get_points(self):
        """
        Retourne les points associés à cet aliment.

        Returns:
            int: Points de l'aliment.
        """
        return self.points

    def place_on_y_with_mouse(self):
            """
            Met à jour la position sur l'axe Y en fonction de la position de la souris,
            tout en maintenant l'axe X fixe à 20.
            """
            _, mouse_y = pygame.mouse.get_pos()  # Obtenir la position de la souris
            self.x = 20  # Fixer l'axe X
            self.y = mouse_y  # Positionner l'aliment en fonction de la souris

            # faire push l'aliment sur x




    def food_push(self):


        #if self.is_pushed:  # Si l'aliment est en mouvement
        self.x += 20  # Augmente rapidement la position X pour un déplacement fluide

        """
        Fait avancer l'aliment le long de l'axe X.
        Returns:
            bool: True si l'aliment traverse l'écran, sinon False.
        
        if self.is_pushed:  # Si l'aliment est en mouvement
            self.x += 10  # Augmente la position X pour le faire avancer
            if self.x > 900:  # Si l'aliment sort de l'écran
                self.is_pushed = False  # Arrêter le mouvement
                self.x = 200  # Réinitialiser la position pour un nouvel aliment
                return True  # L'aliment a traversé l'écran
        return False
        """

    #fonction pour collision 
    def get_rect(self):
            """
            on choppe le rectangle de la nourriture
            """
            return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

# SOUS CLASSE DE FOOD 
class ChickenLeg(Food):
    """
    Classe pour une cuisse de poulet (1 point).
    """
    def __init__(self, x, y):
        super().__init__(r"C:\Users\Léo\OnedriveLeo\OneDrive\Esilv A4 CreaTek\CS_octobre\Jeux-proteine\asset\cuisse-de-poulet.png", x, y, size=(40, 40), points=1)


class WholeChicken(Food):
    """
    Classe pour un poulet entier (2 points).
    """
    def __init__(self, x, y):
        super().__init__(r"C:\Users\Léo\OnedriveLeo\OneDrive\Esilv A4 CreaTek\CS_octobre\Jeux-proteine\asset\poulet (1).png", x, y, size=(60, 60), points=2)


class Fries(Food):
    """
    Classe pour des frites (-2 points).
    """
    def __init__(self, x, y):
        super().__init__(r"C:\Users\Léo\OnedriveLeo\OneDrive\Esilv A4 CreaTek\CS_octobre\Jeux-proteine\asset\patates-frites.png", x, y, size=(50, 50), points=-2)
