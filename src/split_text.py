from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode],
                          delimiter: str,
                          text_type:TextType) -> list[TextNode]:

    new_nodes = []
    for node in old_nodes:
        # If the node is not a text type we don't need to split it by the delimiter
        if self.text_type != TextType.TEXT:
            new_nodes.append(node)

        split_string = node.text.split(delimiter)

        @TODO: Create list of new text nodes


        
