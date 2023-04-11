import pytest
from binary_tree.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


def test_multi_level_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(40)
    tree.root.right.left = Node(-5)
    tree.root.right.right = Node(15)

    actual = tree.find_maximum_value()
    expected = 40

    assert actual == expected


def test_multi_multi_level_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(40)
    tree.root.right.left = Node(-5)
    tree.root.right.right = Node(15)
    tree.root.left.left.left = Node(62)
    tree.root.left.left.right = Node(-50)
    tree.root.left.right.left = Node(1)
    tree.root.left.right.left = Node(84)
    tree.root.right.left.right = Node(132)
    tree.root.right.right.left = Node(62)

    actual = tree.find_maximum_value()
    expected = 132

    assert actual == expected


def test_exists():
    assert BinaryTree
