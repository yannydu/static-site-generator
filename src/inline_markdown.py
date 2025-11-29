# A Markdown parser to create TextNodes from raw Markdown string
# For now it ignores nested inline elements
import re
from typing import List, Tuple
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text:str) -> list[TextNode]:

    node = TextNode(text, TextType.TEXT)
    textnodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    textnodes = split_nodes_delimiter(textnodes, "**", TextType.BOLD)
    textnodes = split_nodes_delimiter(textnodes, "`", TextType.CODE)
    textnodes = split_nodes_image(textnodes)
    textnodes = split_nodes_link(textnodes)
    return textnodes

