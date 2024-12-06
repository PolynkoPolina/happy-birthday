import pygame as pg
import os
import random

pg.init()
pg.mixer.init()
clock = pg.time.Clock()
pg.display.set_caption("Happy Birthday Olegsha 😍😎")

WIDGHT = 800
HEIGHT = 800
FONT_SIZE = 50
LETTER_SIZE = FONT_SIZE + 10
PADDING = 10

screen = pg.display.set_mode((WIDGHT, HEIGHT))

words = [
    ["А второй куплет?"],
    ["Его пока что нет!"],
    ["И вам не повезло: щас будет набор слов"],
    ["Аэробика, четыре гомика"],
    ["Сплю я с пушкою под подушкою"],
    ["Спеют яблочки, светят лампочки"],
    ["Сила трения,"],
    [""],
    [""],
    ["С ДНЁМ РОЖДЕНИЯ!"],
    [""],
    ["Будешь рыпаться"],
    ["дам под дыхало"],
    ["Играет и поёт"],
    ["Валя Стрыкало"],
    ["Это — песня для девочек"],
    ["Чтобы девочки плакали."],
    ["Конец!"]
]


directory = os.path.dirname(__file__)
d =  directory + "\Валентин Стрыкало - Песня для девочек.mp3"

pg.mixer.music.load(d)
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play(start=83.0, fade_ms=153)

class Olan():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rects = []
        self.rects_t = []

class Solina():
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.font = pg.font.Font(None, FONT_SIZE)
        self.font_link = os.path.join(directory, "minecraft.ttf")
        self.shift = pg.font.Font(self.font_link, 50)
        self.text_shoft = self.shift.render(self.text, True, (0, 0, 0))

    def draw(self):
        screen.blit(self.text_shoft, self.pos)

c = Olan(20, 20)
current_letter_index = 0
flat_words = " ".join([" ".join(term) for term in words])

colors = []

def prepare_text():
    global c, flat_words, current_letter_index, m

    while current_letter_index < len(flat_words):
        letter = flat_words[current_letter_index]
        if c.y + LETTER_SIZE > HEIGHT:
            break

        if letter == " ":
            c.x = 20
            c.y += LETTER_SIZE + PADDING + 30
        else:
            cube = pg.Rect(c.x + 15, c.y, 60, 80)
            m = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            colors.append(m)
            text = Solina(letter, (cube.centerx - 15, cube.centery - 25))
            c.rects.append(cube)
            c.rects_t.append(text)
            c.x += LETTER_SIZE + PADDING

            if c.x + LETTER_SIZE >= WIDGHT + 5:
                c.x = 20
                c.y += LETTER_SIZE + PADDING

        current_letter_index += 1

prepare_text()

rect_index = 0

game = True


def reset_text():
    global c, rect_index
    c.x = 20
    c.y = 20
    c.rects = []
    c.rects_t = []
    rect_index = 0
    prepare_text()

drawn_rects = []  

def reset_text():
    global c, rect_index, drawn_rects
    c.x = 20
    c.y = 20
    c.rects = []
    c.rects_t = []
    rect_index = 0
    drawn_rects = [] 
    prepare_text()

while game:
    screen.fill((209, 191, 148))  

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False

    for i, rect in enumerate(drawn_rects):
        pg.draw.rect(screen, colors[i], rect)
        c.rects_t[i].draw()

    if rect_index < len(c.rects):
        rect = c.rects[rect_index]
        pg.draw.rect(screen, m, rect)
        c.rects_t[rect_index].draw()
        drawn_rects.append(rect) 
        rect_index += 1
    else:
        reset_text()

    pg.display.flip()
    clock.tick(3.5)

pg.quit()