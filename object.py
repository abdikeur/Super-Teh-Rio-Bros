import pygame

from settings import PLATFORM_IMAGE, GOAL_IMAGE, COIN_IMAGE, SPIKE_IMAGE, SAW_IMAGE


class Platform:
    SHEET = None

    ROW_HEIGHT = 16
    SPRITE_W = 32
    SPRITE_H = 9

    def __init__(self, x, y, w, h, color_row=1):
        if Platform.SHEET is None:
            Platform.SHEET = pygame.image.load(PLATFORM_IMAGE).convert_alpha()

        sprite = Platform.SHEET.subsurface(pygame.Rect(0, color_row * Platform.ROW_HEIGHT, Platform.SPRITE_W, Platform.SPRITE_H)).copy()

        self.image = pygame.transform.scale(sprite,(w, h))

        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Goal:
    def __init__(self, x, y, w, h):
        self.image = pygame.image.load(GOAL_IMAGE).convert_alpha()

        self.image = pygame.transform.scale(self.image,(w, h))

        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        

class Coin:
    def __init__(self, x, y):
        self.image = pygame.image.load(COIN_IMAGE).convert_alpha()

        self.rect = self.image.get_rect(topleft=(x, y))

        self.collected = False
        self.counted = False

    def update(self, player):
        if self.rect.colliderect(player.rect):
            self.collected = True
            
    def reset(self):
        self.collected = False
    

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)
            
class Spike:
    def __init__(self, x, y):
        self.image = pygame.image.load(SPIKE_IMAGE).convert_alpha()

        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
class Saw:
    def __init__(self, x, y):
        self.image = pygame.image.load(SAW_IMAGE).convert_alpha()

        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)