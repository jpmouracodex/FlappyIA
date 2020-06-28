import random
#from main import *
from bird import Bird
TOTAL = 500

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
        

def calculateFitness(sBirds):
    
    sum = 0
    for bird in sBirds:
        sum += bird.score
    
    for bird in sBirds:
        bird.fitness = bird.score / sum
    
 








