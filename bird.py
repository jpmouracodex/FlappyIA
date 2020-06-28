#from game import *
from pygame_functions import *
from nn import *

class Bird():
    def __init__(self, brain=None):
        self.y = height//2
        self.x = 64
        #self.sprite = makeSprite("bird.png")
        self.gravity = 0.6
        self.velocity = 0
        self.lift = -4
        mutation = 0.1
        
        if isinstance(brain, NeuralNetwork):
            self.brain = brain.copy()
            self.brain.mutate(mutation)
        else:
            self.brain = NeuralNetwork(4, 4, 2)
            
        self.score = 0
        self.fitness = None
        
        
    def show(self): 
        drawEllipse(self.x, self.y, 22, 22, (255,0,255))
        #moveSprite(self.sprite, self.x, self.y)
        #showSprite(self.sprite)
        
    def think(self, pipes):

        closest = None
        closestD = float("inf")
        for i in range(len(pipes)):
            d = (pipes[i].x + pipes[i].w) - self.x
            if d < closestD and d > 0:
                closest = pipes[i]
                closestD = d
        
        inputs = []
        
        inputs.append(self.y / height)
        inputs.append(closest.top / height)
        inputs.append(closest.bottom / height)
        inputs.append(closest.x / width)
        
        output = self.brain.predict(inputs)
 
        if output[0] > output[1]:
            self.up()

        
    def update(self):
        
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity
        
        self.score += 1
        

    
    def up(self):
        self.velocity += self.lift
        
