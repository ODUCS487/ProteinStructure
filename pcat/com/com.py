## @package pcat
# @TODO: needs full header

# @author W. Cole Davis

## com
#
# the pcat.com module handles the creation, management, 
# and communictions between spawned processes (not the
# MPI created processes

## Import exceptions
from pcat.exception import Error

## Import the multiprocessing
from multiprocessing import Manager, Queue, Pipe, Process

## Import globals
from pcat.globals import globals

## Import types
import types

## pcat.com.mgr
#
# The mgr class is a central object that handles much
# of the coordinated/synchronized/shared values between
# subprocesses in each node. Nodes will request new
# processes from the manager as it will initialize them
# properly and keep them synched with any other processes
class mgr(object):
	
	# pcat.com.mgr constructor, should only be called once
	# per initialization per node (that needs it)
	def __init__(self):

		# this internal manager provides the shared access semaphors
		# dicts, lists, shared memory (via Value, Array...)
		self.manager = Manager()

		# this is the primary queue for shared message passing between
		# default processes
		self.queue = Queue()

		# customary initialization of the process array
		self.workers = {}

		# pipes
		self.pipes = {}

	# pcat.com.mgr.new_process creates a new process and adds it
	# to its internal pool of workers, properly initializing it
	# to use the available message passing interfaces
	def new_process(self, name=None, run=None, additional=None, gui=False):

		# append the queue to the argument list
		if additional == None:
			additional = [self.queue]
		else:
			additional.append(self.queue)

		#pipes for the process
		comm1, comm2 = Pipe()

		additional.append(comm2)

		# create the new process and add it to pool
		p = Process(target=run, args=additional)
		
		p.start()

                # Error("Created pid %d name %s" % (p.pid, p.name))
		
		# add to workers pool
		self.workers[p.pid] = p
                if name != None:
                  # allow indexing by pid AND by name if one was given
                  self.workers[name] = p

		# add pipe to pool
		self.pipes[p.pid] = comm1
                if name != None:
                  # allow indexing by pid AND by name if one was given
                  self.pipes[name] = comm1

		# return the pid of the new process
		return p.pid

	def start(self, pid=None):
		self.workers[pid].start()	

	def stop(self, pid=None):
		self.workers[pid].terminate()	

	def send(self, pid=None, message=None):
		self.pipes[pid].send(message)

	def recv(self, pid):
		return self.pipes[pid].recv()

	def term(self, process_name=None, pid=None):
		pass
	
	def join(self, pid):
		self.workers[pid].join()

	def close(self):
		self.queue.close()
                # for _k in self.workers.keys():
                #   self.workers[_k].terminate()
                # they should have the exact same keys...no need to
                # iterate through twice
                for _k in self.pipes.keys():
                  self.pipes[_k].close()
                  self.workers[_k].terminate()
        
        def add(self, obj):
          self.queue.put(obj)


## The dispatcher "function" is executed as a separate process
#
# It contains uses a static class/object to maintain functionality with
# its own runloop waiting for instructions
def dispatcher(queue, con):

  # static _dispatcher class to handle mpi communications
  # to nodes...
  class _dispatcher(object):
    @staticmethod
    def run():
      while True:
        # loop until killed/is requested to close
        # assumption is that it will receive a dict with
        # numeric keys that represent the target
        # it can pass any serializable (pickleable) data objects
        while con.poll(2) == False: continue
        instr = con.recv()
        if instr is None: continue
        elif isinstance(instr, dict):
          # parse(instr) if len(instr) > 0 else continue
          if len(instr) > 0: _dispatcher.parse(instr)
          else: continue
        else: continue
    @staticmethod
    def parse(instr):
      for _k in instr.keys():
        globals.comm.send(instr[_k], dest=_k, tag=_k)
        
  # actually run the class
  _dispatcher.run()

  # Error("In dispatcher")
  # while True:
  #   instr = con.recv()
  #   if instr == "EXIT":
  #     break
  #   else:
  #     for _k in instr.keys():
  #       globals.comm.send(instr[_k], dest=_k, tag=_k)

  # print "Dispatcher received exit instruction, exiting"
  # exit

## The publisher "function" is executed as a separate process
#
# It contains a static class/object to receive all messages as reported
# by child-nodes for logging, printing...
def publisher(queue, con):
  pass
  # Error("In publisher")
  # Error("In publisher")
  # while True:
  #   msg = globals.comm.recv(source=0, tag=789)
  #   Error("publisher received message %s" % (msg))

# def test_func(q, comm):
# 	while True:
# 		msg = comm.recv()
# 		comm.send("did receive: %s" % msg)
# 
# if __name__ == "__main__":
# 	_mgr = mgr()
# 	pid = _mgr.new_process(run=test_func)
# 	print "pid returned: ", pid
# 	for i in range(9):
# 		_mgr.send(pid, i)
# 		print _mgr.recv(pid)
# 	_mgr.close()
# 	_mgr.stop(pid)
# 	print "done"
# 	exit

