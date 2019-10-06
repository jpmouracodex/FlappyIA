import random

from pygame_functions import *

class Pipe:
    def __init__(self):
        spacing = 125

        centery = random.randint(spacing, height - spacing)
        
        self.top = centery - spacing // 2
        self.bottom = height - (centery + spacing // 2)
        self.x = width
        self.w = 80
        self.speed = 3

    def hits(self, bird):
        if bird.y < self.top or bird.y > height - self.bottom:
            if bird.x > self.x and bird.x < self.x + self.w:
                return True
        else:
            return False
    
    def show(self):
        drawRect(self.x, 0, self.w, self.top, (0,255,0))
        drawRect(self.x, height-self.bottom, self.w, self.bottom,(0,255,0))

    def update(self):
        self.x -= self.speed
        
    def offscreen(self):
        if self.x < -self.w:
            return True
        else:
            return False
##    def __str__(self):
##        return str(self.name)
