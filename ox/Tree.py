"""
    二叉树的简单实现
"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self, data_list):
        # 初始化即将传入的列表的迭代器
        self.it = iter(data_list)

    # 创建树
    def creattree(self, bt=None):
        # 获取下个元素
        try:
            next_data = next(self.it)
            # 如果列元素是 # 认为它是空的，不是节点
            if next_data is "#":
                bt = None
            else:
                bt = Node(next_data)
                bt.lchild = self.creattree()   # 创建该节点的左孩子
                bt.rchild = self.creattree()
        except StopIteration:
            print('停止创建树')
        return bt   # 这个节点左右都创建完了就返回


def pre_order(root_node):
    # 根左右
    if root_node is not None:
        print(root_node.item, end='')
        pre_order(root_node.lchild)
        pre_order(root_node.rchild)


def back_order(root_node):
    # 左右根
    if root_node is not None:
        back_order(root_node.lchild)
        back_order(root_node.rchild)
        print(root_node.item, end='')


def mid_order(root_node):
    # 左根右
    if root_node is not None:
        back_order(root_node.lchild)
        print(root_node.item, end='')
        back_order(root_node.rchild)


data = ['a', 'b', 'd', '#', '#', '#', 'c', '#', '#']

# 创建数
tree_root = Tree(data).creattree()
print('根节点', tree_root.item)
print('前序遍历', pre_order(tree_root))
print('后序', back_order(tree_root))
print('中序列', mid_order(tree_root))