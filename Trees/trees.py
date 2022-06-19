from re import X


class Tree:
    def __init__(self,cargo,left=None,right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.cargo)

tree = Tree(1,Tree(2),Tree(3))

def print_tree(tree):
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)

def get_token(token_list,expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    x = token_list[0]
    if type(x) != type(0): return None
    del token_list[0]
    return Tree(x,None,None)

