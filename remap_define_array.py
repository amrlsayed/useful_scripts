#!/bin/python
"""
this python 3 script open a file and replace
the indexes of a C language array in the file with its C defined names
Example
A C file contains
#define FIRST_INDEX 0
#define SECOND_INDEX 1

int array[2];
array[0] = 5;
array[1] = 33;

after appling the propable patterns below on a file containing the 
above strings. the file should be edited to.

#define FIRST_INDEX 0
#define SECOND_INDEX 1

int array[2];
array[FIRST_INDEX] = 5;
array[SECOND_INDEX] = 33;

notice that the indexes of the arrays has been changed to the defined names.

NOTE: Change the below "Initializations" section to your regex patterns and file path following the noted regulations before appling this script.
for this example the patterns should be
# make a group for the define name and another group for the index. 
define_pattern = r"define\s+(\w+_INDEX)\s+(\d+)"
# note make a regex group for the  the items before the index ,the index and also items after it
# in three separate groups.
index_pattern = r"(array\[)(\d+)(])"
 
"""
import re
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
####################### Initializations ##############################################
file_path = "/home/amr/useful_scripts/examples/remap_define_array_ex.c"

list = []
# a work around to not replace the declaration int array[2]
list.insert(2,"2")	
# patterns.
# make a group for the define name and another group for the index. 
define_pattern = r"define\s+(\w+_INDEX)\s+(\d+)"
# note make a regex group for the  the items before the index ,the index and also items after it
# in three separate groups.
index_pattern = r"(array\[)(\d+)(])"
####################################################################

def replace(matchobj):
	str = matchobj.group(1) + list[int(matchobj.group(2))] + matchobj.group(3)
	return str
	

fh, abs_path = mkstemp()
with fdopen(fh,'w') as new_file:
	with open (file_path) as f:
		for line in f:
			for m in re.finditer(define_pattern,line):		
				list.insert(int(m.group(2)),m.group(1))
		f.close()	
		with open (file_path) as f:			
			for line in f:
				str = re.sub(index_pattern, replace, line)
				new_file.write(str)
			
#Remove original file
remove(file_path)
#Move new file
move(abs_path, file_path)











