import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Color Change Example")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def change_color(self):
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

sprite1 = Sprite(RED, 50, 50)
sprite1.rect.x = 100
sprite1.rect.y = 100

sprite2 = Sprite(GREEN, 50, 50)
sprite2.rect.x = 200
sprite2.rect.y = 100

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 2000) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == COLOR_CHANGE_EVENT:
            sprite1.change_color() 

    screen.fill(WHITE)

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()