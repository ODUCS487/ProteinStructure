## @package prottools
# @TODO: needs full header

## Import globals
from prottools.globals import globals

## Set globals.type
globals.type = "head"

def start():
	print "This message is coming from the head-node from"
	print "within its 'start' function which both types of nodes"
	print "should execute since each has their own"
