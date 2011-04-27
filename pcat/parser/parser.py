## @package pcat
# @TODO: needs full header

# @author W. Cole Davis
# @author Tim Werner

## Parser Class

# First-iteration quick attempt to make the parser
# since one was not available...

# @TODO: more efficient implementation...
# @TODO: add comments

# Import pcat.globals
from pcat.globals import globals

# Import math
from math import sqrt, pow

# Import pcat.exception
from pcat.exception import Error

# Import node
from pcat.node.node import Node

# Import chain
from pcat.chain.chain import Chain

# Import bond
from pcat.bond.bond import Bond

# Import dircache
import dircache

class parser(object):
  def __init__(self):
    self.files = []
  
  def set_files(self, files = None, parseafter = False):
    if files is None:
      return False      
    if type(files) is str:
      files = files.strip().split()
    self.files = files
    if parseafter:
      self.parse()
  
  def parse(self, files = None):
    if files is None:
      if len(self.files) <= 0:
        # Error("Attempted to parse without files available", type="Fatal")
        files = dircache.listdir("data")
        print "Using all files found in data/ directory"
        print "%s" % (", ".join(files))
      else:
        files = self.files
    badfiles = []
    for file in files:
      try:
        _f = open("data/%s" % (file), "r")
        _chain = Chain(file)
        _nodes = []
        for line in _f:
          if line.strip():
            try:
              name, x, y, z = line.split()
            except: 
              print "Error in line: '%s'" % (line)
              globals.shutdown()
            x = float(x)
            y = float(y)
            z = float(z)
            _nodes.append(Node(name, x, y, z))
            if len(_nodes) == 2:
              _bond = Bond(_nodes[0], _nodes[1])
              _chain.add_bond(_bond)
              _nodes = []
        globals.chains.append(_chain)
      except IOError as (no, err): 
        badfiles.append("data/%s" % (file))
    if len(badfiles) > 0:
      Error("There were errors in file(s): %s" % (", ".join(badfiles)))     
      if len(globals.chains) < 2:
        Error("The number of chains available will be too few to continue", type="Fatal")
