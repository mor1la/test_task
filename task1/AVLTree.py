from AVLNode import Node
from collections import deque

class AVLTree:

    # =======================
    # Базовые операции
    # =======================

    def __init__(self):
        """
        Инициализация AVL-дерева.
        Корень дерева изначально отсутствует.
        """
        self.root = None

    def get_height(self, node: Node) -> int:
        """
        Возвращает высоту узла. Если узел отсутствует, возвращает 0.
        """
        return 0 if not node else node.height

    def update_height(self, node: Node) -> None:
        """
        Обновляет высоту узла на основе высоты его потомков.
        """
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node: Node) -> int:
        """
        Возвращает баланс-фактор узла (разность высот левого и правого поддерева).
        """
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def get_min_node(self, node: Node) -> Node:
        """
        Возвращает узел с минимальным значением в поддереве.
        """
        return node if not node.left else self.get_min_node(node.left)

    def get_max_node(self, node: Node) -> Node:
        """
        Возвращает узел с максимальным значением в поддереве.
        """
        return node if not node.right else self.get_max_node(node.right)

    # =======================
    # Повороты
    # =======================

    def rotate_right(self, root: Node) -> Node:
        """
        Правый поворот вокруг узла root.
        Возвращает новую вершину, которая стала вместо root.
        """
        new_root = root.left
        moved_subtree = new_root.right

        # Выполняем поворот
        new_root.right = root
        root.left = moved_subtree

        # Обновляем высоты
        self.update_height(root)
        self.update_height(new_root)

        return new_root

    def rotate_left(self, root: Node) -> Node:
        """
        Левый поворот вокруг узла root.
        Возвращает новую вершину, которая стала вместо root.
        """
        new_root = root.right
        moved_subtree = new_root.left

        # Выполняем поворот
        new_root.left = root
        root.right = moved_subtree

        # Обновляем высоты
        self.update_height(root)
        self.update_height(new_root)

        return new_root

    def left_right_rotate(self, node: Node) -> Node:
        """
        Выполняет левый поворот вокруг левого поддерева узла,
        а затем правый поворот вокруг самого узла.
        Возвращает новую вершину, которая стала вместо исходного узла.
        """
        node.left = self.rotate_left(node.left)
        return self.rotate_right(node)

    def right_left_rotate(self, node: Node) -> Node:
        """
        Выполняет правый поворот вокруг правого поддерева узла,
        а затем левый поворот вокруг самого узла.
        Возвращает новую вершину, которая стала вместо исходного узла.
        """
        node.right = self.rotate_right(node.right)
        return self.rotate_left(node)

    def balance(self, node: Node) -> Node:
        """
        Балансировка узла node.
        В зависимости от баланс-фактора выполняется левый, правый или двойной поворот.
        """
        balance = self.get_balance(node)

        if balance == -2:
            if self.get_balance(node.right) == 1:
                return self.right_left_rotate(node)  # Большой левый поворот
            return self.rotate_left(node)  # Малый левый поворот

        if balance == 2:
            if self.get_balance(node.left) == -1:
                return self.left_right_rotate(node)  # Большой правый поворот
            return self.rotate_right(node)  # Малый правый поворот

        return node  # Если баланс в норме, возвращаем без изменений

    # =======================
    # Операции поиска, вставки, удаления
    # =======================

    def search(self, val: int) -> Node:
        """
        Ищет узел с заданным значением в дереве.
        Возвращает узел, если найден, иначе вызывает рекурсивный метод _search.
        """
        return self._search(self.root, val)

    def _search(self, node: Node, val: int) -> Node:
        """
        Рекурсивно ищет узел с заданным значением в поддереве, начиная с узла node.
        Возвращает True, если узел найден, иначе продолжает поиск в левом или правом поддереве.
        """
        if not node:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def insert(self, val: int) -> None:
        """
        Вставка нового значения в AVL-дерево.
        Значение должно быть натуральным числом.
        """
        if val <= 0:
            raise ValueError("Значение должно быть натуральным числом")
        self.root = self._insert(self.root, val)

    def _insert(self, node: Node, val: int) -> Node:
        """
        Рекурсивная вставка в поддерево с корнем node.
        Возвращает новый корень поддерева после вставки.
        """
        if not node:
            return Node(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            return node  # Дубликаты не вставляем
        self.update_height(node)
        return self.balance(node)# Балансируем поддерево


    def delete(self, val: int) -> None:
        """
        Удаление значения из AVL-дерева.
        """
        self.root = self._delete(self.root, val)

    def _delete(self, node: Node, val: int) -> Node:
        """
        Рекурсивное удаление узла со значением val.
        Возвращает новый корень поддерева после удаления.
        """
        if not node:
            return None

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_larger_node = self.get_min_node(node.right)
                node.val = min_larger_node.val
                node.right = self._delete(node.right, min_larger_node.val)

        return self.balance(node)

    # =======================
    # Дополнительные операции
    # =======================

    def merge(self, left_tree: Node, right_tree: Node) -> Node:
        """
        Сливает два поддерева в одно сбалансированное дерево.
        Возвращает корень нового дерева.
        """
        if not left_tree:
            return right_tree
        if not right_tree:
            return left_tree

        if self.get_height(left_tree) > self.get_height(right_tree):
            max_left = self.get_max_node(left_tree)
            left_tree = self._delete(left_tree, max_left.val)

            max_left.left = left_tree
            max_left.right = right_tree

            self.update_height(max_left)
            return self.balance(max_left)
        else:
            min_right = self.get_min_node(right_tree)
            right_tree = self._delete(right_tree, min_right.val)

            min_right.left = left_tree
            min_right.right = right_tree

            self.update_height(min_right)
            return self.balance(min_right)

    def split(self, root: Node, val: int):
        """
        Разделяет дерево на два поддерева: одно с элементами <= val, другое — с элементами > val.
        Возвращает два поддерева.
        """
        def traverse(node, left_elements, right_elements):
            if not node:
                return
            traverse(node.left, left_elements, right_elements)
            if node.val <= val:
                left_elements.append(node.val)
            else:
                right_elements.append(node.val)
            traverse(node.right, left_elements, right_elements)

        left_elements = []
        right_elements = []
        traverse(root, left_elements, right_elements)

        return self.build_avl(left_elements), self.build_avl(right_elements)

    def build_avl(self, arr: list) -> Node:
        """
        Строит сбалансированное AVL-дерево из отсортированного массива.
        Возвращает корень созданного дерева.
        """
        sorted_list = sorted(arr)
        if not sorted_list:
            return None

        mid = len(sorted_list) // 2
        node = Node(sorted_list[mid])
        node.left = self.build_avl(sorted_list[:mid])
        node.right = self.build_avl(sorted_list[mid+1:])
        self.update_height(node)

        return node

    # =======================
    # Статические операции
    # =======================

    def count_nodes(self) -> int:
        """
        Возвращает количество узлов в дереве.
        """
        return self._count_nodes(self.root)

    def _count_nodes(self, node) -> int:
        """
        Рекурсивно считает количество узлов в поддереве.
        """
        return 0 if not node else 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    # =======================
    # Обходы дерева (в глубину и в ширину)
    # =======================

    def inorder_traversal(self) -> list:
        """
        Возвращает список значений в дереве, отсортированный по возрастанию.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node: Node, result: list) -> None:
        """
        Рекурсивный обход дерева в порядке возрастания значений (LNR).
        """
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)

    def bfs(self) -> list:
        """
        Выполняет обход дерева в ширину и возвращает список значений узлов.
        """
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
    
    # =======================
    # Валидация дерева
    # =======================
    
    def validate_avl(self, node: Node) -> bool:
        """
        Проверяет, является ли дерево сбалансированным AVL-деревом.
        """
        return self._validate_avl(node)

    def _validate_avl(self, node: Node) -> bool:
        """
        Рекурсивно проверяет балансировку дерева.
        Возвращает True, если дерево сбалансировано, иначе False.
        """
        if not node:
            return True

        balance = self.get_balance(node)
        if abs(balance) > 1:
            return False
        return self._validate_avl(node.left) and self._validate_avl(node.right)
