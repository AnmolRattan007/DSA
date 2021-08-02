


class Node:
    def __init__(self,data:int):
        self.data = data
        self.left = None
        self.right = None


def level_traversal(root:Node,k):

    q = list()
    q.append(root)
    q.append(None)
    level = 0
    ans = 0

    while len(q) != 0 and level!=k:
        val = q.pop(0)
        if val:
            print(val)
            if val.left:
                q.append(val.left)
            elif val.right:
                q.append(val.right)
        else:
            if len(q) == 0:
                return
            else:
                level += 1
                q.append(None)
                continue

    if level == k:
        for val in q:
            ans += val
        return ans

    return ans

def tree_height(root:Node):
    if root:
        return max(tree_height(root.left),tree_height(root.right)) + 1
    else:
        return 0

def diameter_tree(root:Node):
    if root:
        lheight = tree_height(root.left)
        rheight = tree_height(root.right)
        currheight = lheight+rheight+1
        ldia = diameter_tree(root.left)
        rdia = diameter_tree(root.right)
        return max(currheight,max(ldia,rdia)) + 1
    else:
        return 0

def zigzag_traversal(root:Node):
    q =list()
    traverse_left = False
    q.append(root)
    while len(q)!=0:
        n = q.pop()
        if traverse_left:
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
            traverse_left = False
        else:
            if n.right:
                q.append(n.right)
            if n.left:
                q.append(n.left)
            traverse_left = True


