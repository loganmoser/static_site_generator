from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children, props: dict = None):
       super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        if not self.children or len(self.children) == 0:
            raise ValueError("There are no children for this parent node, meaning it is a leaf node.")

        html_rep = f"<{self.tag}"
        if self.props:
            html_rep += " " + "".join(f'{k}="{v}"' for k,v in self.props.items())
        html_rep += ">"
        for child in self.children:
            html_rep += child.to_html()

        html_rep += f"</{self.tag}>"

        return html_rep
