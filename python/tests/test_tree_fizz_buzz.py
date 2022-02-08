from platform import Node
from code_challenges.trees.tree_fizz_buzz import tree_fizz_buzz, Node, check_the_tree
import pytest

def test_empty_tree_exception():
    with pytest.raises(Exception):
        head = None
        tree_fizz_buzz(head)


def test_fizz_buzz(test_tree):
    fb_tree = tree_fizz_buzz(test_tree)
    expected = ['Buzz','1','2','Fizz','4','Buzz','Fizz','7','8','Buzz','FizzBuzz']
    actual = check_the_tree(fb_tree)
    assert actual == expected


@pytest.fixture
def test_tree():
    head = Node(20)

#### 1st level of nodes ####
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.children = [node1, node2, node3]

#### 2nd Level of Nodes ####
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(10)
    node10 = Node(15)
    node1.children = [node4,node5,node6,node7]
    node2.children = [node8, node9, node10]

    return head



