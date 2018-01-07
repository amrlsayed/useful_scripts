# Useful Scripts

This repository should contain some useful scripts I use to accelerate the development time.
### remap_define_array.py
This python 3 script open a file and replace the indexes of a C language array in the file with its C defined names
#### Usage
Need Python 3 to run this Command
```bash
$ python3 remap_define_array.py
```
#### Example
A C file contains
```c
#define FIRST_INDEX 0
#define SECOND_INDEX 1

int array[2];
array[0] = 5;
array[1] = 33;
```
After appling the proper patterns below on a file containing the 
above strings. the file should be edited to.
```c
#define FIRST_INDEX 0
#define SECOND_INDEX 1

int array[2];
array[FIRST_INDEX] = 5;
array[SECOND_INDEX] = 33;
```
Notice that the indexes of the arrays has been changed to the defined names.
NOTE: Change the "Initializations" sectionin the script to your regex patterns and file path following the noted regulations before appling this script.
for this example the patterns in the python file should be:
```python
# make a group for the define name and another group for the index. 
define_pattern = r"define\s+(\w+_INDEX)\s+(\d+)"
# note make a regex group for the  the items before the index ,the index and also items after it
# in three separate groups.
index_pattern = r"(array\[)(\d+)(])"
```
---

