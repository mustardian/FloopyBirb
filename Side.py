import pygame, random, time, csv
from pygame import mixer
pygame.init()
'''
# screen res
screen = pygame.display.set_mode((960, 512))
# Title
pygame.display.set_caption('Floopy Birb')

# icon
ICON = pygame.image.load('Files/flappy birb.png')
pygame.display.set_icon(ICON)

# background
background = pygame.image.load('Files/floopy birb bg.png')
background = pygame.transform.scale(background, (1280, 512))
press_spacebar = pygame.image.load('Files/press spacebar.png')
press_spacebar = pygame.transform.scale(press_spacebar, (240, 128))
name='yeye'
arialfont = pygame.font.SysFont('Bahnschrift', 28)
running=True

while running:

    # CLOSE CHECK
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            once_more = False
            play_again = False
            START = False
            game_end = True
            running = False
            restart = False

        if x.type==pygame.KEYDOWN:
            if x.key!=pygame.K_KP_ENTER and x.key!=pygame.K_BACKSPACE:
                name+=x.unicode
            elif x.key==pygame.K_BACKSPACE:
                name=name[:-1]
    # BG COLOR

    # BG
    screen.blit(background, (0, 0))
    text=arialfont.render(name,True,(0,0,0))
    screen.blit(text,(0,0))

    pygame.display.update()
'''
'''
N=int(input('Enter number of data'))
eeee=[]
for i in range(N):
    for i in range(i):
        uwu=input('enter : ')
        eeee.append(uwu)
    kems=tuple(eeee)
    print(kems)
'''
'''
with open('Files/Leaderboard.csv', 'r') as leaderboard:
    l_reader = csv.reader(leaderboard, delimiter=',')
    highest_score = 0
    highest = ''
    for row in l_reader:
        row.sort()
        if not row == [] and not row[1] == 'Score':
            if int(row[0]) > highest_score:
                highest_score = int(row[0])
with open('Files/Leaderboard.csv', 'r') as leaderboard2:
    l_reader2 = csv.reader(leaderboard2, delimiter=',')
    emppy = []
    chottomatte = []
    for row2 in l_reader2:
        if row2 != [] and row2[0] != 'Name':
            row2[0], row2[1] = row2[1], row2[0]
            emppy.append(row2)
            for x in emppy:
                chottomatte.append((x[1] + ' has scored ' + x[0]))
chottomatte = list(dict.fromkeys(chottomatte))
no_list=[]
for mm in chottomatte:
    for uu in mm.split():
        if uu.isdigit():
            no_list.append(uu)
op=len(chottomatte)
for i in range(op-1):
    for j in range(0,op-i-1):
        if int(no_list[j])>int(no_list[j+1]):
            no_list[j]=int(no_list[j])
            no_list[j+1]=int(no_list[j+1])
            no_list[j],no_list[j+1]=no_list[j+1],no_list[j]
            chottomatte[j],chottomatte[j+1]=chottomatte[j+1],chottomatte[j]
chottomatte=chottomatte[::-1]
chottomatte=chottomatte[1:-1]
for u in chottomatte:
    print(u)
'''