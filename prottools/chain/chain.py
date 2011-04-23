## @package prottools
# @TODO: needs full header

from sets import Set

class Chain:
  def __init__( self, name = '' ):
    self.name = name
    self.bonds = Set()
    self.atoms = Set()
  
  def add_bond( bond ):
    self.bonds.add( bond )
    self.atoms.add( bond.node_a )
    self.atoms.add( bond.node_b )
