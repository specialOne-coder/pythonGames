import pygame
from jeu import Jeu
import math
from monstre import Monstre
pygame.init()

# Definition d'une clock
clock = pygame.time.Clock()
FPS = 60

# Generer la fenetre du jeu
pygame.display.set_caption("Ecran principal")

# surface
surface = pygame.display.set_mode((1080, 700))

# arriere plan
fond = pygame.image.load("assets/bg.jpg")
accueil = pygame.image.load("assets/banner.png")

# Redimensionnement de l'image d'accueil
accueil = pygame.transform.scale(accueil,(500,500))
accueil_rect = accueil.get_rect()
accueil_rect.x = math.ceil(surface.get_width() / 4)

# Redimensionnement de la taille du boutton
button_img = pygame.image.load("assets/button.png")
button_img = pygame.transform.scale(button_img,(500,200))
# Redimensionnement de la position du boutton
button_img_rect = button_img.get_rect()
button_img_rect.x = math.ceil(surface.get_width() / 4)
button_img_rect.y = math.ceil(surface.get_height() / 1.9)
# Chargement du jeu
game = Jeu()
# m = Monstre(game)

# Variable de conditionnement du jeu
lancement = True


while lancement:

    # Assignation de l'arriere plan au jeu
    surface.blit(fond, (0, -200))

    # voir si le jeu a commencé
    if game.is_play:
        game.update(surface)
    else:
        surface.blit(button_img,button_img_rect)
        surface.blit(accueil, accueil_rect)


    # mise a jour de l'ecran
    pygame.display.flip()
    # Controle de l'action de l'utilisateur

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lancement = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.presser[event.key] = True
            # Gestion des projectiles
            if event.key == pygame.K_SPACE:
                game.joueur.lancer_pouvoir()
            elif event.key == pygame.K_b:
                game.joueur.sauter()
        elif event.type == pygame.KEYUP:
            game.presser[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_img_rect.collidepoint(event.pos):
               game.start()
               game.mesSons.play('click')
    # fixer le nombre de FPS sur la clock
    clock.tick(FPS)

