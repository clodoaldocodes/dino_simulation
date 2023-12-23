import pygame
import os

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("D:\dino_simulation\Assets\Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("D:\dino_simulation\Assets\Dino", "DinoRun2.png"))]
JUMPING = [pygame.image.load(os.path.join("D:\dino_simulation\Assets\Dino", "DinoJump.png"))]
DUCKING = [pygame.image.load(os.path.join("D:\dino_simulation\Assets\Dino", "DinoDucki1.png")),
           pygame.image.load(os.path.join("D:\dino_simulation\Assets\Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("D:\dino_simulation\Assets\Cactus", "SmallCactus1.png")),
           pygame.image.load(os.path.join("D:\dino_simulation\Assets\Cactus", "SmallCactus2.png")),
           pygame.image.load(os.path.join("D:\dino_simulation\Assets\Cactus", "SmallCactus3.png"))]

LARGE_CARTUS = [pygame.image.load(os.path.join("D:\dino_simulation\Assets\Cactus", "LargeCactus1.png")),
           pygame.image.load(os.path.join("D:\dino_simulation\Assets\Cactus", "LargeCactus2.png")),
           pygame.image.load(os.path.join("D:\dino_simulation\Assets\Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("D:\dino_simulation\Assets\Bird", "Bird1.png")),
           pygame.image.load(os.path.join("D:\dino_simulation\Assets\Bird", "Bird2.png"))]

CLOUD = [pygame.image.load(os.path.join("D:\dino_simulation\Assets\Other", "Cloud.png"))]

BG = [pygame.image.load(os.path.join("D:\dino_simulation\Assets\Other", "Track.png"))]

class Dinosaur:
    X_POS = 80
    Y_POS = 310

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        
        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dinp_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.dino_duck()
        if self.dino_run:
            self.dino_run()
        if self.dino_jump:
            self.dino_jump()

        if self.step_index >= 10:
            self.step_index = 0


def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    SCREEN.fill((255,255,255))
    userInput = pygame.key.get_pressed()

    player.draw(SCREEN)
    player.update(userInput)

    clock.tick(30)
    pygame.display.update()

main()