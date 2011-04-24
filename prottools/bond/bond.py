## @package prottools
# @TODO: needs full header

class Bond:
  def __init__( self, node_a, node_b ):
    # Store list sorted by id so that one pair has one key
    self.nodes = sorted ( [ node_a, node_b ] )
    # Should not connect at this point, connecting requires having
    # a list of all the atoms, hence connecting should be handled by
    # the Chain class
    # self.node_a.connect( node_b )

if __name__ == '__main__':
  class Point:
    def __init__( self, idlabel = '', x = 0.0, y = 0.0 ):
      self.idlabel = idlabel
      self.x = x
      self.y = y
  
  point1 = Point( 'AB12', 1.0, 2.0 )
  point2 = Point( 'CD34', 3.0, 4.0 )
  unsorted_points = [ point2, point1 ]
  for point in unsorted_points:
    print point.idlabel
  points = sorted( unsorted_points )
  for point in points:
    print point.idlabel, point.x, point.y
  
  numbers = sorted( [ 3, 5, 2, 6, 1 ] )
  print numbers
  for i in range( 0, len( numbers ) ):
    print numbers[ i ]
