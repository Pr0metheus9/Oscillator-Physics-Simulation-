from p5 import *
import matplotlib.pyplot as plt

width = 600
height = 500
x = []
t = []
i = 0

class Timoshenko_Oscillator:
    def __init__(self,l,m1,g,mu):
        self.l = l
        self.m1 = m1
        self.g = g
        self.mu = mu
        self.cx = width / 2
        self.cy = height / 2
        self.x = 0
        self.v = 5
        self.a = 0

    def update(self):
        self.a = -(2*self.g*self.mu*self.x)/self.l
        print(self.v)

    def move(self):
        self.v += self.a
        self.x += self.v

    def draw__pen(self):
        translate(self.cx, self.cy)
        stroke(0)
        stroke_weight(2)
        fill(0)
        stroke('green')
        rect((self.x, 0), 130, self.m1)

oscillator = Timoshenko_Oscillator(125,10,1,0.1)

def setup():
    size(width, height)

def draw():
    global i

    background(175)

    oscillator.update()

    oscillator.draw__pen()

    oscillator.move()

    t.append(i)
    x.append(oscillator.x)

    i+=1

    print(i)

    if(i == 300):
        plt.plot(t,x)
        plt.show()

while True:
    if __name__ == '__main__':
        run()
