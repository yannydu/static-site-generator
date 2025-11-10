import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is an image node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node with a url", TextType.PLAIN, "https://www.boot.com")
        node2 = TextNode("This is a text node without a url", TextType.PLAIN)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
