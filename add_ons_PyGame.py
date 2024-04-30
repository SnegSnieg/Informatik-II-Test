import pygame
import time
import random
from PIL import Image
import requests
from io import BytesIO
import csv
import sys

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

# versuch Json
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

# Funktion für die Usereingabe am Ende des Spiels
def get_end_game_input(screen, clock):
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(10, 40, 140, 32)
        color_active = pygame.Color('black')
        color_passive = pygame.Color('black')
        color = color_passive
        user_text = ''
        active = True
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            return user_text
                        elif event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode

            screen.fill((255, 255, 255))

            if active:
                color = color_active
            else:
                color = color_passive

            # Render den Text
            text = font.render('Gib Deinen Namen ein:', True, (0, 0, 0))

            # Position des Textes
            text_x = 10
            text_y = 10
            screen.blit(text, (text_x, text_y))

            pygame.draw.rect(screen, color, input_box)
            text_surface = font.render(user_text, True, (255, 255, 255))
            screen.blit(text_surface, (input_box.x+5, input_box.y+5))
            input_box.w = max(100, text_surface.get_width()+10)

            pygame.display.flip()
            clock.tick(60)
            return user_text
def highscore(score, highest):
    if score > highscore:
        highscore = score
        highscore_name = name
        highest = [highscore_name, highscore]
    else:
        pass
    return highest
    
# Funktion zum Schreiben der Werte eines Array als Zeilen in eine csv-Datei
def write_to_csv(array, filename):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(array)


# Funktion zum Lesen der Zeilen einer csv-Datei und speichern in einem Array
def read_from_csv(filename):
    array = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            array.append(row)
    return array


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
    sys.exit()

# Gegner Eigenschaften
ENEMY_WIDTH, ENEMY_HEIGHT = random.randint(20,50), random.randint(20,50)  # Größe des Gegners angepasst