# module imports
import pygame
import time
from threading import Thread
import sqlite3
import random

# initializing variables
score = 0
names = ()
values = ()
dis = True

# fetch data from database
conn = sqlite3.connect("chidiya.db")
c = conn.cursor()
'''
c.execute("CREATE TABLE IF NOT EXISTS animals(No INT, Name TEXT, Value INT)")
c.execute("INSERT INTO animals VALUES(0,'Lion',0)")
c.execute("INSERT INTO animals VALUES(1,'Crow',1)")
c.execute("INSERT INTO animals VALUES(2,'Tiger',0)")
c.execute("INSERT INTO animals VALUES(3,'Sparrow',1)")
c.execute("INSERT INTO animals VALUES(4,'Duck',1)")
c.execute("INSERT INTO animals VALUES(5,'Deer',0)")
c.execute("INSERT INTO animals VALUES(6,'Elephant',0)")
c.execute("INSERT INTO animals VALUES(7,'Eagle',1)")
c.execute("INSERT INTO animals VALUES(8,'Kite',1)")
c.execute("INSERT INTO animals VALUES(9,'Aeroplane',1)")
conn.commit()
'''
r = c.execute("Select Name,Value from animals order by RANDOM()")
for n, v in r.fetchall():
    names = names + (n,)
    values = values + (v,)
conn.close()
print(names)
print(values)

# updation of score


def update_score(w, x, y, score):
    if dis:
        font = pygame.font.SysFont('Arial', 36)  # Choose the font for the text
        text = font.render("Score = " + str(score), 3,
                           black)  # Create the text
        w.blit(text, (x, y))
        pygame.display.update()


# updation of animal
def update_animal():
    global fly
    for i in range(3):
        w.blit(background, (0, 0))
        # w.fill(white)
        font = pygame.font.SysFont('Arial', 72)  # Choose the font for the text
        dis_name = font.render(names[i], 3, black)
        w.blit(dis_name, (130, 200))
        print(names[i])
        fly = values[i]
        i = i+1
        time.sleep(1)
    dis = False
    w.blit(background, (0, 0))
    endscreen()
    time.sleep(2)
    pygame.quit()


def endscreen():
    rect = pygame.Rect(0, 0, 500, 500)
    w.blit(w, rect)
    w.blit(background, (0, 0))
    font = pygame.font.SysFont('Arial', 72)  # Choose the font for the text
    dis_score = font.render("Score = " + str(score), 3,
                            black)  # Create the text
    w.blit(dis_score, (160, 200))
    pygame.display.update()


# Window settings
x = pygame.init()
w = pygame.display.set_mode((500, 500))
white = [255, 255, 255]
black = [0, 0, 0]
pygame.display.set_caption("Chidiya")
w.fill(white)

# Music
# music = pygame.mixer.music.load('C:\\Users\Asus\Pictures\sbirds.mp3')
# pygame.mixer.music.play(-1)

# Background Image
background = pygame.image.load('sokay.png')
w.blit(background, (0, 0))

# thread to update animal
threadanimal = Thread(target=update_animal)
threadanimal.start()


# Events
running = True
while running:
    # pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                flag = 1
                if flag == fly:
                    score = score + 1
                elif flag != fly:
                    score = score - 1
    rect = pygame.Rect(130, 440, 20, 60)
    w.blit(w, rect)
    # thread to increase score
    threadscore = Thread(target=update_score, args=[w, 160, 450, score, ])
    threadscore.start()
pygame.quit()
