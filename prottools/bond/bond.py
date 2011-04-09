## @package prottools
# @TODO: needs full header

from node import node

print "from " + __file__

class Bond:
    def __init__( self, new_node1, new_node2 ):
        self.node1 = new_node1
        self.node2 = new_node2
        self.magnitude = new_node1.x - new_node2.x
