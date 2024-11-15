
import pygame
import random
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


#  tirer un aliment aléatoire , on prend 1 des 3 food au hasard 
def get_random_food():
    food_classes = [ChickenLeg, WholeChicken, Fries]
    selected_food_class = random.choice(food_classes)  # Tirer aléatoirement une classe
    return selected_food_class(20, 100)  # Initialiser l'aliment avec X=20 et Y=100




# Initialisation de la première food en main  et du timer
random_food = get_random_food()
last_time = pygame.time.get_ticks()  # Temps de la dernière mise à jour
last_push_time = 0  # Temps de la dernière activation du push
current_food = get_random_food()

# Boucle principale
running = True
while running:
    current_time = pygame.time.get_ticks()  # Temps actuel en millisecondes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion du clic pour activer le push
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            if current_time - last_push_time >= 3000:  # Limite à 1 clic toutes les 3 secondes
                current_food.is_pushed = True
                last_push_time = current_time

    # Changer de nourriture toutes les 3 secondes (3000 ms)
    if current_time - last_time >= 3000:
        random_food = get_random_food()  # Tirer un nouvel aliment
        last_time = current_time  # Réinitialiser le timer

    random_food.food_push()
    
    # Déplacer le bodybuilder avec rebond
    bodybuilder.move_and_bounce(screen_width=900, screen_height=600)

    # Mettre à jour la position verticale de l'aliment avec la souris
    random_food.place_on_y_with_mouse()

    # Dessiner l'écran et le bodybuilder
    screen.fill((0, 0, 0))  # Effacer l'écran
    screen.blit(background, (0, 0))  # Afficher le fond
    bodybuilder.draw(screen)
    random_food.draw(screen)  # Afficher l'aliment



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

