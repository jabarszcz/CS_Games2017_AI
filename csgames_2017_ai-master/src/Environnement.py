class Environnement(object):
    def __init__(self):
        self.visited = {(i,j): False for j in range(10) for i in range(10)}
        self.neighbours = {(i,j): [] for j in range(10) for i in range(10)}

    def is_visited(self, node):
        return self.visited[node]

    def get_neighbours(self, node):
        return self.neighbours[node]

if __name__ == '__main__':
    env = Environnement()
    print env.is_visited((3,3))
    print env.get_neighbours((3,3))
