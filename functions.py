

def move_and_bounce(x, y, speedX, speedY, img_width, img_height, screen_width, screen_height):
    """
    Met à jour la position de l'image et gère les rebonds.

    Paramètres :
        x, y (int) : Position actuelle de l'image.
        speedX, speedY (int) : Vitesse actuelle sur les axes X et Y.
        img_width, img_height (int) : Dimensions de l'image.
        screen_width, screen_height (int) : Dimensions de la fenêtre.

    Retourne :
        tuple : Nouvelle position (x, y) et vitesses mises à jour (speedX, speedY).
    """
    # Mettre à jour les positions
    x += speedX
    y += speedY

    # Vérifier les collisions avec les bords de la fenêtre
    if x <= 0 or x + img_width >= screen_width:
        speedX = -speedX  # Inverser la direction horizontale
    if y <= 0 or y + img_height >= screen_height:
        speedY = -speedY  # Inverser la direction verticale

    return x, y, speedX, speedY


def protein_total(proteine, x):

    proteine += x
    return proteine 

#def move_food_on_Y():