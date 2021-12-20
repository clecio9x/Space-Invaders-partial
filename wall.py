import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, size,color,x,y) :
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = (x,y))

shape = [
"   xxxxxx",
" xxxxxxxxxx",
"xxxxxxxxxxxxx",
"xxxxxxxxxxxxx",
"xxxx     xxxx",
"xxx       xxx"]

