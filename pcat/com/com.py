## @package pcat
# @TODO: needs full header

## com
#
# the pcat.com module handles the creation, management, 
# and communictions between spawned processes (not the
# MPI created processes

# import the multiprocessing
from multiprocessing import Manager, Queue, Pipe, Process

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
	def new_process(self, run=None, additional=None, gui=False):

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

		print "pid ", p.pid, " name ", p.name
		
		# add to workers pool
		self.workers[p.pid] = p

		# add pipe to pool
		self.pipes[p.pid] = comm1

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
		print self.queue
		print self.manager


def test_func(q, comm):
	while True:
		msg = comm.recv()
		comm.send("did receive: %s" % msg)

if __name__ == "__main__":
	_mgr = mgr()
	pid = _mgr.new_process(run=test_func)
	print "pid returned: ", pid
	for i in range(9):
		_mgr.send(pid, i)
		print _mgr.recv(pid)
	_mgr.close()
	_mgr.stop(pid)
	print "done"
	exit

# import urwid
# 
# import sys
# import os
# import termios


# def handle_inputs(inp):
# 	if inp in ('q', 'Q'):
# 		conn1.send(True)
# 		raise urwid.ExitMainLoop()
# 	else:
# 		conn1.send(inp)
# 		if conn1.recv():
# 			text.set_text(conn1.recv())
# 
# def some_func1(conn):
# 
# 	msgs = []
# 	msg = ""
# 	while True:
# 		ret = conn.recv()
# 		if type(ret) is bool:
# 			if msg != "":
# 				msgs.append(msg)
# 			break
# 		elif ret == "enter":
# 			msgs.append(msg)
# 			conn.send(True)
# 			conn.send(msg)
# 			msg = ""
# 		else:
# 			conn.send(False)
# 			msg += ret
# 	print "loop done?"
# 	print msgs[:]
# 	conn.send(True)
# 	conn.send(msgs)
# 	conn.close()
# 	exit
# 
# if __name__ == "__main__":
# 
# 	conn1, conn2 = Pipe()
# 
# 	p1 = Process(target=some_func1, args=(conn2,))
# 	p1.start()
# 
# 	text = urwid.Text("This is the original text")
# 	wrap = urwid.Filler(text, "middle")
# 	loop = urwid.MainLoop(wrap, unhandled_input=handle_inputs)
# 
# 	loop.run()
# 
# 	
# 	print "loop done"
# 	msgs = conn1.recv()
# 	p1.join()
# 	print "joined p1"
# 	print msgs[:]

# def gui(conn, fdin):
# 
# 	# sys.stdin = termios.tcgetattr(input)
# 	# sys.stdout = termios.tcgetattr(output)
# 	# sys.stdout = sys.__stdout__
# 	sys.stdin = os.fdopen(fdin, 'r')
# 
# 	# print sys.stdin 
# 	# print sys.stdout
# 
# 	def handle_interupts(interupt):
# 		conn.send("HI")
# 		if interupt in ('q', 'Q'):
# 			conn.send(None)
# 			raise urwid.ExitMainLoop()
# 		else: conn.send(interupt)
# 	text = urwid.Text("This is the original text")
# 	wrap = urwid.Filler(text, "middle")
# 	loop = urwid.MainLoop(wrap, unhandled_input=handle_interupts)
# 	loop.run()
# 	
# 
# if __name__ == "__main__":
# 
# 	conn1, conn2 = Pipe()
# 
# 	fd = sys.stdin.fileno()
# 	
# 	p1 = Process(target=gui, args=(conn2, fd))
# 
# 	p1.start()
# 	
# 	msgs = []
# 	while True:
# 		try:
# 			msg = conn1.recv()
# 			if msg == None:
# 				raise ""
# 			else:
# 				msgs.push(msg)
# 		except:
# 			break
# 
# 	p1.join()
# 	
# 	print msgs[:]



# run a test

# import time
# import os
# 
# def some_func1(conn):
# 	for i in range(8):
# 		conn.send("what up %d" % i)
# 		time.sleep(2)
# 	conn.send(True)
# 	conn.close()
# 
# def some_func2(conn):
# 	print "I am some_func2 of second process"
# 	while(True):
# 		try:
# 			msg = conn.recv()
# 			if type(msg) is bool:
# 				raise "Uh..."
# 			print "p2 gets message: ", msg
# 		except:
# 			print "whoa connection closed!"
# 			return
# 		
# if __name__ == "__main__":
# 	conn1, conn2 = Pipe()
# 	p1 = Process(target=some_func1, args=(conn1,))
# 	p2 = Process(target=some_func2, args=(conn2,))
# 	p1.start()
# 	p2.start()
# 	p1.join()
# 	print "p1 joined"
# 	p2.join()
# 	print "p2 joined"
# 	exit
