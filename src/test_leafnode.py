import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_eq(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), node2.to_html())

    def test_neq(self):
        node = LeafNode("a", "test call", {"href": "www.google.com"})
        node2 = LeafNode("p", "Hello, world!")
        self.assertNotEqual(node.to_html(), node2.to_html())


