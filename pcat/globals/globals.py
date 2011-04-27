## @package pcat
# @TODO: needs full header

# @author W. Cole Davis

# Import mpi4py MPI namespace
from mpi4py import MPI

# Import time
import time

# Import os
import os

## Variables
#
# The following variables are merely comments
# representing variables that are set up by
# various modules in the package and are
# available once globals are imported from the
# globals namespace

## @var globals.rank
#
# Global variable representing the rank of the
# process of the currently executing application

## @var globals.name
#
# Global variable representing the name of the
# node of the currently executing application

## Predefined globals 
#
# These values are static and should not be changed
# during runtime and as defined in all uppercase letters
class static:
	## @var KNOWN_HEAD_NODE
	KNOWN_HEAD_NODE = [
		"group1",
		"group1.local",
		"group1.cs.odu.edu"
	]

## Shutdown procedure
#
# Shuts down the entire application properly
# @TODO: is not safe to call until after initialization
#        has been completed!!
def shutdown():
  print "Shutting down the system"
  manager.close()
  for i in range(1, comm.size):
    comm.send("EXIT", dest=i, tag=i)
  # @TODO: this needs to change but for this iteration is 'ok'
  MPI.Finalize()
  print "MPI was shutdown successfully, terminating"
