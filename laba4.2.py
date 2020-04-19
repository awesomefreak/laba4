class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
    

def buildBalancedTree(values):
    if len(values) == 0:
        return None
    else:
        tmp = Node()
        tmp.left = buildBalancedTree(values[:len(values)//2])
        tmp.value = values[len(values)//2]
        tmp.right = buildBalancedTree(values[len(values)//2 + 1:])
        return tmp
def printBalancedTree(root):
    if root == None:
        return "doesnt exist"
    else:
        print(f"{root.value} -> left-{printBalancedTree(root.left)}; right-{printBalancedTree(root.right)}")
        return root.value


if __name__ == "__main__":
    with open("laba4.2.txt") as f:
        data = [x for x in f.readline().split(" ")]
    root = buildBalancedTree(data)
    printBalancedTree(root)
    

