#merge algorithm
#Merge sorted lists xs and ys

from lib2to3.pgen2.token import EQUAL
from unit_tester import test

def merge(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs): #If xs list is finished
            result.extend(ys[yi:]) #Add remaining items from ys
            return result

        if yi >= len(ys):#same again, but swapped list
            result.extend(xs[xi:])
            return result
        #Both lists have items, copy smaller to result
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1 
        else:
            result.append(ys[yi])
            yi += 1

#Tests for this algorithm
xs = [1,3,5,7,9,12,13,15,16,19]
ys = [4,8,12,16,20,24]
zs = xs+ys
zs.sort()
test(merge(xs, []) == xs)
test(merge([], ys) == ys)
test(merge([], []) == [])
test(merge(xs, ys) == zs)
test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
               ["a", "big", "big", "bite", "cat", "dog"])

