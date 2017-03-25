
Direction = {
    'UP': 0,
     'DOWN' : 4,
     'LEFT' : 6,
     'RIGHT' : 2,
     'UPLEFT' : 7,
     'UPRIGHT' : 1,
     'DOWNLEFT' : 5,
     'DOWNRIGHT' : 3,
}

     
class MovesChecker:
    def __init__(self, environment):
        self.environment = environment
        self.visited = set()
        self.visitedWithPowerUp = set()
        
    def availableMoves(self, position, havePowerUp):
        #position[0]:x
        #position[1]:y
        
        self.havePowerUp = havePowerUp
        
        #Iterate on toVisit positions
        self.visited.add(position)
        for x in self.tryAllMoves(position, [], havePowerUp, -1):
            yield x

    def tryAllMoves(self, position, directions, powerUpAvailable, usedPowerUpAtMove):    
        #todo check if arc is already taken
        
        neigh = set(self.environment.get_neighbours(position))
        all = set([     
            (position[0],  position[1]+1),
            (position[0],  position[1]-1),
            (position[0]-1,position[1])  ,
            (position[0]+1,position[1])  ,
            (position[0]-1,position[1]+1),
            (position[0]+1,position[1]+1),
            (position[0]-1,position[1]-1),
            (position[0]+1,position[1]-1) ])
        
        avail = all - neigh
        
        if (position[0],  position[1]+1) in avail :
            for x in  self.tryMove( (position[0],  position[1]+1), directions + [Direction['DOWN']], powerUpAvailable, usedPowerUpAtMove ):
                yield x
        if (position[0],  position[1]-1) in avail :
            for x in  self.tryMove( (position[0],  position[1]-1), directions + [Direction['UP']], powerUpAvailable, usedPowerUpAtMove ):
                yield x
        if (position[0]-1,position[1]) in avail :
            for x in  self.tryMove( (position[0]-1,position[1])  , directions + [Direction['LEFT']], powerUpAvailable, usedPowerUpAtMove ):
                yield x
        if (position[0]+1,position[1]) in avail :
            for x in  self.tryMove( (position[0]+1,position[1])  , directions + [Direction['RIGHT']], powerUpAvailable, usedPowerUpAtMove ):
                yield x
        if (position[0]-1,position[1]+1) in avail :
            for x in  self.tryMove( (position[0]-1,position[1]+1), directions + [Direction['DOWNLEFT']], powerUpAvailable, usedPowerUpAtMove ):
                yield x
        if (position[0]+1,position[1]+1) in avail :
            for x in  self.tryMove( (position[0]+1,position[1]+1), directions + [Direction['DOWNRIGHT']], powerUpAvailable, usedPowerUpAtMove ):
                yield x
        if (position[0]-1,position[1]-1) in avail :
            for x in  self.tryMove( (position[0]-1,position[1]-1), directions + [Direction['UPLEFT']], powerUpAvailable, usedPowerUpAtMove ):
                yield x
        if (position[0]+1,position[1]-1) in avail :
            for x in  self.tryMove( (position[0]+1,position[1]-1), directions + [Direction['UPRIGHT']], powerUpAvailable, usedPowerUpAtMove ):
                yield x

    def tryMove(self, position, directions, powerUpAvailable, usedPowerUpAtMove): #directions so far
        if(position[0] < 0 or position[0] > 14 or position[1] < 0 or position[1] > 14): 
            if not ( (position[0] == 7 and position[1] == -1) or (position[0] == 7 and position[1] == 15) ):
                return
                
        usedPowerUp = (not(powerUpAvailable) and self.havePowerUp)
                
        if(position in self.visited or (position in self.visitedWithPowerUp and usedPowerUp)):
            return
        
        if usedPowerUp:
            self.visitedWithPowerUp.add(position)
        else:
            self.visited.add(position)
        
        
        if(self.environment.is_visited(position)):
            for x in self.tryAllMoves(position, directions, powerUpAvailable, usedPowerUpAtMove):
                yield x
        else:
            yield (position, directions, usedPowerUp, usedPowerUpAtMove)
        
            if powerUpAvailable:
                for x in self.tryAllMoves(position, directions, False, len(directions)-1):
                    yield x

        
        
    