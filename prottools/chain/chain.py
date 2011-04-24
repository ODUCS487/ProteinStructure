## @package prottools
# @TODO: needs full header

class Chain:
  def __init__( self, name = '' ):
    self.name = name
    self.bonds = {}
    self.atoms = {}
  
  def add_bond( bond ):
    #bond_key = tuple( sorted( bond.node_a.idlabel, bond.node_b ) )
    self.bonds[ tuple() ] = bond
    self.atoms.add( bond.node_a )
    self.atoms.add( bond.node_b )

if __name__ == '__main__':
  my_nodes = [ 'CD12', 'AB12' ]
  my_nodes.sort()
  print my_nodes
  
  my_bonds = {}
  my_bonds[ tuple( sorted( my_nodes ) ) ] = ( my_nodes[ 0 ], my_nodes[ 1 ] )
  print ( my_nodes[ 0 ], my_nodes[ 1 ] ) in my_bonds
  print my_bonds[ ( my_nodes[ 0 ], my_nodes[ 1 ] ) ]
