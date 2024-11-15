
import pygame
import ctypes
from functions import move_and_bounce
from food import *
from personnage import Bodybuilder

# Connaitre la taille de l'écran - juste pour moi 
usr32 = ctypes.windll.user32
print("width =", usr32.GetSystemMetrics(0))
print("height =", usr32.GetSystemMetrics(1))
###########################################################################
###########################################################################

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Protein Game...") # renome la fenetre de jeu
logo = pygame.image.load(r"C:\Users\Léo\OnedriveLeo\OneDrive\Esilv A4 CreaTek\CS_octobre\Jeux-proteine\asset\poulet1-removebg-preview.png")
pygame.display.set_icon(logo)#set icone fenetre 


#Player: créer un bodybuiler 
bodybuilder = Bodybuilder("asset/bodybuilder.png", x=100, y=100)

# chargement image
#bodybuilder = pygame.image.load(r"asset\bodybuilder.png")
#bodybuilder2  = pygame.transform.scale_by(bodybuilder,2) # x2 sur la taille de l'image 

""" TEST
#position initial de l'image
playerX = 200
playerY = 450
#vitesse initial 
speedX = 5
speedY = 5
"""

#chargement background 
background = pygame.image.load(r"C:\Users\Léo\OnedriveLeo\OneDrive\Esilv A4 CreaTek\CS_octobre\Jeux-proteine\asset\wallpaper_2monochrome.jpg")


# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacer le bodybuilder avec rebond
    bodybuilder.move_and_bounce(screen_width=900, screen_height=600)

    # Dessiner l'écran et le bodybuilder
    screen.fill((0, 0, 0))  # Effacer l'écran
    screen.blit(background, (0, 0))  # Afficher le fond
    bodybuilder.draw(screen)


    #  Affichaf*ger les points
    font = pygame.font.Font(None, 36)
    points_text = font.render(f"Points: {bodybuilder.points}", True, (255, 0, 0))
    screen.blit(points_text, (10, 10))

    # Timer en haut à droite ( toute les 3sec nouveau projectie )
    elapsed_time = pygame.time.get_ticks() // 1000  # Convertir en secondes
    timer_text = font.render(f"Time: {elapsed_time}s", True, (255, 0, 255))  # Bleu
    screen.blit(timer_text, (screen.get_width() - 150, 10))  # Position en haut à droite


    #MAJ de l'affichage 
    pygame.display.flip()  # Rafraîchir l'affichage
    clock.tick(60)  # Limiter le FPS à 60

   
pygame.quit()

