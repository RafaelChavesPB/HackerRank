def dfs(node,node_set,ancestor_list):
    if node == None:
        return True
    if node.data in node_set:
        return False
    for it in ancestor_list:
        if it[0]==0:
            if node.data>it[1]:
                return False
        else:
            if node.data<it[1]:
                return False
    node_set.add(node.data)
    left_ancestor_list = ancestor_list.copy()
    left_ancestor_list.append((0,node.data))
    right_ancestor_list = ancestor_list.copy()
    right_ancestor_list.append((1,node.data))
    return dfs(node.left,node_set,left_ancestor_list) and dfs(node.right,node_set,right_ancestor_list)
    
def checkBST(root):
    return dfs(root,set(),[])