#!/bin/bash

# This is nothing more than a shortcut
# Important Note: We will NOT be using a process-number (-n or -np)
# when executing mpirun since the dispatcher will do this automatically

# When all of the problems with the NFS being mounted are gone
# this needs to be updated to use the hosts file
# mpirun --host group1,compute-0-0 ./main.py
mpirun -hostfile hosts ./main.py
