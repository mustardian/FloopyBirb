import pygame, random, time, csv
from pygame import mixer

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
print()


def notokiedokie():
    print('An error has been encountered')
    print('Trying to fix it')
    import requests
    print('Downloading missing file...')
    image_url = "https://scontent.fbom19-2.fna.fbcdn.net/v/t1.0-9/109080594_1465214536995353_661856612374309813_n.jpg?_nc_cat=104&_nc_sid=730e14&_nc_ohc=Sfx_SAY9LTQAX8Aex7H&_nc_ht=scontent.fbom19-2.fna&oh=a2e1918b1649045a8c911e7eef7b351b&oe=5F420788"
    img = requests.get(image_url)
    print(img.content)
    local_file = open('Files/floopy birb START.png', 'wb')
    local_file.write(img.content)
    print('Please restart or get the original files')


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
game_over = pygame.image.load('Files/game_over.png')
enter_name_text = pygame.image.load('Files/Enter your name.png')
play_again_bg = pygame.image.load('Files/play again.png')
space_to_restart = pygame.image.load('Files/spacebar to restart.png')
press_enter = pygame.image.load('Files/press enter.png')

try:
    start_screen = pygame.image.load('Files/floopy birb START.png')
    start_screen = pygame.transform.scale(start_screen, (960, 512))
except:
    notokiedokie()
# player
playerimg = pygame.image.load('Files/flappy birb.png')
playerimg = pygame.transform.scale(playerimg, (62, 50))
playerx = 200
playery = 250

# mario pipe
marioimg = pygame.image.load('Files/mario pipe.png')
marioimg = pygame.transform.scale(marioimg, (250, 450))
ivmarioimg = pygame.transform.rotate(marioimg, (180))
mariox = 850
marioy = 300


# mario visible
def mariopipe(x, ye, lastpipecoords=0):
    u = x
    for j in range(len(pipe_total)):
        screen.blit(pipe_total[j], (x[j], ye[j]))
    if j == len(pipe_total) - 1:
        lastpipecoords = x[j]
    for je in range(len(pipe_totalinv)):
        screen.blit(pipe_totalinv[je], (x[je], (ye[je] - 600)))
    return lastpipecoords


# player visible
def player(x, y):
    screen.blit(playerimg, (x, y))


# collision check
def collision(playerx, playery, pipX, pipY, pipYinv, x):
    gems = False
    yems = False
    kems = False
    global points_to_be_earned
    y, z = pipX[x] + 250, pipX[x] - 30
    if playerx in range(z, y + 1):
        # print('COLISION DETECTED ON X')
        gems = True

    b, v = pipY[x] + 250, pipY[x] - 30
    if playery in range(v, b + 1):
        # print('COLISION DETECTED ON Y')
        yems = True

    i, o = pipYinv[x] + 30, pipYinv[x] - 250
    if playery in range(o, i + 1):
        # print('COLISION DETECTED ON Y INV')
        kems = True
    if gems and (yems or kems) == True:
        # print("You hit a metal pipe!")
        chems = True
    else:
        chems = False
    return chems


# Checks if player passed through pipe
def passed_through_check(pipX, x):
    if playerx > pipX[x] + 250:
        x += 1
    return x


# Shows Score at top left
def showscore(x):
    x = font.render("Score :" + str(x), True, (255, 255, 255))
    screen.blit(x, (5, -5))


# music
def main_menu_music(uwu):
    if uwu:
        mixer.Channel(0).play(mixer.Sound('Files/start_music.wav'))


def player_jumped(uwu):
    if uwu:
        mixer.Channel(0).play(mixer.Sound('Files/floopy_jump.wav'))


def game_music(uwu):
    if uwu:
        mixer.Channel(1).play(mixer.Sound('Files/kawaii music_01.wav'))
    else:
        mixer.Channel(1).pause()


# speed and defaults
playery_change = 0  # default
playerx_change = 0  # default
mariox_def = 850  # default
marioy_def = 300  # default
font = pygame.font.SysFont('Comic Sans MS', 28)  # Score Font
font_high = pygame.font.SysFont('Bahnschrift', 28)  # High Score Font
font_last = pygame.font.SysFont('Arial', 28)
bgX_loc = 0
bgY_loc = 0
bg_speed = 0.1
def_speed = 5  # birb jump
def_grav = 2  # gravity
diff_speed = 1  # enemy speed
def_speedfall = 3  # speed fall
player_rotation = 0  # rotation please work
DeltaDistMario = 500  # Distance between pipes
a = 300  # i forgot what this does
points_to_be_earned = 0
lastpipecoords = -260
time_before = 0
diff_check = 0
name = ''
jump_stopper = True
LAST = True  # Last pipe hit
PAUSED = False  # If paused
PIPE_CROSSED = False
START = True  # If not started
FREEROAM = False  # DEBUG
running = True  # runs the game
game_end = False  # ends the game
play_again = True  # repeats
restart = True  # causes the restart
music_started = True  # starts game music
enter_name = True  # enters the name
comedi = []
clock=pygame.time.Clock()
# start loop
screen3 = pygame.display.set_mode((960, 512))
while enter_name:
    # CLOSE CHECK
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            enter_name = False
            once_more = False
            play_again = False
            START = False
            game_end = True
            running = False
            restart = False
        if x.type == pygame.KEYDOWN:
            if x.key != pygame.K_RETURN and x.key != pygame.K_BACKSPACE and x.key != pygame.K_ESCAPE and x.key != pygame.K_SPACE and x.key!= pygame.K_COMMA and x.key!=pygame.K_COLON and x.key!=pygame.K_BACKQUOTE and x.key!=pygame.K_PERIOD and x.key!=pygame.K_EXCLAIM:
                name += x.unicode
            elif x.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif x.key == pygame.K_RETURN and len(name)>2:
                enter_name = False
            elif x.key == pygame.K_ESCAPE:
                enter_name = False
                once_more = False
                play_again = False
                START = False
                game_end = True
                running = False
                restart = False

    # BG
    screen.blit(background, (0, 0))
    text = font_high.render(name, True, (0, 0, 0))
    screen.blit(text, (400, 300))
    screen.blit(enter_name_text, (0, 0))
    if len(name) > 2:
        screen.blit(press_enter, (0, 0))
    pygame.display.update()
