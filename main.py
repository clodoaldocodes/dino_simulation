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

def main():
    run = Trueclock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False




main()