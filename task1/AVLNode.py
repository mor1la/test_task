class Node:
    def __init__(self, val):
        """
        Инициализация узла в AVL-дереве.

        :param val: Значение, которое будет храниться в узле.
        :param height: Начальная высота узла, равная 1 (для листа дерева).
        :param left: Ссылка на левое поддерево (изначально None).
        :param right: Ссылка на правое поддерево (изначально None).
        """
        self.val = val
        self.height = 1
        self.left = None
        self.right = None
