from hockey.action import Action

class Environnement(object):
    def __init__(self):
        self.visited = {(i,j): False for j in range(11) for i in range(11)}
        self.neighbours = {(i,j): [] for j in range(11) for i in range(11)}
        self.current_pos = (5,5)

    def is_visited(self, node):
        return self.visited[node]

    def init_pos(self, pos):
        self.visited[pos] = True
        self.current_pos = pos

    def get_neighbours(self, node):
        return self.neighbours[node]

    def visit(self, action):
        delta = Action.move[action]
        new_pos = (self.current_pos[0] + delta[0], self.current_pos[1] + delta[1])
        self.visited[new_pos] = True
        self.neighbours[new_pos].append(self.current_pos)
        self.neighbours[self.current_pos].append(new_pos)
        self.current_pos = new_pos
        print self.current_pos


if __name__ == '__main__':
    env = Environnement()
    print env.is_visited((3,3))
    print env.get_neighbours((3,3))
