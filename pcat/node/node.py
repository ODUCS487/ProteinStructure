## @package prottools
# @TODO: needs full header

# @author Alvin Fagan

from sets import Set

class Node:
  def __init__( self, idlabel = '', x = 0.0, y = 0.0, z = 0.0, neighbors = None ):
    self.idlabel = idlabel
    self.x = x
    self.y = y
    self.z = z
    # Make neighbors as set of string ids rather than actual nodes to
    # prevent nodes from connecting to nodes not in the same chain
    self.neighbors = Set() if neighbors is None else neighbors
  
  # Connect function should not exist here, connecting requires having
  # a list of all the nodes, hence connecting should be handled by
  # the Chain class in order to prevent duplicate nodes/etc
  # Analogy to graph theory: the Graph (Chain) should connect the dots

#if __name__ == '__main__':
if False:
  print __package__
  import string, random

  def connect( node_a, node_b ):
    node_a.neighbors.append( node_b )
    node_b.neighbors.append( node_a )

  my_nodes = []
  chars = string.ascii_uppercase + string.digits
  char_set = random.sample( chars, len( chars ) )
  print char_set, '\n'
  
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
        
    print i, '=', my_nodes[ i ].idlabel
    print my_nodes[ i ].x
    print my_nodes[ i ].y
    print my_nodes[ i ].z, '\n'
    
  print my_nodes[ 1 ].neighbors
    
  connect( my_nodes[ 1 ], my_nodes[ 0 ] )
  connect( my_nodes[ 1 ], my_nodes[ 2 ] )
    
  for node in my_nodes[ 1 ].neighbors:
    print node.idlabel
