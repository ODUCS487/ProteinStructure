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

