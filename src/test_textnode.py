import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_link_neq(self):
        node = TextNode("This is not equal", TextType.LINK, "http://www.youtube.com")
        node2 = TextNode("This is not equal", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_type_neq(self):
        node = TextNode("this is text", TextType.LINK)
        node2 = TextNode("this is text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_neq(self):
        node = TextNode("this is text", TextType.LINK)
        node2 = TextNode("this is different text", TextType.LINK)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
