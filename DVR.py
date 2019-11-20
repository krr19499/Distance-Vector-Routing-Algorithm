import math
from threading import Thread

from InputController import InputController
from TimedFunc import TimedFunc
from PeerServer import PeerServer
from Peer import Peer

class DVR():

    def __init__(self):
        self.server_running = False
        InputController(self)

    def __del__(self):
        self.crash()

    def server(self, _t, filename, _i, update_interval):
        '''Reads the topology file, initiates the node table, and starts the update & server thread'''
        self.server_running = True

        with open(filename, 'r') as f:
            num_servers = int(f.readline())
            num_neighbors = int(f.readline())

            servers = dict.fromkeys(range(1, num_servers+1))
            neighbors = dict()

            for i in range(0, num_servers):
                line = f.readline()
                id, ip, port = (int(i) if '.' not in i else i for i in line.split())
                servers[id] = ip, port

            for i in range(0, num_neighbors):
                line = f.readline()
                myid, neighbor, cost = (int(i) for i in line.split())
                neighbors[neighbor] = cost

        me = servers[myid]

        # Establish links and create a neighbor connection table {'<id>': <sock object>...}
        # Create a node table with link costs
        TimedFunc(self.step, float(update_interval))
        PeerServer(*me)

    def update(self, server1, server2, cost):
        if cost == 'inf':
            cost = math.inf
        pass

    def step(self):
        # update node table here
        pass

    def packets(self):
        '''Display the number of distance vector (packets) this  server
        has  received  since  the  last  invocation of this information'''
        pass

    def display(self):
        '''Display the current routing table formatted as a sequence
        of lines, with each line indicating: <source-server-ID> <next-hop-server-ID> <cost-of-path>'''
        pass

    def disable(self, server):
        '''Closes the connection with the given server id'''
        pass

    def crash(self):
        '''Closes all server connections. The neighboring servers must
        handle this close correctly and set the link cost to infinity.'''
        pass

if __name__ == "__main__":
    DVR()

