import pygame
import  random
import animation

class Monstre(animation.Animation):

    # Constructeur
    def __init__(self, jeu, name, size, offset=0):
        super().__init__(name,size)
        self.jeu = jeu
        self.vie = 100
        self.vie_max = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540 - offset
        self.startAnimation()
        self.degat_subit = 10

    def set_speed(self,speed):
        self.default_speed = speed
        self.vitesse = random.randint(1, 3)

    def set_degatSubit(self, degat):
        self. degat_subit = degat


    # Fonction de mort du monstre
    def monster_death(self,degat):
        self.vie -= degat
        # Condition d'existance
        if self.vie <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.vitesse += random.randint(1, self.default_speed)
            self.vie = self.vie_max
            # ajouter le nombre de points
            self.jeu.gameScore(self.degat_subit)

            # si la barre d'evenement de pluie de feu est chargé à son maximum
            if self.jeu.pluieF.est_charge():
                #retirer les monstres de jeu
                self.jeu.all_monstres.remove(self)
                # Declenchement de la pluie
                self.jeu.pluieF.pluie()


    def monsterAnimation(self):
        self.animate(loop=True)

    # Fonction de vie du monstre
    def life(self, surface_devie):

        # Assignation a l'ecran pour la création d'un nouveau rectangle
        pygame.draw.rect(surface_devie, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.vie_max, 5])
        pygame.draw.rect(surface_devie,(111,210,8),[self.rect.x + 10,self.rect.y - 20,self.vie,5])


    # Fonction de Deplacement du monstre
    def se_deplace(self):
        # S'il n'y a pas de collision avec le joueur
        if not self.jeu.collision(self,self.jeu.all_joueurs):
           self.rect.x -= self.vitesse
        else:
          # recuperation du joueur pour lui infliger des degats
          self.jeu.joueur.death(self.attack)

class Mummy(Monstre):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_degatSubit(10)



class Alien(Monstre):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300),150)
        self.vie = 250
        self.vie_max = 250
        self.set_speed(1)
        self.attack = 0.5
        self.set_degatSubit(20)
