## @package prottools
# @TODO: needs full header

import random
import string

class Node:
    def __init__( self, idlabel = "", x = 0.0, y = 0.0, z = 0.0, nodes = [] ):
        self.idlabel = idlabel
        self.x = x
        self.y = y
        self.z = z
        self.nodes = nodes

if __name__ == '__main__':
    my_nodes = []
    chars = string.ascii_uppercase + string.digits
    char_set = random.sample( chars, len( chars ) )
    print char_set
    limit = 100
    limit_a = -limit
    limit_b = limit
    for i in range( 0, 5 ):
        x = random.uniform( limit_a, limit_b )
        y = random.uniform( limit_a, limit_b )
        z = random.uniform( limit_a, limit_b )
        label = ''.join( char_set[:4] )
        char_set = char_set[4:]
        my_nodes.append( Node( label, x, y, z ) )
        
        print my_nodes[ i ].idlabel
        print my_nodes[ i ].x
        print my_nodes[ i ].y
        print my_nodes[ i ].z
        
    print my_nodes[ 1 ].nodes
    
    my_nodes[ 1 ].nodes.append( my_nodes[ 0 ] )
    my_nodes[ 0 ].nodes.append( my_nodes[ 1 ] )
    my_nodes[ 1 ].nodes.append( my_nodes[ 2 ] )
    my_nodes[ 2 ].nodes.append( my_nodes[ 1 ] )
    
    for node in my_nodes[ 1 ].nodes:
		print node.idlabel
