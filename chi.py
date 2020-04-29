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
clock = pygame.time.Clock()
updatescore = True


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
c.execute("INSERT INTO animals VALUES(10,'Jaguar',0)")
c.execute("INSERT INTO animals VALUES(11,'Parrot',1)")
c.execute("INSERT INTO animals VALUES(12,'Rabbit',0)")
c.execute("INSERT INTO animals VALUES(13,'Sparrow',1)")
c.execute("INSERT INTO animals VALUES(14,'Falcon',1)")
c.execute("INSERT INTO animals VALUES(15,'Giraffe',0)")
c.execute("INSERT INTO animals VALUES(16,'Horse',0)")
c.execute("INSERT INTO animals VALUES(17,'Pelican',1)")
c.execute("INSERT INTO animals VALUES(18,'Blue Jay',1)")
c.execute("INSERT INTO animals VALUES(19,'Emu',0)")
c.execute("INSERT INTO animals VALUES(20,'Robin',1)")
c.execute("INSERT INTO animals VALUES(21,'Kakapo',0)")
c.execute("INSERT INTO animals VALUES(22,'Kiwi',0)")
c.execute("INSERT INTO animals VALUES(23,'Dove',1)")
c.execute("INSERT INTO animals VALUES(24,'Raven',1)")
c.execute("INSERT INTO animals VALUES(24,'Hyena',0)")
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
def update_score(w, score):
    w.blit(background, (0, 450))
    # Choose the font for the text
    font = pygame.font.Font("digitalism.ttf", 36)
    text = font.render("Score = " + str(score), 3, black)  # Create the text
    w.blit(text, (240, 460))
    pygame.display.update()


def endscreen():
    global updatescore
    global running
    updatescore = False
    w.blit(background, (0, 0))
    dis_name = fontanimal.render("Thank You", 3, white)
    w.blit(dis_name, (70, 200))
    time.sleep(2)
    # running = False


# updation of animal
def update_animal():
    suraj = True
    global fly, count
    count = 0
    for i in range(10):
        count = count + 1
        w.blit(background, (0, 0))
        screenrect = w.get_rect()
        dis_name = fontanimal.render(names[i], 3, white)
        textrect = dis_name.get_rect()
        # To display text in the center of the screen
        textrect.center = screenrect.center
        w.blit(dis_name, textrect)
        print(names[i])
        fly = values[i]
        i = i+1
        time.sleep(1)
    endscreen()


def start_game():
    # music = pygame.mixer.music.load('D://GitHub/Python-Game/sbirds.mp3')
    # pygame.mixer.music.play(-1)
    w.blit(background, (0, 0))
    text = font1.render("Game starts in....", 3, white)
    text1 = fonto.render("Don't Forget to Hold Down Spacebar!!", 3, white)
    w.blit(text, (140, 200))
    w.blit(text1, (130, 300))
    pygame.display.update()
    time.sleep(2)

    for n in range(3, 0, -1):
        w.blit(background, (0, 0))
        font = pygame.font.Font("digitalism.ttf", 80)
        text = font.render(str(n), 3, white)
        w.blit(text, (290, 200))
        pygame.display.update()
        time.sleep(1.5)

    # calling thread to update animal
    threadanimal = Thread(target=update_animal)
    threadanimal.start()


# Window settings
x = pygame.init()
# music = pygame.mixer.music.load('sbirds.mp3')
# pygame.mixer.music.play(-1)
fontanimal = pygame.font.Font("Surfing Capital.ttf", 90)
w = pygame.display.set_mode((600, 500))
white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 100, 200]
pygame.display.set_caption("CHIDIYAA")

# Background Image
background = pygame.image.load('sokay.png')
w.blit(background, (0, 0))


# starting screen
rect1 = pygame.Rect(135, 175, 330, 100)
startbutton = pygame.draw.ellipse(w, white, rect1, 9)
font1 = pygame.font.Font("Surfing Capital.ttf", 40)
text = font1.render("Start game", 3, white)
w.blit(text, (180, 205))
fonto = pygame.font.Font("Surfing Capital.ttf", 20)
text = fonto.render("Press Enter to start", 3, white)
w.blit(text, (190, 330))
text = fonto.render("Hold Space-Bar.....Release to fly", 3, white)
w.blit(text, (150, 365))
pygame.display.update()

# Events
running = True
while running:
    # time.sleep(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if updatescore:
                    flag = 1
                    if flag == fly:
                        score = score + 1
                    elif flag != fly:
                        score = score - 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_game()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 135 and pygame.mouse.get_pos()[1] >= 175:
                if pygame.mouse.get_pos()[0] <= 465 and pygame.mouse.get_pos()[1] <= 275:
                    start_game()

    # clock.tick(100)
    # Update score
    # calling thread to increase score
    threadscore = Thread(target=update_score, args=[w, score])
    threadscore.start()

pygame.quit()
