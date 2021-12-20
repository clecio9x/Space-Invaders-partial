import sys
import pygame
from player1 import Player

# Cor de fundo
background_color = [0, 0, 0]

# Titulo da janela
title = "Space Invaders"

# player1
class Game:
    def __init__(self):
        player_sprite = Player((width / 2, height),width,10)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.player.firer = pygame.sprite.GroupSingle()

    def run(self):
        self.player.update()
        self.player.sprite.firer.draw(screen)
        self.player.draw(screen)


# programção da janela, configurada com o tamanho altura, largura = 800x680
if __name__ == "__main__":
    pygame.init()
    size = width, height = 800, 680
    speed = [1, 10]
    screen = pygame.display.set_mode((width, height))
    pygame.time.Clock()
    clock = pygame.time.Clock()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.run()
        pygame.display.flip()
        screen.fill(("black"))
        clock.tick(60)

