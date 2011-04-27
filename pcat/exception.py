## @package pcat
# @TODO: needs full header

# @TODO: needs definitions

# @author W. Cole Davis

## Import globals
from pcat.globals import globals

## Import traceback
import traceback

## Import os
import os

def Error(message, type = "Debug"):
  stack = traceback.extract_stack(limit=2)
  caller = stack[0][2]
  file = stack[0][0]
  line = stack[0][1]
  print "Caught : %s => %s" % (type, message)
  print "\t["
  print "\t  node    => %s" % globals.name
  print "\t  process => %s" % globals.rank
  print "\t  pid     => %d" % os.getpid()
  print "\t  caller  => %s" % caller
  print "\t  file    => %s" % file
  print "\t  line    => %s" % line
  print "\t]"
  if type == "Fatal":
    globals.shutdown()
