import random

from twisted.internet import protocol
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver

from hockey.action import Action
from Environnement import Environnement


class HockeyClient(LineReceiver, object):
    def __init__(self, name, debug):
        self.name = name
        self.debug = debug
        self.env = Environnement()

    def connectionMade(self):
        self.sendLine(self.name)

    def sendLine(self, line):
        super(HockeyClient, self).sendLine(line.encode('UTF-8'))

    def lineReceived(self, line):
        line = line.decode('UTF-8')
        if self.debug:
            print('Server said:', line)
        if '{} is active player'.format(self.name) in line or 'invalid move' in line:
            self.play_game()
        if 'ball is' in line:
            tuple = line.split(' ')[3:5]
            tuple = (int(tuple[0].strip(',').strip('(')), int(tuple[1].strip(')')))
            self.env.init_pos(tuple)
        if 'did go' in line:
            possible_line = line.split(' ')[-4]
            direction = ''
            if possible_line == 'north' or possible_line == 'south':
                direction += possible_line + ' '
            direction += line.split(' ')[-3]
            self.env.visit(direction)

    def play_game(self):
        result = Action.from_number(random.randint(0, 7))
        self.sendLine(result)


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


name = "poly caulking{}".format(random.randint(0, 999))

f = ClientFactory(name, debug=True)
reactor.connectTCP("localhost", 8023, f)
reactor.run()
