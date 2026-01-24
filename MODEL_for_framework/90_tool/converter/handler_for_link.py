import re

class Handler_for_Link:
    """
    A utility class for handling link conversions in HTML content.
    """

    @staticmethod
    def handle_for_link(content, from_ext, to_ext):
        """
        Handles link conversion in HTML content by replacing file extensions.

        Args:
            content: The HTML content to process
            from_ext: The source file extension to replace (e.g., ".md")
            to_ext: The target file extension (e.g., ".html")

        Returns:
            The processed HTML content with updated links
        """
        # Escape the extensions for use in regex
        escaped_from_ext = re.escape(from_ext)

        # Replace href attributes - exclude external URLs (http:// or https://)
        content = re.sub(
            rf'href="((?!https?://)[^"]+{escaped_from_ext})"',
            lambda match: f'href="{match.group(1).replace(from_ext, to_ext)}"',
            content
        )
        # Replace src attributes - exclude external URLs (http:// or https://)
        content = re.sub(
            rf'src="((?!https?://)[^"]+{escaped_from_ext})"',
            lambda match: f'src="{match.group(1).replace(from_ext, to_ext)}"',
            content
        )
        return content
