from bird import *
from pipe import *
from pygame_functions import *
from nn import *
#from ga import nextGeneration, TOTAL
from os import system
#screenRefresh=False
setAutoUpdate(False)
TOTAL = 500

birds = []
savedBirds = []
pipes = []
count = 0
cycles = 1
generation = 1

def setup():
    global birds
    global pipes

    
    screenSize(400, 600)
    setBackgroundImage("background.png")
    pipes.append(Pipe())

    for i in range(TOTAL):
        birds.append(Bird())
    
    
def draw():
    
    updateDisplay()
    clearShapes()
    
    global count
    global pipes
    global savedBirds
    global birds
    global cycles
    
    
    
    for n in range(cycles):
        for i in range((len(pipes)-1), -1, -1):
            pipes[i].update()

            for j in range((len(birds)-1), -1, -1):
                if pipes[i].hits(birds[j]) or birds[j].y <= 0 or birds[j].y >= height:
                    savedBirds.append(birds.pop(j))
               
            if pipes[i].offscreen():
                pipes.pop(i)
            if keyPressed('right'):
                cycles += 1
                if cycles > 100:
                    cycles = 100
            elif keyPressed('left'):
                cycles -= 1
                if cycles < 1:
                    cycles = 1
                
        for bird in birds:
            bird.update()
            bird.think(pipes)
            
        if len(birds) == 0:
            birds = nextGeneration(savedBirds)
            savedBirds = []
            pipes = []
            pipes.append(Pipe())
            count = 0
          
        if count == 120:
            pipes.append(Pipe())
            count = 0

        
        count += 1
    
    #print(len(birds))    
    for pipe in pipes:
        pipe.show()

    for bird in birds:
        bird.show()
        
    
    





setup()
import random

def nextGeneration(sBirds):
    birds = []
    calculateFitness()
    for i in range(TOTAL):
        birds.append(pickOne(sBirds))
        
    return birds
    

def pickOne(birds):
    index = 0
    r = random.random()

    while r > 0:
        r -= savedBirds[index].fitness
        index += 1
        
    index -= 1

    bird = savedBirds[index]
    child = Bird(bird.brain)
    
    return child
        

def calculateFitness():
    
    sum = 0
    for bird in savedBirds:
        sum += bird.score
    
    for bird in savedBirds:
        bird.fitness = bird.score / sum
    
 
while True:
    
    updateShapes()
    draw()
    tick(60)
   
    
