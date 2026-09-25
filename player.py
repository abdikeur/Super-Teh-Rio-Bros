import pygame
from settings import WIDTH, HEIGHT
from settings import GRAVITY, JUMP_STRENGTH, MOVE_SPEED
from settings import PLAYER_IMAGE


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load(PLAYER_IMAGE).convert_alpha()

        hitbox_w, hitbox_h = 30, 54
        self.rect = pygame.Rect(x, y, hitbox_w, hitbox_h)

        self.start_pos = (x, y)
        self.vel_y = 0
        self.on_ground = False

    def handle_input(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= MOVE_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += MOVE_SPEED

        if (keys[pygame.K_SPACE] or
            keys[pygame.K_UP] or
            keys[pygame.K_w]) and self.on_ground:
            self.vel_y = JUMP_STRENGTH

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += int(self.vel_y)

    def check_platform_collisions(self, platforms):
        self.on_ground = False

        for plat in platforms:
            if self.rect.colliderect(plat.rect) and self.vel_y >= 0:
                if self.rect.bottom - int(self.vel_y) <= plat.rect.top + 1:
                    self.rect.bottom = plat.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                    
    def check_spike_collisions(self, spikes):
        for spike in spikes:
            if self.rect.colliderect(spike.rect):
                self.rect.topleft = self.start_pos
                self.vel_y = 0
                return True
        return False
    
    def check_saw_collisions(self, saws):
        for saw in saws:
            if self.rect.colliderect(saw.rect):
                self.rect.topleft = self.start_pos
                self.vel_y = 0
                return True
        return False

    def keep_in_bounds(self):
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def reset_if_fallen(self):
        if self.rect.top > HEIGHT:
            self.rect.topleft = self.start_pos
            self.vel_y = 0
            return True
        return False

    def update(self, keys, platforms, spikes, saws):
        self.handle_input(keys)
        self.apply_gravity()
        self.check_platform_collisions(platforms)
        self.keep_in_bounds()
        if self.check_spike_collisions(spikes):
            return True
        if self.check_saw_collisions(saws):
            return True
        
        return self.reset_if_fallen()

    def draw(self, screen):
        image_rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, image_rect)