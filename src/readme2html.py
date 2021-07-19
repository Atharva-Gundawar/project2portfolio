import markdown
import pathlib
from markdown.extensions.toc import TocExtension


def getHtml(filepath: str) -> str:
    """Returns Html text from markdown

    Args:
        filepath (str): Path to markdown file

    Returns:
        str: Converted Html  
    """

    source = pathlib.Path(filepath).read_text()
    source = '[TOC]\n' + source
    return markdown.markdown(source, extensions=['fenced_code', 'codehilite', 'toc', 'md_in_html'])


if __name__ == '__main__':
    html = getHtml('README.md')
    with open('example.html', 'w') as f:
        f.write(html)
