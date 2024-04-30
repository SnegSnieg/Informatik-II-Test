import pygame
import time
import random
from PIL import Image
import requests
from io import BytesIO
import json

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

# def save_score(score):
#     with open('Bestenliste.json', 'w') as file:
#         json.dump(score, file)

# def load_scores():
#     try:
#         with open('Bestenliste.json', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}

# def update_higscorelist(name, score):
#     highscores = load_scores()
#     if name in highscores:
#         highscores[name] = max(highscores[name], score)
#     else:
#         highscores[name] = score
#     save_score(highscores)

def save_scores(scores):
    with open('Bestenliste.json', 'w') as file:
        json.dump(scores, file)

def load_scores():
    try:
        with open('Bestenliste.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def update_highscore_list(name, score):
    highscores = load_scores()
    if name in highscores:
        highscores[name] = max(highscores[name], score)
    else:
        highscores[name] = score
    save_scores(highscores)

# Beispiel:
# update_leaderboard("Alice", 150)
# update_leaderboard("Bob", 200)
# update_leaderboard("Alice", 180)



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