# 783. Minimum Distance Between BST Nodes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    #      5
    #      / \
    #     9   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1

a = TreeNode(5)
b = TreeNode(9)
c = TreeNode(8)
d = TreeNode(11)
e = TreeNode(13)
f = TreeNode(4)
g = TreeNode(7)
h = TreeNode(2)
i = TreeNode(1)

a.left=b
a.right=c
b.left=d
d.left=g
d.right=h
c.left=e
c.right=f
f.right=i

class Solution:
    def minDiffInBST(self, root) -> int:
        stack = []
        def untree(root):
            if root:
                stack.append(root.val)
                untree(root.left)
                untree(root.right)
        untree(root)
        if len(stack) == 2:
            return abs(stack[0] - stack[1])

        stack.sort()
        dres = []
        for i in range(1, len(stack)):
            dres.append(stack[i] - stack[i - 1])
        return min(dres)


solver = Solution()
print(solver.minDiffInBST(a))