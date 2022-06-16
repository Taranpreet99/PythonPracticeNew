#algorithm to remove adjacent duplicates from the list

from unit_tester import test

def remove_adjacent_dups(xs):
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result

#tests
test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a","big","big","bite","dog"]) == ["a","big","bite","dog"])