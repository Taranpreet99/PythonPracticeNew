#Implementation of stack
class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return (self.items == [])


s = Stack()
s.push(54)
s.push("Taran")
s.push("=")

while not s.is_empty():
    print(s.pop(),end=" ")


#Evaluating postfix

def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if token == "" or token == "": #ignore empty space
            continue
        if token == "+":
            sum = stack.pop() + stack.pop() #if it is addition token, took two more tokens - added them and then onto the stack again
            stack.push(sum)
        elif token == "*":
            product = stack.pop()*stack.pop() #same thing with product now
            stack.push(product)
        else:
            stack.push(int(token)) #Conver other tokens to int or single tokens and move them back to stack
    return stack.pop() #Print the stack at the end, which should have only one operand now
