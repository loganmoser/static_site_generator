from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode("this is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node.__repr__())

    html_node = HTMLNode("p", "test",None,{"href": "https://www.google.com", "target": "_blank"})
    print(html_node.__repr__())


if __name__ == "__main__":
    main()
