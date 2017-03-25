from AvailableMoves import *
from Environnement import *

if __name__ == '__main__':
    env = Environnement()
    env.init_pos((3,3))
    movs = MovesChecker(env)
    env.visit('north')
    m = movs.availableMoves((3,3))
    for x in m:
        print x
