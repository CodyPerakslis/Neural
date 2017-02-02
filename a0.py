from random import uniform, randint
import numpy as np
from math import ceil
#import matplotlib.pyplot as plt
from time import sleep

class Preceptron(object):
    def __init__(self,inputsize=2):
        self.weights = [uniform(-1,1) for i in range(inputsize+1)]
        self.alpha = .01

    def activate(self, s):
        if s > 0: return 1
        return -1

    def feedforward(self,inputs):
        end = 0.0
        for i in range(len(inputs)):
            end += inputs[i]*self.weights[i]
        end += self.weights[-1]
        return self.activate(end)

    def train(self, inputs, desired, alp):
        guess = self.feedforward(inputs)
        error = desired - guess
        for i in range(len(inputs)):
            self.weights[i] += alp * error * inputs[i]
        self.weights[-1] += alp * error

def test(r=20):
    v = uniform(-1,1)
    goal = lambda x: v*x
    #g_x = np.linspace(-50,50, 200)
    #g_y = [goal(x) for x in g_x]

    #plt.plot(g_x, g_y)

    p = Preceptron()
    #hit = [[],[]]
    #miss = [[],[]]
    #C_h = [0,.6,.3]
    #C_m = [.9,0,.3]

    def draw(p, hit=0, miss=0):
        scores = 0
        for i in range(1000):
            x = randint(-50, 50)
            y = randint(-40, 70)
            a = p.feedforward([x,y])
            ans = -1
            if y > goal(x): ans = 1
            if a == ans: scores += 1
            """
            if a == 1:
                hit[0].append(x)
                hit[1].append(y)
            else:
                miss[0].append(x)
                miss[1].append(y)
            """
        return scores/10

    for i in range(r):
        #hit = [[],[]]
        #miss = [[],[]]
        #sc = draw(p, hit, miss)
        #plt.scatter(hit[0], hit[1], c=C_h)
        #plt.scatter(miss[0], miss[1], c=C_m)
        #plt.draw()
        #plt.pause(.001)
        x = randint(-50, 50)
        y = randint(-40, 70)
        ans = -1
        if y > goal(x): ans = 1
        p.train([x,y], ans, r/(10*(r+i)))
        #sleep(.5)
        #print(i, str(sc)+"%")
        #plt.clf()
        #plt.plot(g_x, g_y)


    sc = draw(p)
    #print("END", str(sc)+"%")
    #plt.scatter(hit[0], hit[1], c=C_h)
    #plt.scatter(miss[0], miss[1], c=C_m)
    #plt.show()
    return sc
for i in range(5):
    S = 0
    z = 10**i
    for i in range(200):
        S += test(z)
    print(z, round(S/200,2))
