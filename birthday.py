import pygame as pg
import time 
import os
clock = pg.time.Clock()

dp = pg.display.set_mode((800, 800))


words = [
 ["А"," ","в","т","о","р","o","й"," ", "к","у""п","л","е","т","?"],
 ["Его пока что нет!"],
 ["И вам не повезло: щас будет набор слов"],
 ["Аэробика, четыре гомика"],
 ["Сплю я с пушкою под подушкою"],
 ["Спеют яблочки, светят лампочки"],
 ["Сила трения"], 
 ["с днём рождения"],
 ["Будешь рыпаться"],
 ["дам под дыхало"],
 ["Играет и поёт"],
 ["Валя Стрыкало"]
 ]

xz = []
xzt = []
x = 20
y= 20
#def wd():
    #if l == " ":
       # x = 20
        #y += 120
    #else:
       # pg.draw.rect(dp,(99, 81, 38),l)


game = True
while game:

    dp.fill((209, 191, 148))
    #for i in range(len(xz)):
    
         
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
            


    for term in words:
        for word in term:
            l = pg.Rect(x,y,50,70)
            #xz.append(l)
            if word == " ":
                x = 20
                y += 120
            else:
                pg.draw.rect(dp,(99, 81, 38),l)
                x+=80
            #xzt.append(word)
            
            
          
                
        
    pg.display.flip() 
    clock.tick(60)