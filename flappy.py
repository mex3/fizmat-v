#please don't change this code

from time import sleep
from threading import Thread
from random import choice

HEIGHT = 30
WIDTH = 50
sleep_duration = 0.04
BIRD_X = WIDTH // 10
g = 0.1

highscore = 0
game_is_running = False

bsod = '\n' * 25 + '''A problem has been detected and Windows has been shut down to prevent damage
to your computer.

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED

If this is the first time you've seen this stop error screen,
restart your computer. If this screen appears again, follow
these steps:

Check to make sure any new hardware or software is properly installed.
If this is a new installation, ask your hardware or software manufacturer
for any Windows updates you might need.

If problems continue, disable or remove any newly installed hardware
or software. Disable BIOS memory options such as caching or shadowing.
If you need to use safe mode to remove or disable components, restart
your computer, press F8 to select Advanced Startup Options, and then
select Safe Mode.

Technical Information:

*** STOP: 0x1000007e (0xffffffffc0000005, 0xfffff80002e55151, 0xfffff880009a99d8, 
0xfffff880009a9230)''' + '\n' * 5

linux = '\n' * 25 + r'''
                          __-----___
                         /          \
                        /  _      __ \
                       |  | \    /_ | \
                       |  |()|  |( )| |
                       |  \_||__||/_| |
                       |  /        _\ |
                       | |       _/_| |
                       | |\\____/_/\   \
                      / /  \____/   |   \
                     / /             \   \
                    / |              | \  \
                   / //              |  |  |  
                  / ||               |  |  | 
                 /  ||     |         |  |  |
                 | | |     |         | /   /
                /__\_|     |        /_-- _/
               //  \ |     |       | |  | |
              |/    \ \    \       | |__/  \
              /      \ \_          |        |_
           ---        \__|        /|          )
          |            \_______--  |       __/
         _|             |          |      /
        /              /           |     /
        ---------_____/            \____/
        
''' + '\n' * 5
def f():
    global v
    while game_is_running:
        input()
        v = -1
        if game_is_running:
            redraw() 

def redraw():
    frame = '\n' * 100
    frame += str(score) + ' HIGHSCORE: ' + str(highscore) + '\n'
    frame += '-' * WIDTH + '\n'
    for y in range(HEIGHT):
        line = [' '] * WIDTH
        if y == h:
            line[BIRD_X] = '0'
        if y-barrier_y not in range(5):
            line[barrier_x] = '*'
        frame += ''.join(line)
        frame += '\n'
    print(frame, end = '')

while True:
    answer = input('\n' * 160 + ' ' * 17 + 'Start a new game?' + '\n' * 17)
    if answer != 'yes' and answer != 'Yes' and answer != 'y' and answer != 'Y' and answer != '':
        if answer == 'i like windows':
            sleep(2)
            print(bsod)
            while True:
                input()
                print(bsod)
        if answer == 'i like linux':
            print(linux)
            sleep(5)
            continue
        exit()
    v = 0
    h = HEIGHT // 2
    score = -1
    game_is_running = True
    
    t = Thread(target=f, daemon=True)
    t.start()
    
    while game_is_running:
        barrier_y = choice(range(HEIGHT - 6))  # Lower bound of the hole in the barrier
        score += 1
        highscore = max(score, highscore)
        for barrier_x in reversed(range(WIDTH)):
            redraw()
            if (barrier_x == BIRD_X and h-barrier_y not in range(5)) or h not in range(HEIGHT):
                game_is_running = False
                break
            sleep(sleep_duration)
            v += g
            h += v
            h = int(h)
    BIRD_X -= 1
    v1 = (v + abs(v)) // 2
    while h <= HEIGHT:
        redraw()
        sleep(sleep_duration)
        v1 += g
        h += v1
        h = int(h)
    BIRD_X += 1
    print('{}Game Over{}Your score: {}{}Highscore: {}{}'.format
    ('\n'*140 + ' '*20, '\n'*3 + ' '*18, score, '\n' + ' '*18, highscore, '\n' * 15))
    sleep(1)
    print('{}Game Over{}Your score: {}{}Highscore: {}{}Press Enter to continue{}'.format
    ('\n'*140 + ' '*20, '\n'*3 + ' '*18, score, '\n' + ' '*18, highscore, '\n'*3 + ' '*13, '\n' * 12))
    
