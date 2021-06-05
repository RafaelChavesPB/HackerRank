
# def build(p,i, tree):
#     left = 0 
#     right = 1
#     if i>p:
#         if tree[p][right]==-1:
#             tree[p][right]=i
#             return 1
#         else:
#             return build(tree[p][right],i,tree) + 1
#     else:
#         if tree[p][left]==-1:
#             tree[p][left]=i
#             return 1
#         else:
#             return build(tree[p][left],i,tree) + 1

# tree = []
# root = 0
# answer = 0
# n = int(input())
# for i in range(n):
#     tree.append([-1,-1])
# num = [int(x) for x in input().split()]
# for i in range(0,n):
#     if i == 0:
#         root = num[i]
#     else:
#         answer = max(build(root,num[i],tree),answer)
# print(answer)
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(no):
    if no==None:
        return -1
    return max(height(no.right) + 1,height(no.left) + 1)
    

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
