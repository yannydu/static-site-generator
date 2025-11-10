import unittest

from htmlnode import HTMLNode, LeafNode

class TextHTMLNode(unittest.TestCase):
    
    def test_init_default(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_init_values(self):
        tag = "p"
        value = "this is a text paragraph"
        chidren = [HTMLNode(), HTMLNode()]
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode(tag=tag, value=value, children=chidren, props=props)
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.children, chidren)
        self.assertEqual(node.props, props)

    def test_props_to_html(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=test_props)
        expected = ' href="https://www.google.com" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(actual, expected)

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me</a>')

