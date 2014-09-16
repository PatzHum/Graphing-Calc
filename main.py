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

pts = []
grd = [(0,240),(640,240), (320,240),(320,0), (320,480)]

fn = ''
print "Type done when 'done' entering functions."
while fn != 'done':
    fn = raw_input("f(x)=")
    if fn == 'done':
        break
    mpr = 50

    # for i in range(0,int(640/mpr)+5):
    #     d = i*mpr-i+mpr
    #     grd.append((d, 0))
    #     grd.append((d,480))
    #     grd.append((d, 0))
    # for i in range(0,int(640/mpr)+5):
    #     d = i*mpr-i*2+mpr-2
    #     grd.append((640,d))
    #     grd.append((0,d))
    #     grd.append((640,d))

    for x in range(-1000,1001):
        x = float(x)/10
        pts.append((mpr*x+320, -mpr*solvefunc(fn,x)+240))
    print pts


pygame.init()
surface = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

while True:
    pygame.draw.lines(surface, (50,50,50), False, grd,2)
    pygame.draw.lines(surface, (255,255,255), False, pts, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(30)

raw_input()

