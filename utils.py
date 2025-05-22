import pygame

def load_player_images():
    images = []
    for i in range(1, 5):
        img = pygame.transform.scale(
            pygame.image.load(f'assets/player_images/{i}.png'), (45, 45))
        images.append(img)
    return images

def load_ghost_images():
    blinky_img = pygame.transform.scale(pygame.image.load('assets/ghost_images/red.png'), (45, 45))
    pinky_img  = pygame.transform.scale(pygame.image.load('assets/ghost_images/pink.png'), (45, 45))
    inky_img   = pygame.transform.scale(pygame.image.load('assets/ghost_images/blue.png'), (45, 45))
    clyde_img  = pygame.transform.scale(pygame.image.load('assets/ghost_images/orange.png'), (45, 45))
    return blinky_img, pinky_img, inky_img, clyde_img
