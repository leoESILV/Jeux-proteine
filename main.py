
import pygame
import ctypes
from functions import move_and_bounce

# Connaitre la taille de l'écran - juste pour moi 
usr32 = ctypes.windll.user32
print("width =", usr32.GetSystemMetrics(0))
print("height =", usr32.GetSystemMetrics(1))

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Protein Game...") # renome la fenetre de jeu
logo = pygame.image.load(r"C:\Users\Léo\OnedriveLeo\OneDrive\Esilv A4 CreaTek\CS jeu python_protein_game\asset\poulet1-removebg-preview.png")
pygame.display.set_icon(logo)#set icone fenetre 

#Player: image tankred
# chargement image
bodybuilder = pygame.image.load(r"asset\bodybuilder.png")
#bodybuilder2  = pygame.transform.scale_by(bodybuilder,2) # x2 sur la taille de l'image 

#position initial de l'image
playerX = 200
playerY = 450
#vitesse initial 
speedX = 5
speedY = 5

#chargement background 
background = pygame.image.load(r"C:\Users\Léo\OnedriveLeo\OneDrive\Esilv A4 CreaTek\CS jeu python_protein_game\asset\wallpaper_2monochrome.jpg")


# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacer et gérer le rebond     fonction .get_width() ---> avoir longeur image 
    playerX, playerY, speedX, speedY = move_and_bounce(playerX, playerY, speedX, speedY,bodybuilder.get_width(), bodybuilder.get_height(),screen.get_width(), screen.get_height())

#def player() :
 #Affiche le joueur à la position de debut de partie .
        #  screen.blit(bodybuilder,(playerX,playerY))

    # Dessiner le fond et le joueur
    screen.fill((0, 0, 0))  # Effacer l'écran
    screen.blit(background, (0, 0))  # Afficher le fond
    screen.blit(bodybuilder, (playerX, playerY))  # Afficher le joueur



    #MAJ de l'affichage 
    pygame.display.flip()  # Rafraîchir l'affichage
    clock.tick(60)  # Limiter le FPS à 60

   
pygame.quit()

