## @package pcat
# @TODO: needs full header

# @author W. Cole Davis

## Import exception handler
from pcat.exception import Error

## Import globals
from pcat.globals import globals

## Import ui
from pcat.ui import ui

## Import database
from pcat.database import database

## Import parser
from pcat.parser.parser import parser

## Set globals.type
globals.type = "head"

## Import com
from pcat.com import com

## Import sys
import sys

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

        # start the dispatcher process
        # it is accessible from here on out in globals manager and can be accessed by name
        globals.manager.new_process(run=com.dispatcher, name="dispatcher")

        # start the service that will be listening for the reports from the child nodes
        globals.manager.new_process(run=com.publisher, name="publisher")
        
        # Error("The size of the graph of nodes is %d" % (globals.comm.size))

        # need to set the chains object in the global namespace (head-only)
        globals.chains = []
        
        # need to set the parser object
        globals.parser = parser()

        # Need to start the GUI
        # TEMPORARY !--------------------------------
        
        # READ FILENAMES ONE AT A TIME UNTIL BLANK
        print "Please enter filenames space-delimited then press enter,"
        print "or press enter to use all available chains in the data/ directory"
        files = raw_input("\r: ")
        if files == "":
          globals.parser.parse()
        else:
          globals.parser.set_files(files, True)
        #--------------------------------------------
        print "Done parsing"
        
        print "Printing chains:"
        for chain in globals.chains:
          print ""
          print "Name: %s" % (chain.name)
          for bond in chain.bonds:
            print bond
          print ""

        # globals.manager.close()
        # exit

        globals.shutdown()


        # example of making a broadcast
        # globals.comm.bcast("BEGIN", root=0)
        # time.sleep(10)
        # globals.manager.send("dispatcher", {1:"hello",2:"bonjour",3:"nihao",4:"hola"})
        # Error("Testing dispatcher by sending it a string instead of dict")
        # globals.manager.send("dispatcher", "EXIT")
        # Error("Waiting to join with the dispatcher (head-node)")
        # globals.manager.close()
        # globals.manager.join("dispatcher")
        # Error("Joined, now closing down manager")
        # Error("Closed the manager, done")

