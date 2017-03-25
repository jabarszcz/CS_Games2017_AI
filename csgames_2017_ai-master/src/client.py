import random

from twisted.internet import protocol
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver

from hockey.action import Action
from Environnement import Environnement
from AvailableMoves import *
import sys
import re


class HockeyClient(LineReceiver, object):
    def __init__(self, name, debug):
        self.name = name
        self.debug = debug
        self.env = Environnement()
        self.r = re.compile('polarity of the goal has been inverted - \d*')
        self.r4 = re.compile('your goal is \w+ - \d*')
        self.power_used = False

    def connectionMade(self):
        self.sendLine(self.name)

    def sendLine(self, line):
        super(HockeyClient, self).sendLine(line.encode('UTF-8'))

    def lineReceived(self, line):
        line = line.decode('UTF-8')

        if self.debug:
            print('Server said:', line)
        if '{} is active player'.format(self.name) in line:
            self.play_game()
        if 'invalid move' in line:
            result = Action.from_number(random.randint(0, 7))
            self.sendLine(result)
        if 'ball is at' in line:
            try:
                tuple = line.split(' ')[3:5]
                tuple = (int(tuple[0].strip(',').strip('(')), int(tuple[1].strip(')')))
                self.env.init_pos(tuple)
            except:
                pass
        if 'power up is at' in line:
            try:
                tuple = line.split(' ')[4:6]
                tuple = (int(tuple[0].strip(',').strip('(')), int(tuple[1].strip(')')))
                self.env.power_up = tuple
            except:
                pass
        if re.match(self.r4, line):
            goal_str = line.split(' ')[-3]
            if goal_str == 'north':
                self.env.goal_idx = 0
            else:
                self.env.goal_idx = 1
        if 'did go' in line:
            possible_line = line.split(' ')[-4]
            direction = ''
            if possible_line == 'north' or possible_line == 'south':
                direction += possible_line + ' '
            is_us = {}.format(self.name) in line
            direction += line.split(' ')[-3]
            self.env.visit(direction, is_us)
        if re.match(self.r, line):
            self.env.goal_idx = (self.env.goal_idx + 1) % 2
            print 'invted', self.env.my_goal()

    def play_game(self):
        movs = MovesChecker(self.env)
        dis, best = sys.maxint, 0
        for move in movs.availableMoves(self.env.current_pos, False):
            pos, dirs = move
            dis, best = min((dis, best), (self.distance(self.env.my_goal(), pos), dirs[0]))
        l = ''
        # If power up, l += 'power '
        l += Action.from_number(best)
        self.sendLine(l)
        self.env.try_take(best)

    def distance(self, a, b):
        ax, ay = a
        bx, by = b
        return max(abs(ax-bx), abs(ay-by))


class ClientFactory(protocol.ClientFactory):
    def __init__(self, name, debug):
        self.name = name
        self.debug = debug

    def buildProtocol(self, addr):
        return HockeyClient(self.name, self.debug)

    def clientConnectionFailed(self, connector, reason):
        if self.debug:
            print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        if self.debug:
            print("Connection lost - goodbye!")
        reactor.stop()


name = "poly caulking did go south polarity of the goal has been inverted {}".format(random.randint(0, 999))

f = ClientFactory(name, debug=True)
reactor.connectTCP("localhost", 8023, f)
reactor.run()
