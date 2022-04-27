import sys

def turn_clockwise(a):
    if a == "N":
        return "E"
    elif a == "E":
        return "S"
    elif a == "S":
        return "W"
    elif a == "W":
        return "N"


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(turn_clockwise("N") == "E")
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None)