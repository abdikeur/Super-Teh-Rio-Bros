import pygame

from settings import WIDTH, HEIGHT, FPS, SKY_BLUE, BLACK, MUSIC_FILE
from player import Player
from level import Level


pygame.init()

pygame.mixer.music.load(MUSIC_FILE)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Teh Rio Bros")

clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.player = Player(20, 580)

        # Start at level 1
        self.current_level = 1
        self.level = Level(self.current_level)

        self.total_coins = 0
        self.level_coins = 0
        
        self.start_time = pygame.time.get_ticks()
        self.final_time = 0

        self.font = pygame.font.SysFont(None, 60)
        self.won = False
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if self.won:
            return

        keys = pygame.key.get_pressed()

        # Update player using the platforms
        # from the current level
        dead = self.player.update(keys, self.level.platforms, self.level.spikes, self.level.saws)
        
        if dead:
            for coin in self.level.coins:
                coin.reset()
                
            self.level_coins = 0
            
        for coin in self.level.coins:
            was_collected = coin.collected
            coin.update(self.player)
            
            if coin.collected and not was_collected:
                self.level_coins += 1
                
                if not coin.counted:
                    self.total_coins += 1
                    coin.counted = True

        # Check if player reached the goal
        if self.player.rect.colliderect(self.level.goal.rect):
            self.next_level()

    def next_level(self):
        self.current_level += 1

        # If there are no more levels
        if self.current_level > 4:
            self.final_time = self.get_time()
            self.won = True
            return

        # Load the next level
        self.level = Level(self.current_level)
        self.level_coins = 0

        # Reset player position
        self.player.rect.topleft = self.player.start_pos
        self.player.vel_y = 0
        
    def get_time(self):
        if self.won:
            return self.final_time

        current_time = pygame.time.get_ticks()
        return (current_time - self.start_time) // 1000

    def draw(self):
        screen.fill(SKY_BLUE)

        # Draw current level's platforms
        for plat in self.level.platforms:
            plat.draw(screen)

        for coin in self.level.coins:
            coin.draw(screen)
            
        for spike in self.level.spikes:
            spike.draw(screen)
            
        for saw in self.level.saws:
            saw.draw(screen)
    
        # Draw current level's goal
        self.level.goal.draw(screen)

        # Draw player
        self.player.draw(screen)

        text = self.font.render(f"Total Coins: {self.total_coins}", True, BLACK)
        screen.blit(text, (20, 20))

        text = self.font.render(f"Level Coins: {self.level_coins}/{len(self.level.coins)}", True, BLACK)
        screen.blit(text, (20, 70))
        
        time = self.get_time()
        text = self.font.render(f"Time: {time}s", True, BLACK)
        screen.blit(text, (20, 120))
        
        # Show win message after the final level
        if self.won:
            text = self.font.render(
                "You Win!",
                True,
                BLACK
            )

            screen.blit(
                text,
                (
                    WIDTH // 2 - text.get_width() // 2,
                    HEIGHT // 2 - 30
                )
            )

        pygame.display.flip()

    def run(self):
        while self.running:
            clock.tick(FPS)

            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    Game().run()
