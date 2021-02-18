import pygame

class Pouvoir(pygame.sprite.Sprite):

    # Constructor
    def __init__(self,joueur):
        super().__init__()
        self.vitesse = 5
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.joueur = joueur
        self.rect.x = joueur.rect.x + 120
        self.rect.y = joueur.rect.y + 80
        self.original_image = self.image
        self.angle = 0

    # Rotation de la boule de feu
    def rotation(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.original_image,self.angle,1)
        self.rect = self.image.get_rect(center = self.rect.center)


    # Suppression apres sa sortie
    def supprimer(self):
        self.joueur.all_pouvoirs.remove(self)

    # Roulade de la boule de feu
    def rouler(self):
        # deplacement de son pouvoir
        self.rect.x += self.vitesse
        self.rotation()
        for monstre in self.joueur.jeu.collision(self,self.joueur.jeu.all_monstres):
           self.supprimer()
           monstre.monster_death(self.joueur.pouvoir)
           # verifier s'il sort et le supprimer
        if self.rect.x > 1080:
            self.supprimer()
            print("pouvoir supprimé")
