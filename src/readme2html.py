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
    # return markdown.markdown(source)
    return markdown.markdown(source, extensions=['fenced_code', 'codehilite','toc'])

if __name__ == '__main__':    
    md_text = '# Hello\n\n**Text**'
    html = markdown.markdown(md_text)
    print(html)
    html = getHtml(r'C:\Users\Atharva\Desktop\Projects\project2portfolio\README.md')
    with open('example.html','w') as f:
        f.write(html)