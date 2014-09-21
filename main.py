import pygame
import oop
import sys

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
myfont = pygame.font.SysFont("monospace", 11)
fn = ''
print "Type done when 'done' entering functions."
while fn != 'done':
    fn = raw_input("f(x)=")
    if fn == 'done':
        break
    functions.append(fn)

pygame.init()
surface = pygame.display.set_mode((640,480))
pygame.display.set_caption(str(functions))
clock = pygame.time.Clock()

update = True
while True:
    ## generates points based on multiplier and functions
    pts = []
    screen = pygame.Surface((640,480))
    if update == True:
        for fn in functions:
            for x in range(-1000,1001):
                x = float(x)/10
                pts.append((mpr*x+320, -mpr*solvefunc(fn, x)+240))

        pygame.draw.lines(screen, (50,50,50), False, grd,2)
        pygame.draw.lines(screen, (255,255,255), False, pts, 1)
        surface.blit(screen,(0,0))
        for i in range(-6,7):
            lbl = myfont.render(str(i), 1, (255,255,255))
            surface.blit(lbl, (i*640/12*(mpr/50)+318, 240))

        update = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                mpr *= 2
                update = True
            if event.button == 5:
                mpr *= 0.5
                update = True

    pygame.display.update()

    clock.tick(10)

raw_input()

