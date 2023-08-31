import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
screen_width = 1500
screen_height = 1000
player_speed = 5
enemy_speed = 3
bullet_speed = 8
enemy_spawn_rate = 0.02

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shoot 'em Up Game")

# Load images
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")
bullet_image = pygame.image.load("bullet.png")

# Initialize player
player_x = screen_width // 2
player_y = screen_height - player_image.get_height()
player_rect = player_image.get_rect(center=(player_x, player_y))

# Lists to store enemies and bullets
enemies = []
bullets = []

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_h] or keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_l] or keys[pygame.K_RIGHT] and player_rect.right < screen_width:
        player_rect.x += player_speed
    if keys[pygame.K_SPACE]:
        bullet_rect = bullet_image.get_rect(center=(player_rect.centerx, player_rect.top))
        bullets.append(bullet_rect)

    # Update bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Update enemies and check collisions
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.colliderect(player_rect):
            running = False
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)

    # Spawn enemies
    if random.random() < enemy_spawn_rate:
        enemy_x = random.randint(0, screen_width - enemy_image.get_width())
        enemy_rect = enemy_image.get_rect(topleft=(enemy_x, 0))
        enemies.append(enemy_rect)

    # Clear the screen
    screen.fill(black)

    # Draw player, enemies, and bullets
    screen.blit(player_image, player_rect.topleft)
    for enemy in enemies:
        screen.blit(enemy_image, enemy.topleft)
    for bullet in bullets:
        screen.blit(bullet_image, bullet.topleft)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

