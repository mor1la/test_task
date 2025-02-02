import pytest
from AVLTree import AVLTree
from AVLNode import Node

@pytest.fixture
def avl_tree():
    return AVLTree()

def test_get_height(avl_tree):
    # Тест для пустого дерева
    assert avl_tree.get_height(None) == 0

    # Тест для дерева с одним узлом
    root = Node(10)
    assert avl_tree.get_height(root) == 1
    # Тест для дерева с несколькими уровнями
    root.left = Node(5)
    root.right = Node(15)
    avl_tree.update_height(root)
    assert avl_tree.get_height(root) == 2

def test_update_height(avl_tree):
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    avl_tree.update_height(root)
    assert root.height == 2

def test_get_balance(avl_tree):
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)

    avl_tree.update_height(root.left)
    avl_tree.update_height(root.right)
    avl_tree.update_height(root)

    assert avl_tree.get_balance(root) == 0

    root.left.left = Node(2)

    avl_tree.update_height(root.left.left)
    avl_tree.update_height(root.left)
    avl_tree.update_height(root)

    assert avl_tree.get_balance(root) == 1

def test_rotate_right(avl_tree):
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    new_root = avl_tree.rotate_right(root)
    assert new_root.val == 5
    assert new_root.right.val == 10
    assert new_root.left.val == 2

def test_rotate_left(avl_tree):
    root = Node(10)
    root.right = Node(15)
    root.right.right = Node(20)
    new_root = avl_tree.rotate_left(root)
    assert new_root.val == 15
    assert new_root.left.val == 10
    assert new_root.right.val == 20

def test_insert(avl_tree):
    avl_tree.insert(10)
    assert avl_tree.root.val == 10

    avl_tree.insert(5)
    assert avl_tree.root.left.val == 5

    avl_tree.insert(15)
    assert avl_tree.root.right.val == 15

    avl_tree.insert(2)
    avl_tree.insert(1)
    assert avl_tree.root.val == 10
    assert avl_tree.root.left.val == 2
    assert avl_tree.root.right.val == 15

def test_delete(avl_tree):
    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(15)
    avl_tree.insert(2)
    avl_tree.insert(7)

    avl_tree.delete(5)
    assert avl_tree.root.left.val == 7

    avl_tree.delete(10)
    assert avl_tree.root.val == 7

def test_merge(avl_tree):
    left_tree = Node(5)
    left_tree.left = Node(2)
    left_tree.right = Node(7)

    right_tree = Node(15)
    right_tree.left = Node(12)
    right_tree.right = Node(20)

    merged_root = avl_tree.merge(left_tree, right_tree)
    assert merged_root.val == 12
    assert merged_root.left.val == 5
    assert merged_root.right.val == 15

def test_split(avl_tree):
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(20)

    left_tree, right_tree = avl_tree.split(root, 10)
    assert left_tree.val == 7
    assert right_tree.val == 15

def test_build_avl(avl_tree):
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = avl_tree.build_avl(arr)
    assert root.val == 4
    assert root.left.val == 2
    assert root.right.val == 6

def test_count_nodes(avl_tree):
    assert avl_tree.count_nodes() == 0

    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(15)
    assert avl_tree.count_nodes() == 3

def test_inorder_traversal(avl_tree):
    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(15)
    assert avl_tree.inorder_traversal() == [5, 10, 15]

def test_bfs(avl_tree):
    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(15)
    avl_tree.insert(2)
    avl_tree.insert(7)
    assert avl_tree.bfs() == [10, 5, 15, 2, 7]

def test_validate_avl(avl_tree):
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    avl_tree.update_height(root.left)
    avl_tree.update_height(root.right)
    avl_tree.update_height(root)

    assert avl_tree.validate_avl(root) == True

    root.left.left = Node(2)
    root.left.left.left = Node(1)
    avl_tree.update_height(root.left.left.left)
    avl_tree.update_height(root.left.left)
    avl_tree.update_height(root.left)
    avl_tree.update_height(root)
    
    assert avl_tree.validate_avl(root) == False
