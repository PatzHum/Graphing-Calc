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
        return oop.bedmas(function)[0]
    except ValueError:
        return 0


functions = []
mpr = 50
grd = [(0,240),(640,240), (320,240),(320,0), (320,480)]

fn = ''
print "Type done when 'done' entering functions."
while fn != 'done':
    fn = raw_input("f(x)=")
    if fn == 'done':
        break
    functions.append(fn)


pygame.init()
surface = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

while True:
    pts = []
    for fn in functions:
        for x in range(-1000,1001):
            x = float(x)/10
            pts.append((mpr*x+320, -mpr*solvefunc(fn,x)+240))

    pygame.draw.lines(surface, (50,50,50), False, grd,2)
    pygame.draw.lines(surface, (255,255,255), False, pts, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mpr += 1
            if event.key == pygame.K_MINUS:
                mpr -= 1
    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)

raw_input()

