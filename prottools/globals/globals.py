## @package prottools
# @TODO: needs full header


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
