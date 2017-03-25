from enum import Enum
class Direction(Enum):
     UP = 1
     DOWN = 2
     LEFT = 3
     RIGHT = 4
     UPLEFT = 5
     UPRIGHT = 6
     DOWNLEFT = 7
     DOWNRIGHT = 8

class MovesChecker:
    def __init__(self, environment):
        self.environment = environment
        self.visited = set()
        
    def availableMoves(self, position):
        #position[0]:x
        #position[1]:y
        
        #Iterate on toVisit positions
        self.visited.add(position)
        self.tryAllMoves(position, [])

    def tryAllMoves(self, position, directions):    
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
            self.tryMove( (position[0],  position[1]+1), directions + [Direction.UP] )
        if (position[0],  position[1]-1) in avail :
            self.tryMove( (position[0],  position[1]-1), directions + [Direction.DOWN] )
        if (position[0]-1,position[1]) in avail :
            self.tryMove( (position[0]-1,position[1])  , directions + [Direction.LEFT] )
        if (position[0]+1,position[1]) in avail :
            self.tryMove( (position[0]+1,position[1])  , directions + [Direction.RIGHT] )
        if (position[0]-1,position[1]+1) in avail :
            self.tryMove( (position[0]-1,position[1]+1), directions + [Direction.UPLEFT] )
        if (position[0]+1,position[1]+1) in avail :
            self.tryMove( (position[0]+1,position[1]+1), directions + [Direction.UPRIGHT] )
        if (position[0]-1,position[1]-1) in avail :
            self.tryMove( (position[0]-1,position[1]-1), directions + [Direction.DOWNLEFT] )
        if (position[0]+1,position[1]-1) in avail :
            self.tryMove( (position[0]+1,position[1]-1), directions + [Direction.DOWNRIGHT] )

    def tryMove(self, position, directions): #directions so far
        if(position[0] < 0 or position[0] > 10 or position[1] < 0 or position[1] > 10): 
            return
        if(position in self.visited):
            return
            
        self.visited.add(position)
        
        if(self.environment.is_visited(position)):
            self.tryAllMoves(position, directions)
        else:
            print(directions)
        
        
    