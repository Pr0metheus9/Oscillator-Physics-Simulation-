from p5 import *
import matplotlib.pyplot as plt

width = 600
height = 500
x = []
t = []
i = 0

class Coupled_Pendulum:
    def __init__(self,r1,r2,m1,m2,a1,a2,a1_v,a2_v,a1_a,a2_a,g,k):
        self.r1 = r1
        self.r2 = r2
        self.m1 = m1
        self.m2 = m2
        self.a1 = a1
        self.a2 = a2
        self.a1_v = a1_v
        self.a2_v = a2_v
        self.a1_a = a1_a
        self.a2_a = a2_a
        self.g = g
        self.k = k
        self.px2 = -1
        self.py2 = -1
        self.cx = width / 2
        self.cy = height / 3
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def update(self):
        num1 = sin(self.a1)*(self.m1*(self.r1*self.a1_v*self.a1_v - self.g) - self.k*self.r1)
        num2 = self.k*self.r2*sin(self.a2)
        dem = self.m1*self.r1*cos(self.a1)
        self.a1_a = (num1+num2)/dem

        num1 = sin(self.a2) * (self.m2 * (self.r2 * self.a2_v * self.a2_v - self.g) - self.k * self.r2)
        num2 = self.k * self.r1 * sin(self.a1)
        dem = self.m2 * self.r2 * cos(self.a2)
        self.a2_a = (num1 + num2) / dem

        self.x1 = self.r1 * sin(self.a1)
        self.y1 = self.r1 * cos(self.a1)

        self.x2 = self.r2 * sin(self.a2)
        self.y2 = self.r2 * cos(self.a2)

    def move(self):
        self.a1_v += self.a1_a
        self.a2_v += self.a2_a
        self.a1 += self.a1_v
        self.a2 += self.a2_v

    def draw__pen(self):
        translate(self.cx, self.cy)
        stroke(0)
        stroke_weight(2)

        line((0, 0), (self.x1, self.y1))
        fill(0)
        ellipse((self.x1, self.y1), self.m1, self.m1)

        line((0, 0), (self.x2, self.y2))
        fill(209)
        ellipse((self.x2, self.y2), self.m2, self.m2)

        line((self.x1, self.y1), (self.x2, self.y2))

pendulum = Coupled_Pendulum(125,125,10,10,PI/3,PI/4,0,0,0,0,1,0.1)

def setup():
    size(width, height)

def draw():
    global i

    background(175)

    pendulum.update()

    pendulum.draw__pen()

    pendulum.move()

    t.append(i)
    x.append(pendulum.x1)

    i+=1

    print(i)

    if (i == 200):
        plt.plot(t, x)
        plt.show()

if __name__ == '__main__':
    run()

