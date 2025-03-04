import pygame
from Object import Object


class Segment(Object):
    def __init__(self, x, y, w, h, filepath, speed):
        super().__init__(x, y, w, h, filepath)
        self.speed = speed


    def update(self, targetPos):

        dirc = [targetPos[0] - self.rect.x, targetPos[1] - self.rect.y]
        length = (dirc[0] ** 2 + dirc[1] ** 2) ** (1/2)
        if length < self.rect.w/2:
            return
        dirc = [dirc[0] / length, dirc[1] / length]
        self.rect.x += dirc[0] * self.speed
        self.rect.y += dirc[1] * self.speed

