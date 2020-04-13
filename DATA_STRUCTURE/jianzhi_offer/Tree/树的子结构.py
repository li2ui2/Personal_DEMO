"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False

        # 判断pRoot1根节点开始的树中是否有pRoot2
        def has_proot2(pRoot1, pRoot2):
            if pRoot1 == None:
                return False
            if pRoot2 == None:
                return True
            if pRoot1.val == pRoot2.val:
                if pRoot2.left == None:
                    left = True
                else:
                    left = has_proot2(pRoot1.left, pRoot2.left)
                if pRoot2.right == None:
                    right = True
                else:
                    right = has_proot2(pRoot1.right, pRoot2.right)
                return left and right
            return False

        if pRoot1.val == pRoot2.val:
            ret = has_proot2(pRoot1, pRoot2)
            if ret:
                return True
        # 再判断pRoot1的左子树中是否有pRoot2
        if self.HasSubtree(pRoot1.left, pRoot2):
            return True
        # 后判断pRoot1的右子树中是否有pRoot2
        ret = self.HasSubtree(pRoot1.right, pRoot2)
        return ret