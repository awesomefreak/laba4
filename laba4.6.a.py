
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

def simplifyTree(root):
    if root == None:
        return None
    else:
        simplifyTree(root.left)
        simplifyTree(root.right)
        if root.value == "+" or root.value == "-":
            if root.left.value == "0":
                root.value = root.right.value
                root.left = root.right.left
                root.right = root.right.right
            if root.right.value == "0":
                root.value = root.left.value
                root.right = root.left.right
                root.left = root.left.left
        if root.value == "*":
            if root.left.value == "1":
                root.value = root.right.value
                root.left = root.right.left
                root.right = root.right.right
            if root.right.value == "1":
                root.value = root.left.value
                root.right = root.left.right
                root.left = root.left.left
        if root.value == "*":
            if root.left.value == "0" or root.right.value == "0":
                root.value = "0"
                root.left = None
                root.right = None
        return root



  

test = "a 1 * 1 * a 0 + d 3 + * *"
#Построение дерева по постфиксному выражению 
r = constructTree(test.split())
print("Original expression is")
printExpression(r)
sr = simplifyTree(r)
print("\nSimplified expression is")
printExpression(sr) 