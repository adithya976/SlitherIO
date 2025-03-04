import pygame
from Player import Player
from Orb import Orb
from Camera import Camera
import random


START_W = 50
START_H = 50
PLAYER_START_X = 0
PLAYER_START_Y = 0
PLAYER_COLOR = "blue.png"

fps = 90
NUM_ORBS = 200



class MainCG:
    def __init__(self):
        self.winDims = (800, 800)
        self.window = pygame.display.set_mode(self.winDims)
        self.winColor = (60, 102, 102)
        self.quit = False
        self.clock = pygame.time.Clock()

        self.camera = Camera(PLAYER_START_X, PLAYER_START_Y, (START_W, START_H), self.winDims)

        self.player = Player(PLAYER_START_X, PLAYER_START_Y, START_W, START_H, PLAYER_COLOR)
        self.orbs = []
        self.removed_orbs = 0


    def init(self):

        Texture = ["bitmap.png", "blue.png", "l_green.png", "neon.png", "red.png", "yellow.png"]

        for i in range(0, NUM_ORBS):
            randx = random.randint(-self.winDims[0] * 2, self.winDims[0] * 2)
            randy = random.randint(-self.winDims[1] * 2, self.winDims[1] * 2)
            # randx = random.randint(0, self.winDims[0])
            # randy = random.randint(0, self.winDims[1])

            randR = random.randint(10, START_W)
            randTexture = random.choice(Texture)
            newOrb = Orb(randx, randy, randR, randTexture)
            self.orbs.append(newOrb)

        self.play()

    def play(self):
        while not self.quit:
            self.update()
            self.render()
            if self.quit == True:
                print(f"SCORE: {self.player.score}")


    def update(self):
        self.clock.tick(fps)
        # window events update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
        # player update
        self.player.update(self.winDims)
        # orb update
        for orb in self.orbs:
            if orb.update(self.player):
                self.orbs.remove(orb)


        # camera update
        self.camera.update(self.player.rect.x, self.player.rect.y)

    def render(self):
        self.window.fill(self.winColor)
        self.player.draw(self.window, self.camera)

        for orb in self.orbs:
            orb.draw(self.window, self.camera)

        pygame.display.update()
