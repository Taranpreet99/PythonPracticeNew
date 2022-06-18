from ast import get_docstring
import os

def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    if prefix == "":
        print("Folder listing for", path)
        prefix = "| "
    
    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_files(fullname,prefix + "| ")



def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60,-120,60,0]:
            koch(t,order-1,size/3)
            t.left(angle)


#Sum of elements in a nested num list
def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot


#Find largest value in nested number list
def r_max(nxs):
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e
        
        if first_time or val >largest:
            largest = val
            first_time = False
        
    return largest