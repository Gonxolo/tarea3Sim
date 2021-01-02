"""
# A class to store the application control
"""
import glfw
from sys import exit
import numpy as np

class Controller:
    def __init__(self):
        self.fillPolygon = True
        self.sunPos = np.zeros(3)
        self.rx = np.random.uniform(-0.005,0.005)
        self.ry = np.random.uniform(-0.005,0.005)
        self.rz = np.random.uniform(-0.005,0.005)
        self.bounds = (5.0,-5.0)
        self.followSun = False

    def updatePos(self, time):
        # update sun position
        self.sunPos[0] += self.rx
        self.sunPos[1] += self.ry
        self.sunPos[2] += self.rz
        if self.sunPos[0] >= self.bounds[0] or self.sunPos[0] <= self.bounds[1]:
            a = self.rx//abs(self.rx)
            self.rx = np.random.uniform(-0.05,0.05)
            b = self.rx//abs(self.rx)
            if a == b:
                self.rx *= -1
        if self.sunPos[1] > self.bounds[0] or self.sunPos[1] < self.bounds[1]:
            a = self.ry//abs(self.ry)
            self.ry = np.random.uniform(-0.05,0.05)
            b = self.ry//abs(self.ry)
            if a == b:
                self.ry *= -1
        if self.sunPos[2] > self.bounds[0] or self.sunPos[2] < self.bounds[1]:
            a = self.rz//abs(self.rz)
            self.rz = np.random.uniform(-0.05,0.05)
            b = self.rz//abs(self.rz)
            if a == b:
                self.rz *= -1

# we will use the global controller as communication with the callback function
ctrl = Controller()

def on_key(window, key, scancode, action, mods):

    if action != glfw.PRESS:
        return
    
    global ctrl

    if key == glfw.KEY_SPACE:
        ctrl.fillPolygon = not ctrl.fillPolygon

    elif key == glfw.KEY_ESCAPE:
        sys.exit()

    elif key == glfw.KEY_E:
        ctrl.followSun = not ctrl.followSun 

    else:
        print('Unknown key')


