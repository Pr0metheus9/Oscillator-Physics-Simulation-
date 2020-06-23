from p5 import *
import matplotlib.pyplot as plt

width = 600
height = 500
x = []
t = []
i = 0

class Spring_Pendulum:
    def __init__(self,r1,m1,a1,a1_v,a1_a,g):
        self.r1 = r1
        self.m1 = m1
        self.a1 = a1
        self.a1_v = a1_v
        self.a1_a = a1_a
        self.g = g
        self.k = 0.3
        self.px2 = -1
        self.py2 = -1
        self.cx = width / 2
        self.cy = height / 3
        self.x1 = 0
        self.y1 = 0
        self.x = 0
        self.x_a = 0
        self.x_v = 0

    def update(self):
        try:
            self.x_a = (self.r1+self.x)*self.a1_v*self.a1_v - (self.k/self.m1)*self.x + self.g*cos(self.a1)
            self.a1_a = -(self.g/(self.r1+self.x))*sin(self.a1) - ((2*self.x_v)/(self.r1+self.x))*self.a1_v

            self.x1 = (self.r1 + self.x) * sin(self.a1)
            self.y1 = (self.r1+self.x) * cos(self.a1)

        except:
            print("a1: ", self.a1)
            exit()

    def move(self):
        self.x_v += self.x_a
        self.x += self.x_v
        self.a1_v += self.a1_a
        self.a1 += self.a1_v

        #self.a1_v *= 0.99

    def draw__pen(self):
        translate(self.cx, self.cy)
        stroke(0)
        stroke_weight(2)

        line((0, 0), (self.x1, self.y1))
        fill(0)
        stroke('purple')
        ellipse((self.x1, self.y1), self.m1, self.m1)


pendulum = Spring_Pendulum(125,10,PI/3,0,0,1)

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

    if(i == 300):
        plt.plot(t,x)
        plt.show()

while True:
    if __name__ == '__main__':
        run(None,None,30)
