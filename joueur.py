import pygame
from pouvoir import Pouvoir
import random
import animation

# Classe su joueur

class Joueur(animation.Animation):

    # Constructor
    def __init__(self,jeu):
        super().__init__("player")
        self.vie = 100
        self.jeu = jeu
        self.vie_max = 100
        self.saut = 150
        self.pouvoir = 10
        self.all_pouvoirs = pygame.sprite.Group()
        self.vitesse = 5
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 500

    # Mort
    def death(self,moins):
        if self.vie - moins > moins:
           self.vie -= moins
        else:
            self.jeu.game_over()

    # pouvoir
    def lancer_pouvoir(self):
        pv = Pouvoir(self)
        self.all_pouvoirs.add(pv)
        self.startAnimation()
        self.jeu.mesSons.play('tir')

    def playerAnimation(self):
        self.animate()

    # deplacement à droite
    def dep_droite(self):
        if not self.jeu.collision(self,self.jeu.all_monstres):
           self.rect.x += self.vitesse

    # deplacement à droite
    def dep_gauche(self):
        self.rect.x -= self.vitesse

    # Saut
    def sauter(self):

        if self.rect.y == 500:
              self.rect.y -= self.saut
        else:
            self.rect.y += self.saut

    # Niveau de vie
    def life(self, surface_devie):
        # Assignation a l'ecran pour la création d'un nouveau rectangle
        pygame.draw.rect(surface_devie, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.vie_max, 5])
        pygame.draw.rect(surface_devie, (111, 210, 8), [self.rect.x + 50, self.rect.y + 20, self.vie, 5])


