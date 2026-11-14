from extract_links import extract_markdown_images, extract_markdown_links
import unittest

class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
                "This is a text with a [link](file link here)"
                )
        self.assertListEqual([("link", "file link here")], matches)

    def test_multiple_links(self):
        matches = extract_markdown_links(
                """This has one link [here](//file/path/here.txt) and
                another [over here](//file/path/two.txt)"""
                )
        self.assertListEqual([("here", "//file/path/here.txt"), ("over here", "//file/path/two.txt")],
                             matches)
    def test_multiple_images(self):
        matches = extract_markdown_images(
                """This has an image ![here](https://www.boot.dev/img.png) and 
                ![over here](https://www.google.com/cat.jpg)""")
        self.assertListEqual([("here", "https://www.boot.dev/img.png"),
                              ("over here", "https://www.google.com/cat.jpg")
                              ], matches)
    def test_image_no_link(self):
        matches = extract_markdown_images(
                """This is an image ![here](https://www.boot.dev/img.png) and
                [here](this is a link)"""
                )
        self.assertListEqual([("here", "https://www.boot.dev/img.png")], matches)

