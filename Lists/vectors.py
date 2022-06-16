import sys

def add_vectors(u, v):
    new_list = []
    if len(u) == len(v):
        for i in range(len(u)):
            num = u[i] + v[i]
            new_list.insert(i,num)
    return new_list

lista = [1,2,3]
listb = [4,5,6]
add_a_b = add_vectors(lista,listb)
for i in add_a_b:
    print(i)


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([2, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])