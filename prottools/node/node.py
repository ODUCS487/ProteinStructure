## @package prottools
# @TODO: needs full header

print "from " + __file__

class Point:
    def __init__( self, new_x, new_y, new_z ):
        self.x = new_x
        self.y = new_y
        self.z = new_z

class Node:
    def __init__( self, idlabel, point, nodes ):
        self.idlabel = idlabel
        self.point = point
        self.nodes = nodes
