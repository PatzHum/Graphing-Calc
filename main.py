import pygame
import oop
import sys
from pygame import gfxdraw

def solvefunc(function, x):
    if x == 0:
        x += 0.001
    while 'x' in function:
        for i,j in enumerate(function):
            if j == 'x':
                function = function [:i] + str(x) + function [i+1:]
                break
    try:
        return float(oop.bedmas(function)[0])
    except ValueError:
        return 0


functions = []
mpr = 50
grd = [(0,240),(640,240), (320,240),(320,0), (320,480)]
pygame.font.init()
myfont = pygame.font.SysFont("courier new", 10)
fn = ''
print "operators: \n * for multiply \n / for divide \n - for subtraction \n + for addition \n | for abs (only on left side of x \n & for square root \nAlso remember that you must explicity declare each operation, no hocus pocus 3x instead of 3*x"
print "Type done when 'done' entering functions."
while fn != 'done':
    fn = raw_input("f(x)=")
    if fn == 'done':
        break
    elif fn == 'tov':
        for fn in functions:
            for x in range(-1000,1001):
                x = float(x)/100
                print x, solvefunc(fn, x)
    functions.append(fn)

pygame.init()
surface = pygame.display.set_mode((640,480))

pygame.display.set_caption(str(functions))
clock = pygame.time.Clock()

update = True
while True:
    ## generates points based on multiplier and functions
    screen = pygame.Surface((640,480))
    if update == True:
        for fn in functions:
            for x in range(-1000,1001):
                x = float(x)/mpr/2
                screen.set_at((int(mpr*x+320), int(-mpr*solvefunc(fn, x)+240)),(255,255,255))

        pygame.draw.lines(screen, (50,50,50), False, grd,2)

        surface.blit(screen,(0,0))
        for i in range(-60,70):
            i = round(float(i)/(mpr/50),2)
            lbl = myfont.render("-"+"("+str(i)+")", 1, (255,255,255))
            surface.blit(pygame.transform.rotate(lbl,-90), (i*640/12*(mpr/50)+313, 240))
            surface.blit(lbl, (320, -i*640/12*(mpr/50)+236))

        update = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                mpr *= 1.1
                update = True
            if event.button == 5:
                mpr *= 1/1.1
                update = True

    pygame.display.update()

    clock.tick(10)

raw_input()

