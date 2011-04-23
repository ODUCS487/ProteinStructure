## @package prottools
# @TODO: needs full header

class Chain:
  def __init__( self, nodes = None, edges = None ):
    self.atoms = [] if nodes is None else nodes
    self.bonds = [] if edges is None else edges
