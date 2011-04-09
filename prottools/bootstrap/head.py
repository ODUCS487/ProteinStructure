## @package prottools
# @TODO: needs full header

## Import exception handler
from prottools.exception import Error

## Import globals
from prottools.globals import globals

## Import ui
from prottools.ui import ui

## Import database
from prottools.database import database

## Import parser
from prottools.parser import parser

## Set globals.type
globals.type = "head"

## Start
# The primary functionality/loop begins here for the head-node
def start():
	# The tasks for this function are as follows
	# @TODO: This is being updated regularly and is not in a final form
	# 
	# - setup and manage the process pool for the head-node that has
	# 	the following responsibilities
	# 	- user-interface activity (responsiveness and display real-time data)
    #	- receive MPI messages passed from the child-nodes
	#	- send MPI messages to the child-nodes
	#	- manage appropriate actions through the logic controller
	#	- manage the database interface (as a sub-process)
	# @TODO: tbc...

	# 
	Error("Top of main loop in head-node")
