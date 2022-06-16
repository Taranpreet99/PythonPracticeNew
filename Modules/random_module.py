#Practicing Random module

import random

def make_random_ints(num,lower_bound, upper_bound):
    #a list contating num random numbers between lower_bound and upper_bound
    rng = random.Random() #random number generator
    result = [] #empty list
    for i in range(num):
        result.append(rng.randrange(lower_bound,upper_bound))
    return result #will get random number list from this function

#Above liust can have duplicates
#To create a unique list, follow this:
rand_list = list(range(1,13)) #list 1-12 no duplicates
rng = random.Random()
rng.shuffle(rand_list) #shuffle the list
result = rand_list[:5] # chooses first 5 from the shuffled list

#Another way (Better Performance) of generating random numbers without duplicates
def make_randnum_no_dups(num,lower_bound,upper_bound):
    result= []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound,upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result


