from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# ---------Solution--------------
class Solution:
    def pathSum(self, root, sum):
        if not root: return []
        if root.left == None and root.right == None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        a = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in a]

    #----Input-------------------------------------------------
    def generateTrees(self, n: int):
        D = {(1, 0): []}
        for s in range(n, 0, -1):
            for e in range(s, n + 1):
                D[(s, e)] = []
                for i in range(s, e + 1):
                    if s > i - 1:  # 左邊為null
                        D[(s, i - 1)] = [None]
                    for l in D[(s, i - 1)]:
                        if i + 1 > e:  # 右邊為null
                            D[(i + 1, e)] = [None]
                        for r in D[(i + 1, e)]:
                            t = TreeNode(i)
                            t.left, t.right = l, r
                            D[(s, e)].append(t)
        return D[(1, n)]
    def levelOrder(self, root: TreeNode):
        if not root: return []
        dq = deque([(0, root)])
        Ans = [[]]
        while dq:
            level, node = dq.popleft()
            if level == len(Ans):
                Ans.append([])
            Ans[level].append(node.val)
            if node.left:
                dq.append([level+1, node.left])
            if node.right:
                dq.append([level+1, node.right])
        return Ans
#----Input---------
# -----------Testing(Output)--------------
S = Solution()
I = S.generateTrees(6)
i = I[117]
#for i in I:
print(S.levelOrder(i))
print(S.pathSum(i,15))