from hockey.action import Action

class Environnement(object):
    def __init__(self):
        self.visited = {(i,j): 0 for j in range(-1, 16) for i in range(-1, 16)}
        self.neighbours = {(i,j): [] for j in range(-1, 16) for i in range(-1, 16)}
        self.current_pos = (7,7)
        self.possible_goal = [(7, -1), (7, 15)]
        self.goal_idx = 0
        self.power_up = (0,0)
        self.power_up_avail = False
        self.power_up_taken = False

    def is_visited(self, node):
        return self.visited[node] > 0

    def init_pos(self, pos):
        self.visited[pos] = 1
        self.current_pos = pos

    def get_neighbours(self, node):
        return self.neighbours[node]

    def visit(self, action, is_us):
        try:
            delta = Action.move[action]
            new_pos = (self.current_pos[0] + delta[0], self.current_pos[1] + delta[1])
            self.visited[new_pos] += 1
            self.neighbours[new_pos].append(self.current_pos)
            self.neighbours[self.current_pos].append(new_pos)
            self.current_pos = new_pos
            if self.current_pos == self.power_up_taken:
                if not self.power_up_taken:
                    self.power_up_avail = True
                self.power_up_taken = True
        except Exception as e:
            print 'err', str(e)

    def try_take(self, pos):
        if not self.power_up_taken and pos == self.power_up:
            self.power_up_avail = True

    def un_try(self, pos):
        if self.power_up_taken and pos == self.power_up:
            self.power_up_avail = False

    def unuse_power_up(self):
        if self.power_up_taken:
            self.power_up_avail = True

    def use_power_up(self):
        self.power_up_avail = False

    def unvisit(self, action, is_us):
        delta = Action.move[action]
        new_pos = (self.current_pos[0] - delta[0], self.current_pos[1] - delta[1])
        self.visited[self.current_pos] -= 1
        self.neighbours[new_pos].remove(self.current_pos)
        self.neighbours[self.current_pos].remove(new_pos)
        self.current_pos = new_pos
        if self.visited[self.power_up] == 0:
            self.power_up_taken = False
            self.power_up_avail = False

    def my_goal(self):
        return self.possible_goal[self.goal_idx]

    def other_goal(self):
        return self.possible_goal[(self.goal_idx + 1) % 2]

if __name__ == '__main__':
    env = Environnement()
    env.init_pos((4,2))
    env.visit('north')
    print env.is_visited((4,1))
    print env.get_neighbours((4,2))
    env.unvisit('north')
    print env.is_visited((4,1))
    print env.get_neighbours((4,1))
