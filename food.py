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
        super().__init__(r"C:\Users\Léo\OnedriveLeo\OneDrive\Esilv A4 CreaTek\CS_octobre\Jeux-proteine\asset\cuisse-de-poulet.png", x, y, size=(50, 50), points=-2)
