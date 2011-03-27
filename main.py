#!/usr/bin/python

#######################################################
# CS488 - SPRING 2011 - ODU CS - J. MORRIS
#######################################################
#
# @TODO: needs full header
#
#######################################################

## @file main.py
#
# This is the primary executable of the application. There
# are essentially 2 paths of how this file is handled once
# executed in a MPI runtime: as a head-node dispatcher and 
# as a child-node dispatcher.
# @TODO: needs complete description and implementation details
#        once it has been completed and they have been defined

## Import the project globals
from prottools.globals import globals

## Import the project bootstrapper
#
# Once the bootstrapper has been imported, it automatically
# begins its initialization process by importing any other
# immediately necessary package(s) - it also determines
# whether or not this is a head-node or child-node and
# acts accordingly. For more information see bootstrap.py
# in the prottools package root directory
from prottools.bootstrap import bootstrap

print 'Rank: %d, Name: %s, Type: %s' % (globals.rank, globals.name, globals.type)

exit
