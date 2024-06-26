from OpenGL.GL import *
from OpenGL.GLU import *


G_OBJ_PLANE = 1
G_OBJ_SPHERE = 2
G_OBJ_CUBE = 3


def make_plane():
    glNewList(G_OBJ_PLANE, GL_COMPILE)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for i in xrange(41):
        glVertex3f(-10.0 + 0.5 * i, 0, -10)
        glVertex3f(-10.0 + 0.5 * i, 0, 10)
        glVertex3f(-10.0, 0, -10 + 0.5 * i)
        glVertex3f(10.0, 0, -10 + 0.5 * i)

    # These are the axes for cube
    glEnd()
    glLineWidth(5)

    glBegin(GL_LINES)
    glColor3f(0.5, 0.7, 0.5)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(5, 0.0, 0.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.5, 0.7, 0.5)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 5, 0.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.5, 0.7, 0.5)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 5)
    glEnd()

    # Drawing the Y-Axis
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)
    glVertex3f(0.0, 5.5, 0.0)
    glVertex3f(0.0, 5.5, 0.0)
    glVertex3f(-0.5, 6.0, 0.0)
    glVertex3f(0.0, 5.5, 0.0)
    glVertex3f(0.5, 6.0, 0.0)

    # Drawing the Z-Axis
    glVertex3f(-0.5, 0.0, 5.0)
    glVertex3f(0.5, 0.0, 5.0)
    glVertex3f(0.5, 0.0, 5.0)
    glVertex3f(-0.5, 0.0, 6.0)
    glVertex3f(-0.5, 0.0, 6.0)
    glVertex3f(0.5, 0.0, 6.0)

    # Drawing the X-Axis
    glVertex3f(5.0, 0.0, 0.5)
    glVertex3f(6.0, 0.0, -0.5)
    glVertex3f(5.0, 0.0, -0.5)
    glVertex3f(6.0, 0.0, 0.5)

    glEnd()
    glLineWidth(1)
    glEndList()


def make_sphere():
    glNewList(G_OBJ_SPHERE, GL_COMPILE)
    quad = gluNewQuadric()
    gluSphere(quad, 0.5, 30, 30)
    gluDeleteQuadric(quad)
    glEndList()


def make_cube():
    glNewList(G_OBJ_CUBE, GL_COMPILE)
    vertices = [((-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5)),
                ((-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5)),
                ((0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5)),
                ((-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)),
                ((-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5)),
                ((-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5))]
    normals = [(-1.0, 0.0, 0.0), (0.0, 0.0, -1.0), (1.0, 0.0, 0.0), (0.0, 0.0, 1.0), (0.0, -1.0, 0.0), (0.0, 1.0, 0.0)]

    glBegin(GL_QUADS)
    for i in xrange(6):
        glNormal3f(normals[i][0], normals[i][1], normals[i][2])
        for j in xrange(4):
            glVertex3f(vertices[i][j][0], vertices[i][j][1], vertices[i][j][2])
    glEnd()
    glEndList()


def init_primitives():
    make_plane()
    make_sphere()
    make_cube()

# NO ERRORS LETS GOOOOOOOOOOOOOOOOOOOOOOOO!!
