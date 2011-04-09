## @package prottools
# @TODO: needs full header

# @TODO: needs definitions

# Import globals
from prottools.globals import globals

# Import traceback
import traceback

def Error(message, type = "Debug"):
	stack = traceback.extract_stack(limit=2)
	caller = stack[0][2]
	file = stack[0][0]
	line = stack[0][1]
	print "Caught : %s => %s" % (type, message)
	print "\t["
	print "\t  node    => %s" % globals.name
	print "\t  process => %s" % globals.rank
	print "\t  caller  => %s" % caller
	print "\t  file    => %s" % file
	print "\t  line    => %s" % line
	print "\t]"

