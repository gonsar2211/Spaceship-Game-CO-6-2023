import pygame
import random
from game.components.enemis.enemy import Enemy
from game.utils.constants import ENEMY_2


class Enemy2(Enemy):
    WIDTH = 40
    HEIGTH = 60
    SPEED_X = random.randint(4,25)
    SPEED_Y = random.randint(7,15)


    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)
