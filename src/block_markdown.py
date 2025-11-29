import re
from enum import Enum
from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown:str) -> list[str]:

    inlines = markdown.split("\n\n")
    result = []
    for inline in inlines:
        line = inline.strip()
        result.append(re.sub(r'\n\s+', '\n', line))
    return result
