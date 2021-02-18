from joueur import Joueur
import pygame
from Pluie_deFeu import PluieDeFeu
from monstre import Monstre, Mummy,Alien
import son


#Classe du jeu
from monstre import Monstre


class Jeu:

    # Constructor
    def __init__(self):
        self.is_play = False
        # Player
        self.joueur = Joueur(self)
        self.all_joueurs = pygame.sprite.Group()
        self.all_joueurs.add(self.joueur)
        # Monster
        self.all_monstres = pygame.sprite.Group()
        self.presser = {}
        self.mesSons = son.SonManager()
        # pluie de feu
        self.pluieF = PluieDeFeu(self)
        self.score = 0
        self.font = pygame.font.SysFont("Serif", 25)


    # Fonction de score
    def gameScore(self, points = 10):
        self.score += points

    # Fonction de commencement du jeu

    def start(self):
        self.is_play = True
        self.generer_monstre(Mummy)
        self.generer_monstre(Mummy)
        self.generer_monstre(Alien)



    # Fonction de finition du jeu
    def game_over(self):
        # Game Over ,tout redemarrer
        self.all_monstres = pygame.sprite.Group()
        self.pluieF.all_feu = pygame.sprite.Group()
        self.joueur.vie = self.joueur.vie_max
        self.is_play = False
        self.score = 0
        self.mesSons.play('game_over')


    # Fonction de mise à jour en temps réel
    def update(self,surface):

        # Affichage du score sur l'ecran

        scoreText = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        surface.blit(scoreText, (20, 20))

        # Assignation du joueur au jeu
        game = self
        surface.blit(game.joueur.image, game.joueur.rect)
        game.joueur.playerAnimation()

        # Jauge de vie du joueur
        game.joueur.life(surface)

        # surface.blit(m.image, m.rect)
        # Assignation de la barre de temporisation d'arrivée des pluies de feu
        game.pluieF.update_bar(surface)
        # parcours des pouvoirs et roulement
        for pouvoir in game.joueur.all_pouvoirs:
            pouvoir.rouler()

        # Assignation du projectile à la surface
        game.joueur.all_pouvoirs.draw(surface)

        for monstre in game.all_monstres:
            monstre.se_deplace()
            monstre.life(surface)
            monstre.monsterAnimation()

        # Assignation du monstre à la surface
        game.all_monstres.draw(surface)

        for feux in self.pluieF.all_feu:
            feux.chute()
        # Assignation des feu à la surface
        game.pluieF.all_feu.draw(surface)
        # Deplacement du joueur
        if game.presser.get(pygame.K_RIGHT) and game.joueur.rect.x + game.joueur.rect.width < surface.get_width():
            game.joueur.dep_droite()
        elif game.presser.get(pygame.K_LEFT) and game.joueur.rect.x > 0:
            game.joueur.dep_gauche()



    def collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)


    def generer_monstre(self,monster_class):
        self.all_monstres.add(monster_class.__call__(self))

