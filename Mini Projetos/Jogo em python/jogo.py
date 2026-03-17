import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game settings
FPS = 60
PLAYER_SPEED = 5
BULLET_SPEED = 7
ENEMY_SPEED = 2
POWERUP_SPEED = 3

# Powerup types
POWERUP_TYPES = ['extra_bullet', 'speed_up', 'shield', 'extra_life']
POWERUP_COLORS = {
    'extra_bullet': YELLOW,
    'speed_up': GREEN,
    'shield': BLUE,
    'extra_life': RED
}

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space InPython")
clock = pygame.time.Clock()

# Load images
try:
    player_img = pygame.image.load('nave.png')
    player_img = pygame.transform.scale(player_img, (50, 40))
    enemy_img = pygame.image.load('enemie.png')
    enemy_img = pygame.transform.scale(enemy_img, (40, 30))
except pygame.error as e:
    print(f"Error loading images: {e}")
  
    player_img = pygame.Surface((50, 40))
    player_img.fill(GREEN)
    enemy_img = pygame.Surface((40, 30))
    enemy_img.fill(RED)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = PLAYER_SPEED
        self.lives = 3
        self.has_shield = False
        self.shield_timer = 0
        self.bullet_count = 1
        self.last_shot = 0
        self.shoot_delay = 400

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        
        # Update shield timer
        if self.has_shield:
            self.shield_timer -= 1
            if self.shield_timer <= 0:
                self.has_shield = False

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullets = []
            if self.bullet_count == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                bullets.append(bullet)
            elif self.bullet_count >= 2:
                # Double bullet
                bullet1 = Bullet(self.rect.left + 10, self.rect.top)
                bullet2 = Bullet(self.rect.right - 10, self.rect.top)
                bullets.extend([bullet1, bullet2])
            return bullets
        return []

    def activate_powerup(self, powerup_type):
        if powerup_type == 'extra_bullet':
            self.bullet_count = min(self.bullet_count + 1, 5)
        elif powerup_type == 'speed_up':
            self.speed = min(self.speed + 2, 10)
        elif powerup_type == 'shield':
            self.has_shield = True
            self.shield_timer = 600  # 10 seconds at 60 FPS
        elif powerup_type == 'extra_life':
            self.lives = min(self.lives + 1, 5)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1

    def update(self, direction=None):
        if direction is not None:
            self.direction = direction
        self.rect.x += self.direction * ENEMY_SPEED

