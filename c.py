import pygame
import time
import sqlite3
import random


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def check_score(name):
    global clicked
    global score
    print(name)
    if (name[2] == 1 and clicked):
        score += 1


# Displays Score
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
def fetch_data(k):
    conn = sqlite3.connect("chidiya.db")
    c = conn.cursor()

    # c.execute("CREATE TABLE IF NOT EXISTS animals(No INT, Name TEXT, Value INT)")
    # c.execute("INSERT INTO animals VALUES(0,'Lion',0)")
    # c.execute("INSERT INTO animals VALUES(1,'Tiger',0)")
    # c.execute("INSERT INTO animals VALUES(2,'Sparrow',1)")
    # name = c.execute("select Name from animals where No=?", (k,)

    c.execute("select * from animals order by RANDOM() Limit 1")
    for a in c.fetchall():
        show_name(a[1])

    check_score(a)
    # pygame.time.wait(1000)
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

#-----Main Program-----#
while not done:
    # pygame.time.wait(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                clicked = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                clicked = True

    #  Game GUI
    # must be at start or it will fill white on other objects
    screen.fill(WHITE)

    # Show Name of animals
    data_no = random.randint(0, 2)
    fetch_data(data_no)

    # Show the score on the screen
    draw_score(screen, 160, 450, score)

    # clock.tick(60)
    pygame.display.flip()
    pygame.time.wait(500)
    # clicked = False
    pygame.time.wait(500)
