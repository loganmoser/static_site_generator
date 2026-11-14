from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode],
                          delimiter: str,
                          text_type:TextType) -> list[TextNode]:

    new_nodes = []
    for node in old_nodes:
        # If the node is not a text type we don't need to split it by the delimiter
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_string = node.text.split(delimiter)
        if len(split_string) % 2 == 0: # Did not close with the other delimiter
            raise ValueError("String was split into an even number of pieces, there is a missing delimiter.")
        split_nodes = []

        # After splitting the nodes, alternate between adding the new node as the defined delimiter
        # text type, otherwise it is normal text
        for i, string in enumerate(split_string):
            if string == "":
                continue
            if i % 2 == 0:
               new_node = TextNode(string, TextType.TEXT)
               split_nodes.append(new_node)
            else:
                new_node = TextNode(string, text_type)
                split_nodes.append(new_node)
        
        new_nodes.extend(split_nodes)
    return new_nodes
 
