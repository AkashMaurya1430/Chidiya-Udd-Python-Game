import pygame
import time
import sqlite3
import random
from threading import Thread


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def check_score(name):
    global score
    global a
    if (name == 1 and clicked):
        score += 1
    if (name != 1 and clicked):
        score -= 1


def draw_score(screen, x, y, score):
    font = pygame.font.SysFont('Arial', 36)  # Choose the font for the text
    text = font.render("Score = " + str(score), 3, BLACK)  # Create the text
    screen.blit(text, (x, y))  # Draw the text on the screen


# Displays Name of animal
def show_name(animal_name):
    font = pygame.font.SysFont('Arial', 72)  # Choose the font for the text
    dis_name = font.render(str(animal_name), 3, BLACK)
    screen.blit(dis_name, (160, 200))


# As the Function name suggests
def fetch_data():
    conn = sqlite3.connect("chidiya.db")
    c = conn.cursor()
    c.execute("select * from animals order by RANDOM() Limit 1")
    for a in c.fetchall():
        show_name(a[1])
    check_score(a[2])
    conn.commit()
    conn.close()


# Game Setup
pygame.init()
screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Chidiya Udd")

# run until user clicks close button
done = False

# score
score = 0

clicked = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
screen.fill(WHITE)
t1 = Thread(target=fetch_data)
t1.start()
draw_score(screen, 160, 450, score)

#-----Main Program-----#
millis = int(round(time.time() * 1000))
while not done:
    # pygame.time.wait(200)
    if int(round(time.time() * 1000)) - millis >= 2000:
        millis = int(round(time.time() * 1000))
        screen.fill(WHITE)
        fetch_data()
        draw_score(screen, 160, 450, score)
        clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                clicked = True
                # check_score()
                screen.fill(WHITE)
                draw_score(screen, 160, 450, score)
                show_name(a[i])
                # clicked = False

    #  Game GUI
    # must be at start or it will fill white on other objects

    # Show Name of animals
    # data_no = random.randint(0, 2)
    # fetch_data()
    # screen.fill(WHITE)

    # Show the score on the screen

    # clock.tick(60)
    pygame.display.flip()
    # pygame.time.wait(500)
    # clicked = False
    # pygame.time.wait(500)
