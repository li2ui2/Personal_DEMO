# 通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild左孩子和rchild右孩子
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


# 树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, elem):
        """为树添加节点, 按层次添加"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        # 对已有的节点进行层次遍历
        while queue:
            # 弹出队列的第一个元素
            cur = queue.pop(0)
            if cur.lchild is None:
                cur.lchild = node
                return
            else:
                # 如果左子树不为空，加入队列继续判断
                queue.append(cur.lchild)

            if cur.rchild is None:
                cur.rchild = node
                return
            else:
                # 如果右子树不为空，加入队列继续判断
                queue.append(cur.rchild)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_order(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def mid_order(self, node):
        """中序遍历"""
        if node is None:
            return

        self.mid_order(node.lchild)
        print(node.elem, end=" ")
        self.mid_order(node.rchild)

    def post_order(self, node):
        """中序遍历"""
        if node is None:
            return

        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print("")
    tree.pre_order(tree.root)
    print("")
    tree.mid_order(tree.root)
    print("")
    tree.post_order(tree.root)





