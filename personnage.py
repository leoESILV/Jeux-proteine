import pygame

class Bodybuilder:
    """
    Classe Bodybuilder, représentant le joueur.
    """

    def __init__(self, image_path, x, y, size=(100, 100)):
        """
        Initialise un bodybuilder avec une image, une position et des statistiques.
        """
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.x = x
        self.y = y
        self.points = 0
        self.wins = 0
        self.speedX = 5
        self.speedY = 5

    def draw(self, screen):
        """
        Dessine le bodybuilder sur l'écran.
        """
        screen.blit(self.image, (self.x, self.y))

    def update_points(self, value):
        """
        Met à jour les points du joueur.
        """
        self.points += value

    def increment_wins(self):
        """
        Incrémente le nombre de parties gagnées.
        """
        self.wins += 1

    def reset(self):
        """
        Réinitialise les statistiques.
        """
        self.points = 0
        self.x = 100
        self.y = 100

    def get_width(self):
        """
        Retourne la largeur de l'image.
        """
        return self.image.get_width()

    def get_height(self):
        """
        Retourne la hauteur de l'image.
        """
        return self.image.get_height()

    def move_and_bounce(self, screen_width, screen_height):
        """
        Met à jour la position et gère les rebonds avec les bords de la fenêtre.
        """
        self.x += self.speedX
        self.y += self.speedY

        if self.x <= 0 or self.x + self.get_width() >= screen_width:
            self.speedX = -self.speedX
        if self.y <= 0 or self.y + self.get_height() >= screen_height:
            self.speedY = -self.speedY

    def protein_total(self, value):
        """
        Met à jour le total des points de protéines en ajoutant ou soustrayant une valeur.

        Args:
            value (int): Points à ajouter (positif ou négatif).
        """
        self.points += value