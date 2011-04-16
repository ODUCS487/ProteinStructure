## @package pcat
# @TODO: needs full header

## Initialization
#
# Once imported, the following code executes automatically
# to initialize the application properly and deterine
# if this is running on a head-node or child-node

## ...

## Import mpi4py extensions
from mpi4py import MPI

## Import project globals
from pcat.globals import globals

## Import project com manager
from pcat.com import com

## Determine and assign current rank
globals.rank = MPI.COMM_WORLD.Get_rank()

## Determine and assign current name
globals.name = MPI.Get_processor_name()

## Create global manager
globals.manager = com.mgr()

## Bootstrap function
#
# This function serves an initialize purpose. It
# determines if this process is a root process and
# on which type of node, namely, a head-node or a
# child node. It then sets some shared variables in
# the globals namespace and returns to its caller.
# It is really just a wrapper for importing the
# correct bootstrap for each node type
#
# No parameters, returns no values.
# Should not be called on its own outside of this
# bootstrapper.
def bootstrap():
	# the following allows the assignment of a variable or function
	# outside the scope of the current function
	global start
	# if this is a head-node, import and execute
	# the head-node bootstrap, else same for
	# child-node bootstrap and assign the bootstrap.start
	# reference to the correct function
	if globals.rank == 0 and globals.name in globals.static.KNOWN_HEAD_NODE:
		from pcat.bootstrap import head
		start = head.start
	else:
		from pcat.bootstrap import child
		start = child.start

## Execute the bootstrap startup
bootstrap()
