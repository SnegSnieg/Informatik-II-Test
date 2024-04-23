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

def highscore(score,highscorelist,screen,BLACK,WHITE):
    highscorelist.append(score)
    highscorelist.sort(reverse=True)

    screen.fill(WHITE)
    display_field = pygame.font.Font(None,35)
    scorelist = display_field.render(f"Highscorelist:\n 1. {highscorelist[0]} \n 2. {highscorelist[1]} \n 3. {highscorelist[2]} \n 4. {highscorelist[3]} \n 5. {highscorelist[4]}", True,BLACK)
    screen.blit(scorelist,(5,5))
    pygame.display.flip()

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