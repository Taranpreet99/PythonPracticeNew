#Eight queen puzzle - put eight queens on chess board and none of them should attack each other
from unit_tester import test

#Function to check if diagonal is shared
def share_diagonal(x0,y0,x1,y1):
    dy = abs(y1 - y0) #absolute y distance
    dx = abs(x1 - x0) #absolute x distance
    return dx == dy



#Tests for share diagonal
test(not share_diagonal(5,2,2,0))
test(share_diagonal(5,2,3,0))
test(share_diagonal(5,2,4,3))
test(share_diagonal(5,2,4,1))

#Now next part of the algorithm is to check if the queens clashes with each other
def col_clashes(bs,c):
    #true if queen at column c clashes with any queen to its left
    for i in range(c):
        if share_diagonal(i,bs[i],c,bs[c]):
            return True #Diagonal Clash
    return False #No Clashes 


#Test cases for col_clashes function
test(not col_clashes([6,4,2,0,5],4))
test(not col_clashes([6,4,2,0,5,7,1,3],7))
test(col_clashes([0,1],1))
test(col_clashes([5,6],1))
test(col_clashes([6,5],1))
test(col_clashes([0,6,4,3],3))
test(col_clashes([5,0,7],2))
test(not col_clashes([2,0,1,3],1))
test(col_clashes([2,0,1,3],2))

#Function to check if queens are clashing on diagonals
def has_clashes(the_board):
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

test(not has_clashes([6,4,2,0,5,7,1,3]))
test(has_clashes([4,6,2,0,5,7,1,3]))
test(has_clashes([0,1,2,3]))
test(not has_clashes([2,0,3,1]))

def main():
    
    import random
    rng = random.Random() #Instantiate a generator
    bd = list(range(8)) #Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd,tries))
            tries = 0
            num_found += 1
main()