# Enemy Bullet class
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def update(self):
        self.rect.y += BULLET_SPEED // 2
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Powerup class
class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.type = random.choice(POWERUP_TYPES)
        self.image = pygame.Surface((25, 25))
        self.image.fill(POWERUP_COLORS[self.type])
        
        font = pygame.font.Font(None, 20)
        text = font.render(self.type[0].upper(), True, BLACK)
        self.image.blit(text, (8, 3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += POWERUP_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Game functions
def create_enemies(level):
    enemies = pygame.sprite.Group()
    rows = 3 + level // 2
    cols = 8 + level // 3
    for row in range(rows):
        for col in range(cols):
            x = 50 + col * 70
            y = 50 + row * 50
            enemy = Enemy(x, y)
            enemies.add(enemy)
    return enemies

def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y):
    # Draw shield indicator
    player = player_sprite.sprite
    if player.has_shield:
        pygame.draw.circle(surface, BLUE, (x, y), 15, 3)

def show_game_over(screen, score, level):
    screen.fill(BLACK)
    draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, RED)
    draw_text(screen, f"Score: {score}", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(screen, f"Level Reached: {level}", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
    draw_text(screen, "Press ENTER to restart or ESC to quit", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    return True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    return False

def show_level_complete(screen, level):
    screen.fill(BLACK)
    draw_text(screen, f"LEVEL {level} COMPLETE!", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, GREEN)
    draw_text(screen, "Get ready for the next level...", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    pygame.time.delay(2000)

# Main game loop
def game():
    
    global player_sprite
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    
    # Create player
    player = Player()
    player_sprite = pygame.sprite.GroupSingle(player)
    all_sprites.add(player)
    
    # Game variables
    level = 1
    score = 0
    enemy_direction = 1
    enemy_move_timer = 0
    enemy_move_delay = 1000 - (level * 50)  # Enemies get faster each level
    enemy_shoot_timer = 0
    
    # Create enemies for level
    enemies = create_enemies(level)
    all_sprites.add(enemies)
    
    running = True
    game_over = False
    
    while running:
        clock.tick(FPS)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    new_bullets = player.shoot()
                    for bullet in new_bullets:
                        all_sprites.add(bullet)
                        bullets.add(bullet)
        
        if not game_over:
            
            all_sprites.update()
            
            # Enemy movement
            now = pygame.time.get_ticks()
            if now - enemy_move_timer > enemy_move_delay:
                enemy_move_timer = now
                move_down = False
                
                for enemy in enemies:
                    if enemy.rect.right >= SCREEN_WIDTH - 10:
                        move_down = True
                        break
                    if enemy.rect.left <= 10:
                        move_down = True
                        break
                
                if move_down:
                    enemy_direction *= -1
                    for enemy in enemies:
                        enemy.rect.y += 20
                        enemy.direction = enemy_direction 
                        if enemy.rect.bottom >= player.rect.top:
                            game_over = True
                else:
                    for enemy in enemies:
                        enemy.direction = enemy_direction 
                        enemy.update()
            
            # Enemy shooting
            if now - enemy_shoot_timer > 2000 - (level * 100):
                enemy_shoot_timer = now
                if enemies:
                    shooting_enemy = random.choice(enemies.sprites())
                    enemy_bullet = EnemyBullet(shooting_enemy.rect.centerx, shooting_enemy.rect.bottom)
                    all_sprites.add(enemy_bullet)
                    enemy_bullets.add(enemy_bullet)
            
            # Collision: bullets hit enemies
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                score += 10 * level
                
                if random.random() < 0.2:
                    powerup = Powerup(hit.rect.centerx, hit.rect.centery)
                    all_sprites.add(powerup)
                    powerups.add(powerup)
            
            # Collision: player collects powerups
            powerup_hits = pygame.sprite.spritecollide(player, powerups, True)
            for powerup in powerup_hits:
                player.activate_powerup(powerup.type)
                score += 50
            
            # Collision: enemy bullets hit player
            bullet_hits = pygame.sprite.spritecollide(player, enemy_bullets, True)
            if bullet_hits:
                if player.has_shield:
                    player.has_shield = False
                    player.shield_timer = 0
                else:
                    player.lives -= 1
                    if player.lives <= 0:
                        game_over = True
            
            
            enemy_hits = pygame.sprite.spritecollide(player, enemies, False)
            if enemy_hits:
                game_over = True
            
            # Check if level is complete
            if len(enemies) == 0:
                show_level_complete(screen, level)
                level += 1
                enemy_move_delay = max(200, 1000 - (level * 50))
                enemies = create_enemies(level)
                all_sprites.add(enemies)
                
                score += 100 * level
        
        
        screen.fill(BLACK)
        all_sprites.draw(screen)
        
        # Draw UI
        draw_text(screen, f"Score: {score}", 24, SCREEN_WIDTH // 2, 10)
        draw_text(screen, f"Level: {level}", 24, 60, 10)
        draw_text(screen, f"Lives: {player.lives}", 24, SCREEN_WIDTH - 60, 10)
        
        
        if player.bullet_count > 1:
            draw_text(screen, f"Bullets: {player.bullet_count}", 18, 100, 40, YELLOW)
        if player.has_shield:
            draw_text(screen, "SHIELD", 18, SCREEN_WIDTH - 100, 40, BLUE)
        
        pygame.display.flip()
        
        # Game over screen
        if game_over:
            restart = show_game_over(screen, score, level)
            if restart:
                
                all_sprites.empty()
                enemies.empty()
                bullets.empty()
                enemy_bullets.empty()
                powerups.empty()
                
                player = Player()
                player_sprite = pygame.sprite.GroupSingle(player)
                all_sprites.add(player)
                
                level = 1
                score = 0
                enemy_direction = 1
                enemy_move_timer = 0
                enemy_move_delay = 1000
                enemy_shoot_timer = 0
                
                enemies = create_enemies(level)
                all_sprites.add(enemies)
                
                game_over = False
            else:
                running = False
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()
