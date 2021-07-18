import markdown
import pathlib 

def getHtml(filepath: str) -> str:
    """Returns Html text from markdown

    Args:
        filepath (str): Path to markdown file

    Returns:
        str: Converted Html  
    """

    source = pathlib.Path(filepath).read_text()
    return markdown.markdown(source)

if __name__ == '__main__':    
    md_text = '# Hello\n\n**Text**'
    html = markdown.markdown(md_text)
    print(html)
    print(getHtml(r'C:\Users\Atharva\Desktop\Projects\project2portfolio\PROJECTINFO.md'))