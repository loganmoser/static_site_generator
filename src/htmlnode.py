class HTMLNode():
    def __init__(self, 
                 tag: str = None, 
                 value: str = None,
                 children: list[HTMLNode] = None, 
                 props: dict[str:str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            return "".join(f' {k}="{v}"' for k,v in self.props.items())
        else:
            return ""

    def to_html(self):
        raise NotImplementedError

    def __repr__(self):
        print(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict[str:str] = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return f"{self.value}"
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        tag_part = f"<{self.tag}"
        props_str = "".join(f'{k}="{v}"' for k,v in self.props.items())
        props_part = f' {props_str}">'
        value_part = f'{self.value}'
        tag_closing = f"</{self.tag}>"
        return tag_part + props_part + value_part + tag_closing

    def __repr__(self):
        print(f"LeafNode({self.tag}, {self.value}, {self.props}")
