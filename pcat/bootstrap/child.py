## @package pcat
# @TODO: needs full header

# @author W. Cole Davis

## Import globals
from pcat.globals import globals

## Import exceptions
from pcat.exception import Error

## Import com
from pcat.com import com

## Set globals.type
globals.type = "child"

def start():

  # The child nodes need to be able to receive MPI requests and
  # act accordingly. This means they need to be listening for MPI
  # message passing then creating a sub-process that will execute
  # the correct action for that request. Each sub-process needs
  # the ability to send MPI messages (responses) back to the
  # head node

  # Error("Child node %s started and waiting for instruction..." % (globals.rank))

  # Listen for command from head-node (blocking receive)
  # The first message from the head-node will be a broadcast
  # @TODO: this needs to change...
  
  # example of receiving broadcast from root
  # msg = globals.comm.bcast(None, root=0)

  # The initial iteration of the child nodes will be straight forward
  # and only good enough to do just the tasks that were originally specified
  # as they serve, at this point, primarily as proof-of-concept
  # and need major revision

  # Wait until the first instruction is presented before doing anything
  instr = globals.comm.recv(source=0, tag=globals.rank)

  # Error("Received message: '%s' from head-node (I am rank=%s)" % (instr, globals.rank))

  # globals.report("(%s) Just received my first assignment and reporting" % (globals.rank))

  exit
