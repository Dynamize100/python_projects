import pygame
from random import randint

DIR_RESOURCES = "resources/"
FILE_IMAGE_SPRITE_ROCK = DIR_RESOURCES + "rockSm.jpg"

PROP_SIZE_BLOCK = 30
PROP_SIZE_SCREEN_WIDTH = 1000
PROP_SIZE_SCREEN_HEIGHT = 800

class Rock:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(FILE_IMAGE_SPRITE_ROCK).convert()
        self.x = randint(1, int(PROP_SIZE_SCREEN_WIDTH / PROP_SIZE_BLOCK) - 1) * PROP_SIZE_BLOCK
        self.y = randint(1, int(PROP_SIZE_SCREEN_HEIGHT / PROP_SIZE_BLOCK) - 1) * PROP_SIZE_BLOCK

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = randint(1, int(PROP_SIZE_SCREEN_WIDTH / PROP_SIZE_BLOCK) - 1) * PROP_SIZE_BLOCK
        self.y = randint(1, int(PROP_SIZE_SCREEN_HEIGHT / PROP_SIZE_BLOCK) - 1) * PROP_SIZE_BLOCK