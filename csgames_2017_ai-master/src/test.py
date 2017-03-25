from AvailableMoves import *
from Environnement import *

if __name__ == '__main__':
	env = Environnement()
	movs = MovesChecker(env)
	movs.availableMoves((3,3))