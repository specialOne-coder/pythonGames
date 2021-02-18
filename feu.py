import pygame
import random

class Feu(pygame.sprite.Sprite):

    def __init__(self,pluie):
        super().__init__()
        #image
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.vitesse = random.randint(1,4)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0,800)
        self.pluie = pluie



    def retirerFeu(self):
        self.pluie.all_feu.remove(self)
        # jouon le son
        self.pluie.game.mesSons.play('meteor')
        if len(self.pluie.all_feu) == 0:
            self.pluie.resetP()
            self.pluie.game.start()
            self.pluie.game.start()


    def chute(self):
        self.rect.y += self.vitesse
        if self.rect.y >= 500:
            print("sol")
            self.retirerFeu()
            # s'il n'y a plus de boule de feu reactiver les monstres
            if len(self.pluie.all_feu) == 0:
                print("Pluie finie")
                self.pluie.resetP()
                self.pluie.mode = False
        # Verifier si la boule de feu touche le joueur
        if self.pluie.game.collision(self,self.pluie.game.all_joueurs):
            print('joueur touché')
            self.retirerFeu()
            self.pluie.game.joueur.death(20)
