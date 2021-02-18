import pygame
from feu import Feu
# Classe de gestion des pluies de commet

class PluieDeFeu:

    # Construteur
    def __init__(self,game):
        self.pourcentage = 0
        self.vitesse = 100
        # groupe pour faire apparaitre plusieurs
        self.all_feu = pygame.sprite.Group()
        self.game = game
        self.mode = False

    def ajout_pourcentage(self):
        self.pourcentage +=self.vitesse/100


    def est_charge(self):
      return self.pourcentage >= 100


    def resetP(self):
        self.pourcentage = 0


    def apparution(self):

        for i in range(1, 10):
             self.all_feu.add(Feu(self))


    def pluie(self):
        #si la jauge est totalement chargé
        if self.est_charge() and len(self.game.all_monstres) == 0:
            self.resetP()
            self.apparution()
            self.mode = True


    def update_bar(self,surface):

        self.ajout_pourcentage()


        # Bar noir
        barnoir = pygame.draw.rect(surface,(0,0,0),[
                  0, # l'axe des x comme ça commence en bas à gauche
                  surface.get_height()-20, # l'axe de y
                  surface.get_width(), # longueur de la bar
                  10, # epaisseur de la bar
        ])
        # Bar rouge
        barrouge = pygame.draw.rect(surface,(187,11,11),[
                  0, # l'axe des x comme ça commence en bas à gauche
                  surface.get_height()-20, # l'axe de y
            (surface.get_width()/100)*self.pourcentage, # longueur de la bar
                  10, # epaisseur de la bar
        ])
