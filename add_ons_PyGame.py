import pygame
import time
import random
from PIL import Image
import requests
from io import BytesIO


ENEMY_WIDTH, ENEMY_HEIGHT = random.randint(20,50), random.randint(20,50)  # Größe des Gegners angepasst

def draw_enemies(enemies, screen):
    # Bild laden und Größe anpassen
    gegnerBild = pygame.image.load("Enemypicture.png")
    gegnerBild = pygame.transform.scale(gegnerBild, (ENEMY_WIDTH, ENEMY_HEIGHT))
    for enemy in enemies:
        # Zeichne das Gegnerbild an der Position des Gegners
        screen.blit(gegnerBild, (enemy.x, enemy.y))
pass

def scorecounting(score,ENEMY_SPEED):
    score += ENEMY_SPEED
    return score

def drawscore(score,BLACK,screen):
    display_field = pygame.font.Font(None,25)
    text = display_field.render(f"Score:{score}", True,BLACK)
    screen.blit(text,(450,5))

def save_highscore(score):
    with open('savescores.txt', 'w') as file:
        file.write(str(score))

def load_highscore():
    try:
        with open('savescores.txt', 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0


def gameover(screen,RED):
    display_field = pygame.font.Font(None,100)
    text = display_field.render("GAME OVER", True,RED)
    screen.blit(text,(100,70))
    pygame.display.flip()
    time.sleep(1)

def gameloop():
    pygame.quit()

# Gegner Eigenschaften
ENEMY_WIDTH, ENEMY_HEIGHT = random.randint(20,50), random.randint(20,50)  # Größe des Gegners angepasst