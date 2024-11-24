import pygame as pg
import random
import os


pg.init()
pg.mixer.init()
clock = pg.time.Clock()

dp = pg.display.set_mode((800, 800))
 
bim= [1000,100, 10, 3, 3, 3, 3, 3, 25, 3, 3, 3, 3, 3, 40, 3,3, 15,3,3,3, 10,3,3, 20, 3,3,3]

words = [
 ["А вторoй куплет?"], 
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
 ["Валя Стрыкало"],
 ["Это — песня для девочек"],
 ["Чтобы девочки плакали."]
 ]

count = 0
directory = os.path.dirname(__file__)
d = directory + "\Валентин Стрыкало - Песня для девочек.mp3"


pg.mixer.music.load(d)
pg.mixer.music.set_volume(0.01)
pg.mixer.music.play(start = 83.0)


class Pizda():
    def __init__(self, x, y):
        self.x = x
        self.y= y
        self.rects = []
        self.rects_t = []


class Xyu_sosal():
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.font_link = directory + "/minecraft.ttf"
        self.shift = pg.font.Font(self.font_link, 50)
        self.text_shoft = self.shift.render(self.text, True, (0,0,0))

    def draw(self):
        dp.blit(self.text_shoft, self.pos)                    

c = Pizda(20,20)


for term in words:
    for word in term:
        for letter in word:
            if letter == " ":
                c.x = 20
                c.y += 100
            else:    
                cube = pg.Rect(c.x, c.y, 50, 70)
                text = Xyu_sosal(letter, (cube.centerx - 15, cube.centery - 25))
                c.rects.append(cube)
                c.rects_t.append(text)
                c.x += 80
        c.x = 20
        c.y += 100

rects_len = len(c.rects)

assert len(c.rects) == len(c.rects_t)

dum = 0
m = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
game = True




while game:
        

    dp.fill((209, 191, 148))

    
         
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
  
   
    for i in range(min(count // bim[dum], rects_len)):
        pg.draw.rect(dp, m, c.rects[i])
        c.rects_t[i].draw()
    count += 1
    if count % 10 == 0:
        dum = 1
            
          
                
        
    pg.display.flip() 
    clock.tick(60)