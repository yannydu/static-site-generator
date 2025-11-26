# A Markdown parser to create TextNodes from raw Markdown string
# For now it ignores nested inline elements
import re
from typing import Tuple
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
    
    # Check that old node is TextType.TEXT 
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            parts = old_node.text.split(delimiter)
            if (len(parts)-1) % 2 != 0: # Check closing delim count by num of splits
                raise ValueError(f"Invalid markdown syntax") 
            else:
                for index, item in enumerate(parts):
                    if index % 2 == 0:
                        node_type = TextType.TEXT
                    else:
                        node_type = text_type
                    new_nodes.append(TextNode(item, node_type))
    return new_nodes

def extract_markdown_images(text:str) -> list[tuple[str, str]]:
    # an image has ![a](b)
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text:str) -> list[tuple[str, str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

            


