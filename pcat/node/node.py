#!/usr/bin/python
## @package pcat
# @TODO: needs full header

from random import *

from pcat.globals import globals

# class node
class node:
	def __init__(self, name):
		self.id = getrandbits(12)
		self.name = name
		self.nodes = [ self ]
		self.bonds = []


globals.nodes = [
	node('d'),
	node('e'),
	node('f'),
	node('g'),
	node('h'),
	]


print "globals.nodes has ", len(globals.nodes), " nodes"
for n in globals.nodes:
	print "this nodes name = ", n.name, " id = ", n.id, " and has ", len(n.nodes), " nodes and ", len(n.bonds), " bonds"


print "globals.nodes.count = ", len(globals.nodes)
for n in globals.nodes:
	print "this nodes name = ", n.name, " id = ", n.id, " and has ", len(n.nodes), " nodes and ", len(n.bonds), " bonds"
	for v in n.nodes:
		print "\tchild name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes and ", len(v.bonds), " bonds"


globals.nodes[2].nodes.append(globals.nodes[1])
globals.nodes[3].nodes.append(globals.nodes[0])
globals.nodes[4].nodes.append(globals.nodes[2])
globals.nodes[3].nodes.append(globals.nodes[4])
globals.nodes[0].nodes.append(globals.nodes[2])


print "globals.nodes.count = ", len(globals.nodes)
for n in globals.nodes:
	print "this nodes name = ", n.name, " id = ", n.id, " and has ", len(n.nodes), " nodes and ", len(n.bonds), " bonds"
	for v in n.nodes:
		print "\tchild name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes and ", len(v.bonds), " bonds"


# trying to modify some nodes to see if it is reflected throughout

print ""
print ""
print "modified 'd' to 'z' in one place to see if it was reflected everywhere..."

# changing name from 'd' to 'z'
globals.nodes[0].name = 'z'



print "globals.nodes.count = ", len(globals.nodes)
for n in globals.nodes:
	print "this nodes name = ", n.name, " id = ", n.id, " and has ", len(n.nodes), " nodes and ", len(n.bonds), " bonds"
	for v in n.nodes:
		print "\tchild name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes and ", len(v.bonds), " bonds"



# trying to add a child node to one to see if it is reflected in the count elsewhere

print ""
print ""
print "modified 'd' by adding a child check number of child nodes where 'z' is listed as a child"
print "original number before change = ", len(globals.nodes[0].nodes)

globals.nodes[0].nodes.append(globals.nodes[3])

print "globals.nodes.count = ", len(globals.nodes)
for n in globals.nodes:
	print "this nodes name = ", n.name, " id = ", n.id, " and has ", len(n.nodes), " nodes and ", len(n.bonds), " bonds"
	for v in n.nodes:
		print "\tchild name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes and ", len(v.bonds), " bonds"


# testing the ability to pass as a paramter and make changes to base object

def somefunc(_node, _nodetoadd):
	_node.nodes.append(_nodetoadd)
	if _node.name == 's':
		_node.name = 'ffggff'

print ""
print ""
print "using globals objects as paramters to functions..."

somefunc(globals.nodes[0], globals.nodes[4])
somefunc(globals.nodes[1], globals.nodes[3])

print "globals.nodes.count = ", len(globals.nodes)
for n in globals.nodes:
	print "this nodes name = ", n.name, " id = ", n.id, " and has ", len(n.nodes), " nodes and ", len(n.bonds), " bonds"
	for v in n.nodes:
		print "\tchild name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes and ", len(v.bonds), " bonds"


print ""
print ""
print "same with locals..."

s = node('s')
p = node('p')
q = node('q')

s.nodes.append(p)
q.nodes.append(s)
p.nodes.append(s)
p.nodes.append(q)

print "node name = ", s.name, " id = ", s.id, " and has ", len(s.nodes), " nodes"
for v in s.nodes:
	print "\tnode name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes"

print "node name = ", p.name, " id = ", p.id, " and has ", len(p.nodes), " nodes"
for v in p.nodes:
	print "\tnode name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes"

print "node name = ", q.name, " id = ", q.id, " and has ", len(q.nodes), " nodes"
for v in q.nodes:
	print "\tnode name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes"

print ""
print "using as func params"

somefunc(s, p)
somefunc(p, q)
somefunc(q, s)


print "node name = ", s.name, " id = ", s.id, " and has ", len(s.nodes), " nodes"
for v in s.nodes:
	print "\tnode name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes"

print "node name = ", p.name, " id = ", p.id, " and has ", len(p.nodes), " nodes"
for v in p.nodes:
	print "\tnode name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes"

print "node name = ", q.name, " id = ", q.id, " and has ", len(q.nodes), " nodes"
for v in q.nodes:
	print "\tnode name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes"


print ""
print ""
print ""

print "mixing and matching local and global(s) objects"
print ""


somefunc(s, globals.nodes[3])
somefunc(globals.nodes[2], p)
somefunc(globals.nodes[3], q)

globals.nodes.append(s)
globals.nodes[0].nodes.append(q)

print "printing locals first"
print ""

print "node name = ", s.name, " id = ", s.id, " and has ", len(s.nodes), " nodes"
for v in s.nodes:
	print "\tnode name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes"

print "node name = ", p.name, " id = ", p.id, " and has ", len(p.nodes), " nodes"
for v in p.nodes:
	print "\tnode name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes"

print "node name = ", q.name, " id = ", q.id, " and has ", len(q.nodes), " nodes"
for v in q.nodes:
	print "\tnode name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes"


print "now printing the pcat.globals nodes"
print ""
print "globals.nodes.count = ", len(globals.nodes)
for n in globals.nodes:
	print "this nodes name = ", n.name, " id = ", n.id, " and has ", len(n.nodes), " nodes and ", len(n.bonds), " bonds"
	for v in n.nodes:
		print "\tchild name = ", v.name, " id = ", v.id, " and has ", len(v.nodes), " nodes and ", len(v.bonds), " bonds"

