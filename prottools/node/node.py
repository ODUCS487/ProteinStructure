## @package prottools
# @TODO: needs full header

print "from " + __file__

class Point:
    x = 0.0
    y = 0.0
    z = 0.0
    def __init__( self, new_x = 0.0, new_y = 0.0, new_z = 0.0 ):
        self.x = new_x
        self.y = new_y
        self.z = new_z

class Node:
    idlabel = " ";
    point = Point( )
    nodes = array( [ Point() ] )
    def __init__( self, idlabel, point, nodes ):
        self.idlabel = idlabel
        self.point = point
        self.nodes = nodes
