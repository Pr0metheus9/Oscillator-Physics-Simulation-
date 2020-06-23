from p5 import *
import matplotlib.pyplot as plt

width = 600
height = 500
x = []
t = []
i = 0

class Double_Pendulum:
    def __init__(self,r1,r2,m1,m2,a1,a2,a1_v,a2_v,a1_a,a2_a,g):
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
        self.px2 = -1
        self.py2 = -1
        self.cx = width / 2
        self.cy = height / 3
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def update(self):
        num1 = -self.g * (2 * self.m1 + self.m2) * sin(self.a1)
        num2 = -self.m2 * self.g * sin(self.a1 - 2 * self.a2)
        num3 = -2 * sin(self.a1 - self.a2) * self.m2
        num4 = self.a2_v * self.a2_v * self.r2 + self.a1_v * self.a1_v * self.r1 * cos(self.a1 - self.a2)
        den = self.r1 * (2 * self.m1 + self.m2 - self.m2 * cos(2 * self.a1 - 2 * self.a2))
        self.a1_a = (num1 + num2 + num3 * num4) / den

        num1 = 2 * sin(self.a1 - self.a2)
        num2 = self.a1_v * self.a1_v * self.r1 * (self.m1 + self.m2)
        num3 = self.g * (self.m1 + self.m2) * cos(self.a1)
        num4 = self.a2_v * self.a2_v * self.r2 * self.m2 * cos(self.a1 - self.a2)
        den = self.r2 * (2 * self.m1 + self.m2 - self.m2 * cos(2 * self.a1 - 2 * self.a2))
        self.a2_a = (num1 * (num2 + num3 + num4)) / den

        self.x1 = self.r1 * sin(self.a1)
        self.y1 = self.r1 * cos(self.a1)

        self.x2 = self.x1 + self.r2 * sin(self.a2)
        self.y2 = self.y1 + self.r2 * cos(self.a2)

    def move(self):
        self.a1_v += self.a1_a
        self.a2_v += self.a2_a
        self.a1 += self.a1_v
        self.a2 += self.a2_v

        self.px2 = self.x2
        self.py2 = self.y2

    def draw__pen(self):
        translate(self.cx, self.cy)
        stroke(0)
        stroke_weight(2)

        stroke('black')
        line((0, 0), (self.x1, self.y1))
        fill(0)
        stroke('blue')
        ellipse((self.x1, self.y1), self.m1, self.m1)

        stroke('black')
        line((self.x1, self.y1), (self.x2, self.y2))
        fill(0)
        stroke("red")
        ellipse((self.x2, self.y2), self.m2, self.m2)


pendulum = Double_Pendulum(125,125,10,10,PI/2,PI/2,0,0,0,0,1)

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

    i += 1

    print(i)

    if (i == 300):
        plt.plot(t, x)
        plt.show()


if __name__ == '__main__':
    run()


