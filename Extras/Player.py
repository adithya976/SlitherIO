import pygame
from Object import Object
from Segment import Segment


class Player(Object):
    def __init__(self, x, y, w, h, filepath):
        super().__init__(x, y, w, h, filepath)

        self.speed = 7
        self.boost = 1
        self.prevScore = 0
        self.score = 0
        self.segments = []

    def update(self, winDims):
        mousePos = pygame.mouse.get_pos()
        worldPos = (mousePos[0] - winDims[0] / 2 + self.rect.x, mousePos[1] - winDims[1] / 2 + self.rect.y)
        dir = (worldPos[0] - self.rect.x, worldPos[1] - self.rect.y)
        mag = (dir[0] ** 2 + dir[1] ** 2) ** (1 / 2)
        dir = (dir[0] / mag, dir[1] / mag)

        self.rect.x += dir[0] * self.speed
        self.rect.y += dir[1] * self.speed

        keys = pygame.key.get_pressed()
        #
        if keys[pygame.K_SPACE]:
            self.boost = 7/3
        if keys[pygame.K_b]:
            self.boost = 1
        # if keys[pygame.K_UP]:
        #     self.rect.y -= self.speed
        # if keys[pygame.K_DOWN]:
        #     self.rect.y += self.speed

        # print("Player X:" + str(self.rect.x))
        # print("Mouse X:" + str(worldPos[0]))
        if self.score - self.prevScore >= 20:
            self.prevScore = self.score
            # print("SCORE:",self.score)

            startX = dir[0] * -1 * self.rect.w/2
            startY = dir[1] * -1 * self.rect.h/2

            if len(self.segments) == 0:
                startX += self.rect.x
                startY += self.rect.y
            else:
                startX += self.segments[-1].rect.x
                startY += self.segments[-1].rect.y

            newSegment = Segment(startX, startY, self.rect.w, self.rect.h, "blue.png", self.speed)
            self.segments.append(newSegment)

        for i in range(len(self.segments)):
            if i == 0:
                self.segments[i].update((self.rect.x, self.rect.y))
            else:
                self.segments[i].update((self.segments[i - 1].rect.x, self.segments[i - 1].rect.y))

    def draw(self, window, camera):
        window.blit(self.texture, camera.translate(self.rect.x, self.rect.y))

        for segment in self.segments:
            window.blit(segment.texture, camera.translate(segment.rect.x, segment.rect.y))
