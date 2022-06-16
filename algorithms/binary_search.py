#Now instead of searching through whole file/list we will start
#in the middle instead, that's much better performance wise
#but we have to make sure list is ordered

from unit_tester import test

#Function to find index of the key in the sequence
def search_binary(xs, target):
    lb = 0 #lowerbound of ROI
    ub = len(xs) #upperbound of ROI
    while True:
        if lb == ub: #If region of interest (ROI) becomes empty
            return -1
        
        #Next probe in the middle of the ROI
        mid_index = (lb + ub) // 2

        #fetch the item at the middle position
        item_at_mid = xs[mid_index]

        #Compare probed item to the target
        if item_at_mid == target:
            return mid_index #found the item
        if item_at_mid < target:
            lb = mid_index + 1 #Use upper half of ROI next time
        else: 
            ub = mid_index #Use lower half of ROI next time


#tests first
xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
test(search_binary(xs, 20) == -1)
test(search_binary(xs,99) == -1) 
test(search_binary(xs,1) == -1)
for (i,v) in enumerate(xs):
    test(search_binary(xs, v) == i)