while restart:
    # values req for reset
    start1 = time.time()
    main_menu_music(START)
    playerx = 200
    playery = 250
    playery_change = 0  # default
    playerx_change = 0  # default
    mariox_def = 850  # default
    marioy_def = 300  # default
    font = pygame.font.SysFont('Comic Sans MS', 28)  # Score font
    bgX_loc = 0
    bgY_loc = 0
    bg_speed = 0.1
    def_speed = 5  # birb jump
    def_grav = 2  # gravity
    diff_speed = 1  # enemy speed
    def_speedfall = 3  # speed fall
    player_rotation = 0  # rotation please work
    DeltaDistMario = 500  # Distance between pipes
    a = 300  # idk what this is please don't change
    points_to_be_earned = 0
    lastpipecoords = -260
    time_before = 0
    diff_check = 0
    jump_stopper = True
    LAST = True  # Last pipe hit
    PAUSED = False  # If paused
    PIPE_CROSSED = False
    music_started = True  # starts game music
    comedi = []
    # values req for reset

    while START:
        screen3.blit(start_screen, (0, 0))
        start2 = time.time()
        uwuwu = int(start2 - start1)
        if uwuwu % 2 != 0:
            screen3.blit(press_spacebar, (700, 200))
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                once_more = False
                play_again = False
                START = False
                game_end = True
                running = False
                restart = False
            if x.type == pygame.KEYDOWN:
                if x.key == pygame.K_SPACE:
                    START = False
                elif x.key == pygame.K_ESCAPE:
                    once_more = False
                    play_again = False
                    START = False
                    game_end = True
                    running = False
                    restart = False
        pygame.display.update()

    score_initial = time.time()  # initial time
    game_music(music_started)  # starts game music
    # game loop
    while running:
        clock.tick(120)
        # CLOSE CHECK
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                once_more = False
                play_again = False
                START = False
                game_end = True
                running = False
                restart = False
        # BG
        screen.blit(background, (int(bgX_loc), int(bgY_loc)))

        # Checks if req to add more pipes
        if lastpipecoords < -300:
            diff_check += 1
            if diff_speed <= 10 and diff_check == 3:
                diff_speed += 1
                bg_speed += 0.05
                diff_check = 0
            LAST = True

        # Adds a random amount of pipes
        if LAST:
            u = []
            pipe_total = []
            pipe_totalinv = []
            pipe_totalX = []
            pipe_totalY = []
            pipe_totalYinv = []
            r = 0
            r = random.randrange(1, 5)
            pipes_passed_per_level = 0
            for hhh in range(r):
                u = random.randrange(100, 500)
                pipe_totalY.append(u)
                u -= 190
                pipe_totalYinv.append(u)
                pipe_total.append(marioimg)
                pipe_totalinv.append(ivmarioimg)
                pipe_totalX.append(mariox)
                mariox += DeltaDistMario
            mariox = mariox_def
            marioy = marioy_def
            LAST = False
        if r == pipes_passed_per_level:  # resets pipes
            pipes_passed_per_level = 0

        # Pipe movement
        for i in range(len((pipe_totalX))):
            pipe_totalX[i] -= diff_speed
            pipe_totalX[i] = int(pipe_totalX[i])
            bgX_loc -= bg_speed
            if bgX_loc < -425:
                bgX_loc = 0
        lastpipecoords = mariopipe(pipe_totalX, pipe_totalY, lastpipecoords)

        # Collison check
        ay = collision(playerx, playery, pipe_totalX, pipe_totalY, pipe_totalYinv, pipes_passed_per_level)
        pipes_passed_per_level = passed_through_check(pipe_totalX, pipes_passed_per_level)

        # Game over check
        if ay == True:
            mixer.music.load('Files/metal_bonk.wav')
            mixer.music.play()
            time.sleep(0.8)
            break
        # BORDERS
        if playery >= 450:
            # print('You flew too low')
            break
        elif playery <= 0:
            playery = 0
        # Change in Player
        player(playerx, playery)
        playery += playery_change
        playerx += playerx_change
        # PLAYER CONTROLS
        if x.type == pygame.KEYDOWN:
            if x.key == pygame.K_SPACE or x.key == pygame.K_UP:
                playery_change = -def_speed
                jump_stopper = True
            elif x.key == pygame.K_s or x.key == pygame.K_DOWN:
                playery_change = def_speedfall
            if FREEROAM:
                if x.key == pygame.K_d:
                    playerx_change = 5
                elif x.key == pygame.K_a:
                    playerx_change = -5
                elif x.key == pygame.K_ESCAPE:
                    break
                elif x.key == pygame.K_g:
                    diff_speed = 0
                elif x.key == pygame.K_h:
                    diff_speed = 1
                def_grav = 0
        elif x.type == pygame.KEYUP:
            player_jumped(jump_stopper)
            playery_change = 0
            playerx_change = 0
            jump_stopper = False
        playery += def_grav

        # Score tally
        score_final = time.time()
        actual_score = int(score_final - score_initial)
        showscore(actual_score)
        pygame.display.update()

    if not game_end:
        music_started = False
        game_music(music_started)
        mixer.music.load('Files/game_over_song.wav')
        mixer.music.play()
    # game ender
    koyo = time.time()
    screen2 = pygame.display.set_mode((960, 512))
    while not game_end:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                once_more = False
                play_again = False
                START = False
                game_end = True
                running = False
                restart = False
        screen2.blit(background, (int(bgX_loc), int(bgY_loc)))
        screen2.blit(game_over, (0, 0))
        moyo = time.time()
        yeye = moyo - koyo
        if yeye >= 5:
            game_end = True
        pygame.display.update()

    # Score Checker
    try:
        with open('Files/Leaderboard.csv', 'a') as leaderboard:
            l_writer = csv.writer(leaderboard)
            l_writer.writerow([name, actual_score])
    except NameError:
        actual_score = 0
        with open('Files/Leaderboard.csv', 'a') as leaderboard:
            l_writer = csv.writer(leaderboard)
            l_writer.writerow([name, actual_score])

    with open('Files/Leaderboard.csv', 'r') as leaderboard:
        l_reader = csv.reader(leaderboard, delimiter=',')
        highest_score = 0
        highest = ''
        for row in l_reader:
            if not row == [] and not row[1] == 'Score':
                if int(row[1]) > highest_score:
                    highest_score = int(row[1])
                    highest = row[0]
    # Last Screen
    screen4 = pygame.display.set_mode((960, 512))
    start00 = time.time()
    while play_again:

        # finds high score
        with open('Files/Leaderboard.csv', 'r') as leaderboard:
            l_reader = csv.reader(leaderboard, delimiter=',')
            highest_score = 0
            highest = ''
            for row in l_reader:
                row.sort()
                if not row == [] and not row[1] == 'Score':
                    if int(row[0]) > highest_score:
                        highest_score = int(row[0])
                        highest = row[1]
            moyoyo = ('High score ' + str(highest_score) + ' by ' + str(highest))

        # sorts all scores and puts them in a list
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
        no_list = []
        for mm in chottomatte:
            for uu in mm.split():
                if uu.isdigit():
                    no_list.append(uu)
        op = len(chottomatte)
        for i in range(op - 1):
            for j in range(0, op - i - 1):
                if int(no_list[j]) > int(no_list[j + 1]):
                    no_list[j] = int(no_list[j])
                    no_list[j + 1] = int(no_list[j + 1])
                    no_list[j], no_list[j + 1] = no_list[j + 1], no_list[j]
                    chottomatte[j], chottomatte[j + 1] = chottomatte[j + 1], chottomatte[j]
        chottomatte = chottomatte[::-1]
        chottomatte = chottomatte[1:-1]

        scoreX = 599
        scoreY = 100
        screen4.blit(play_again_bg, (0, 0))

        # space to restart
        startkk = time.time()
        uwuwu = int(startkk - start00)
        if uwuwu % 2 != 0:
            screen4.blit(space_to_restart, (5, 0))

        # displays high score
        moyoyo = font_high.render(moyoyo, True, (0, 0, 0))  # renders high scrore
        screen4.blit(moyoyo, (599, 50))

        # displays scores following high score
        hjk=0
        while hjk <3:
            okokok = font_last.render(chottomatte[hjk], True, (0, 0, 0))
            screen4.blit(okokok, (scoreX, scoreY))
            scoreY += 50
            hjk+=1
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                once_more = False
                play_again = False
                START = False
                game_end = True
                running = False
                restart = False
            if x.type == pygame.KEYDOWN:
                if x.key == pygame.K_SPACE:
                    START = True
                    game_end = False
                    running = True
                    restart = True
                    play_again = False
                    once_more = True
                elif x.key == pygame.K_ESCAPE:
                    play_again = False
                    START = False
                    game_end = True
                    running = False
                    restart = False
                    once_more = False
        pygame.display.update()
    if once_more:
        play_again = True
    else:
        play_again = False
print("Thank you for playing Floopy Birb by Aryan Mishra")
