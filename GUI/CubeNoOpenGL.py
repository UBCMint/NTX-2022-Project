"""
 Simulation of a rotating 3D Cube
 Developed by Leonel Machava <leonelmachava@gmail.com>

http://codeNtronix.com

"""
import sys, math, pygame
from operator import itemgetter

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)

    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)

    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)

    def dot(self, point):
        return self.x*point.x+self.y*point.y+self.z*point.z

    def magnitude(self):
        return (self.x*self.x+self.y*self.y+self.z*self.z)**0.5

    def scale(self, factor):
        return Point3D(self.x*factor,self.y*factor,self.z*factor)

    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        scale = 1
        if win_width>win_height: scale = win_height/1.5/520
        else: scale = win_width/1.5/780
        x = (self.x * factor) * scale + win_width / 2
        y = (-self.y * factor) * scale + win_height / 2
        return Point3D(x, y, self.z)

class Simulation:
    da = 0
    dsize = 0
    def __init__(self, win_width = 780, win_height = 520):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height), pygame.RESIZABLE)
        pygame.display.set_caption("Stimulus Window")

        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,-1,-1),
            Point3D(-1,-1,-1),
            Point3D(-1,1,1),
            Point3D(1,1,1),
            Point3D(1,-1,1),
            Point3D(-1,-1,1)
        ]

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        #                 z-        x+          z+      x-          y+      y-
        self.faces  = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]

        self.normals  = [Point3D(0,0,-1),Point3D(1,0,0),Point3D(0,0,1),Point3D(-1,0,0),Point3D(0,1,0),Point3D(0,-1,0)]

        # Define colors for each face
        self.colors = [(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)]

        self.angle = 0
        self.size = 1

    @classmethod
    def spin(self):
        Simulation.da = 3
    
    @classmethod
    def stop(self):
        Simulation.da = 0
        Simulation.dsize = 0

    @classmethod
    def grow(self):
        #Simulation.da = 0
        Simulation.dsize = 0.01

    @classmethod
    def shrink(self):
        #Simulation.da = 0
        Simulation.dsize = -0.01

    def run(self):
        """ Main Loop """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    

            self.clock.tick(50)
            self.screen.fill((0,0,0))

            # It will hold transformed vertices.
            t = []

            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle)
                s = r.scale(self.size)
                # Transform the point from 3D to 2D
                p = s.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
                t.append(p)

            # Calculate colors based on light source
            for i,n in enumerate(self.normals):
                l = Point3D(1,4,-4) #light source
                r = n.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle) #rotate normal
                intensity = 0.5+r.dot(l)/l.magnitude()*0.5
                self.colors[i] = (255*intensity,255*intensity,255*intensity)

            # Calculate the average Z values of each face.
            avg_z = []
            i = 0
            for f in self.faces:
                z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
                avg_z.append([i,z])
                i = i + 1

            # Draw the faces using the Painter's algorithm:
            # Distant faces are drawn before the closer ones.
            for tmp in sorted(avg_z,key=itemgetter(1),reverse=True):
                face_index = tmp[0]
                f = self.faces[face_index]
                pointlist = [(t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y),
                             (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y),
                             (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y),
                             (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y)]
                pygame.draw.polygon(self.screen,self.colors[face_index],pointlist)

            self.angle += Simulation.da
            self.size += Simulation.dsize
            if self.size > 1.8: self.size,Simulation.dsize = 1.8,0
            if self.size < 0.2: self.size,Simulation.dsize = 0.2,0
            pygame.display.flip()

