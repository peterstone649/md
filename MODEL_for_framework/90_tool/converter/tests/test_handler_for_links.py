import unittest
from handler_for_links import LinkHandler

class TestLinkHandler(unittest.TestCase):
    """Test cases for the LinkHandler class."""

    def test_md_to_html_conversion(self):
        """Test that .md links are converted to .html links."""
        # Test content with various .md links
        test_content = '''
        <html>
        <body>
            <a href="document.md">Link to document</a>
            <a href="path/to/file.md">Link to file</a>
            <a href="../another.md">Relative link</a>
            <img src="image.md" alt="Image">
            <a href="http://example.com/external.md">External link (should not change)</a>
            <a href="already.html">HTML link (should not change)</a>
        </body>
        </html>
        '''

        expected_content = '''
        <html>
        <body>
            <a href="document.html">Link to document</a>
            <a href="path/to/file.html">Link to file</a>
            <a href="../another.html">Relative link</a>
            <img src="image.html" alt="Image">
            <a href="http://example.com/external.md">External link (should not change)</a>
            <a href="already.html">HTML link (should not change)</a>
        </body>
        </html>
        '''

        # Apply the link handler
        result = LinkHandler.handler_for_links(test_content, ".md", ".html")

        # Check that .md links were converted to .html
        self.assertIn('href="document.html"', result)
        self.assertIn('href="path/to/file.html"', result)
        self.assertIn('href="../another.html"', result)
        self.assertIn('src="image.html"', result)

        # Check that external links and existing HTML links were not changed
        self.assertIn('href="http://example.com/external.md"', result)
        self.assertIn('href="already.html"', result)

        # Check that original .md links are no longer present (except external ones)
        self.assertNotIn('href="document.md"', result)
        self.assertNotIn('href="path/to/file.md"', result)
        self.assertNotIn('href="../another.md"', result)
        self.assertNotIn('src="image.md"', result)

    def test_multiple_extension_conversions(self):
        """Test that the handler can work with different extensions."""
        test_content = '''
        <html>
        <body>
            <a href="document.txt">Text file</a>
            <a href="data.csv">CSV file</a>
        </body>
        </html>
        '''

        # Convert .txt to .html
        result_txt = LinkHandler.handler_for_links(test_content, ".txt", ".html")
        self.assertIn('href="document.html"', result_txt)
        self.assertIn('href="data.csv"', result_txt)  # CSV should remain unchanged

        # Convert .csv to .json
        result_csv = LinkHandler.handler_for_links(test_content, ".csv", ".json")
        self.assertIn('href="document.txt"', result_csv)  # TXT should remain unchanged
        self.assertIn('href="data.json"', result_csv)

    def test_edge_cases(self):
        """Test edge cases and special scenarios."""
        # Test with empty content
        empty_result = LinkHandler.handler_for_links("", ".md", ".html")
        self.assertEqual(empty_result, "")

        # Test with no links
        no_links = "<html><body>No links here</body></html>"
        no_links_result = LinkHandler.handler_for_links(no_links, ".md", ".html")
        self.assertEqual(no_links_result, no_links)

        # Test with complex URLs
        complex_content = '''
        <a href="file.with.dots.md">Complex filename</a>
        <a href="path/with-dashes_and_underscores.md">Mixed characters</a>
        '''
        complex_result = LinkHandler.handler_for_links(complex_content, ".md", ".html")
        self.assertIn('href="file.with.dots.html"', complex_result)
        self.assertIn('href="path/with-dashes_and_underscores.html"', complex_result)

if __name__ == "__main__":
    unittest.main()
