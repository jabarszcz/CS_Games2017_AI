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
		self.toVisit = []
		
	def availableMoves(self, position):
		#position[0]:x
		#position[1]:y
		self.toVisit.add(position)
		
		#Iterate on toVisit positions
		
		while(self.toVisit.size):
			actual = self.toVisit.pop()
			self.visited.add(actual)
			tryAllMoves(actual, [])

	def tryAllMoves(self, position, directions):	
		#todo check if arc is already taken
		tryMove( (position[0],  position[1]+1), previousDirections + [Direction.UP] )
		tryMove( (position[0],  position[1]-1), previousDirections + [Direction.DOWN] )
		tryMove( (position[0]-1,position[1])  , previousDirections + [Direction.LEFT] )
		tryMove( (position[0]+1,position[1])  , previousDirections + [Direction.RIGHT] )
		tryMove( (position[0]-1,position[1]+1), previousDirections + [Direction.UPLEFT] )
		tryMove( (position[0]+1,position[1]+1), previousDirections + [Direction.UPRIGHT] )
		tryMove( (position[0]-1,position[1]-1), previousDirections + [Direction.DOWNLEFT] )
		tryMove( (position[0]+1,position[1]-1), previousDirections + [Direction.DOWNRIGHT] )

	def tryMove(self, position, directions) #directions so far
		if(position[0] < 0 or position[0] > 10 or position[1] < 0 or position[1] > 10): 
			return
		if(position in self.visited):
			return
		if(environment.is_visited(position))
			tryAllMoves()
		else
			print(directions)
		
		
	