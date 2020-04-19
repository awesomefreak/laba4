
class Node:
    def __init__(self , value): 
        self.value = value 
        self.left = None
        self.right = None
  
def isOperator(c): 
    if (c == '+' or c == '-' or c == '*'
        or c == '/'): 
        return True
    else: 
        return False

def printExpression(t): 
    if t is not None: 
        if t.left != None:
            print("(", end="")
        printExpression(t.left) 
        print(t.value, end="") 
        printExpression(t.right)
        if t.left != None:
            print(")", end="")

def solveExpression(t): 
    if isOperator(t.value):
        if t.value == "+":
            return solveExpression(t.left) + solveExpression(t.right)
        elif t.value == "-":
            return solveExpression(t.left) - solveExpression(t.right)
        elif t.value == "*":
            return solveExpression(t.left) * solveExpression(t.right)
        elif t.value == "/":
            return solveExpression(t.left) // solveExpression(t.right)
    else:
        return int(t.value)

  
  
def constructTree(postfix): 
    stack = []   
    for elem in postfix : 
        if not isOperator(elem): 
            t = Node(elem) 
            stack.append(t) 
        else: 
            t = Node(elem) 
            t1 = stack.pop() 
            t2 = stack.pop() 
            t.right = t1 
            t.left = t2 
            stack.append(t) 
    t = stack.pop()      
    return t   

test = "7 1 * 1 * 8 0 + 10 3 + * *"
#Построение дерева по постфиксному выражению 
r = constructTree(test.split())
print("Expression is ", end="")
printExpression(r)
print(f"\nResult of expression is {solveExpression(r)}")