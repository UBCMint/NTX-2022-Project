import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import *

isInit = False
drx,dry = (0,0)

def changeRotation(nrx, nry):
    global drx,dry
    drx,dry=nrx,nry

class cubeWindow():
    def __init__(self) -> None:
        pygame.init()
        viewport = (780,520)
        srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)


        glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.7, 0.7, 0.7, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
        glEnable(GL_LIGHT0)

        obj = OBJ("GUI/Assets/box.obj", swapyz=True)
        obj.generate()

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        width, height = viewport
        gluPerspective(90.0, width/float(height), 1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        clock = pygame.time.Clock()
        rx, ry = (0,0)
        zpos = 3
        while 1:
            clock.tick(30)
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                elif e.type == KEYDOWN and e.key == K_ESCAPE:
                    sys.exit()

            rx+=drx
            ry+=dry

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            # RENDER OBJECT
            glTranslate(0,0,-zpos)
            glRotate(ry, 1, 0, 0)
            glRotate(rx, 0, 1, 0)
            obj.render()

            pygame.display.flip()
    