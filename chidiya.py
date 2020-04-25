#module imports
import pygame
import time
from threading import Thread
import sqlite3
import random

#initializing variables
score = 0
names = ()
values = ()

#fetch data from database
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
r=c.execute("Select Name,Value from animals order by RANDOM()")
for n,v in r.fetchall():
    names = names + (n,)
    values = values + (v,)
conn.close()
print(names)
print(values)


#updation of score
def update_score(w, x, y, score):
    font = pygame.font.SysFont('Arial', 36)  # Choose the font for the text
    text = font.render("Score = " + str(score), 3, black)  # Create the text
    w.blit(text, (x, y))
    pygame.display.update()

#updation of animal
def update_animal():
    print("hello")
    for i in range(9):
        font = pygame.font.SysFont('Arial', 72)  # Choose the font for the text
        dis_name = font.render(names[i], 3, black)
        w.blit(dis_name, (160, 200))
        print(names[i])
        i=i+1
        time.sleep(2)



#Window settings
x = pygame.init()
w = pygame.display.set_mode((500,500))
white = [255, 255, 255]
black = [0, 0, 0]

pygame.display.set_caption("Chidiya")


#thread to update animal
threadanimal = Thread(target=update_animal)
threadanimal.start()  


#Events
running=True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: 
                score = score + 1
    
    w.fill(white)
    #thread to increase score
    threadscore = Thread(target=update_score,args=[w, 160, 450, score,])
    threadscore.start()      
                
pygame.quit()

