import unittest
from parentnode import ParentNode
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        parent = ParentNode(None, [LeafNode("b", "child")])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_no_children_value(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_to_html_multiple_children(self):
        child1 = LeafNode("a", "child1")
        child2 = LeafNode("b", "child2")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(
                parent.to_html(),
                "<div><a>child1</a><b>child2</b></div>"
        )
