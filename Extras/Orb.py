import pygame
from Object import Object


class Orb(Object):
    def __init__(self, x, y, r, filepath):
        super().__init__(x, y, r, r, filepath)
        # self.velocity = [-1, 1]

    def update(self, player):
        # self.rect.x += self.velocity[0]
        # self.rect.y += self.velocity[1]

        if self.rect.colliderect(player.rect):
            player.score += 5
            return True
        return False
