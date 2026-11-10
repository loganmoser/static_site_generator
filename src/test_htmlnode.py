import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props = {
                "href": "https://www.google.com",
                "target": "_blank"}
        node = HTMLNode("p", "test", None, props)
        node2 = HTMLNode("p", "test", None, props)
        self.assertEqual(node.__repr__(), node2.__repr__())

    def props_not_eq(self):
        props_1 = {
                "href": "https://www.google.com",
                "target": "_blank"
                }
        props_2 = {
                "href": "https://www.youtube.com",
                "target": "_blank"
                }
        node = HTMLNode("p", "test", None, props_1)
        node2 = HTMLNode("p", "test", None, props_2)
        self.assertNotEqual(node, node2)

    def tag_not_eq(self):
        node = HTMLNode("p")
        node2 = HTMLNode("a")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        props = {
                "href": "https://www.google.com",
                "target": "_blank"
                }
        node = HTMLNode("p", "test", None, props)
        props_str = node.props_to_html()
        correct_str = ''' href="https://www.google.com" target="_blank"'''
        self.assertEqual(props_str, correct_str)

