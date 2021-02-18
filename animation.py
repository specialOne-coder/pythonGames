import pygame
import random

class Animation(pygame.sprite.Sprite):

    def __init__(self, spriteName, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{spriteName}.png")
        self.image = pygame.transform.scale(self.image,size)
        self.current_image = 0  # commencer l'anim à 0
        self.images = animations.get(spriteName)
        self.animation = False


    # Methode pour demarrer l'animation
    def startAnimation(self):
        self.animation = True

    # Methode pour animer le Sprite
    def animate(self,loop=False):
        # iterer les images et revenir au
        # debut si l'image courant es < à la taille
        if self.animation:
            self.current_image += random.randint(0,1)
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# fonction pour charger les image d'un sprite
def load_images(spriteName):
    images = []
    path = f"assets/{spriteName}/{spriteName}"
    # recuperer chacque image
    for num in range(1, 24):
        images.append(pygame.image.load(path + str(num) + '.png'))
    return images

# Dictionnaire qui va contenuir les images de chacque sprite
animations = {
    'mummy': load_images('mummy'),
    'player': load_images('player'),
    'alien' : load_images('alien')
}
