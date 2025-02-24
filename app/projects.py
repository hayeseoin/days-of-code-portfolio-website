import os
from markdown import markdown
import yaml
import json
import re
from pygments.formatters import HtmlFormatter
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions import codehilite

def markdown_processor(input: str) -> dict:
    '''
    Accept a file path to a markdown file. Seperates that markdown
    file into a tuple (metadata: dict, body: str)
    '''
    metadata: dict = {}
    body: dict = {}
    output: dict = {}

    with open(input, 'r') as file:
        lines: list[str] = file.readlines()

    if lines[0].strip() != '---':
        body_string: str = ''.join(lines)
        body: dict = {'body':markdown(body_string, extensions=[CodeHiliteExtension(linenums=0)])}
        output: dict = generate_title_url(metadata | body)
        return output

    frontmatter: list[str] = []
    end_frontmatter_index: int = 0
    lines.pop(0)
    for line in lines:
        if line.strip() == '---':
            end_frontmatter_index = lines.index(line) + 1
            break
        frontmatter.append(line)
    metadata: yaml = yaml.safe_load(''.join(frontmatter))

    body_string: str = ''.join(lines[end_frontmatter_index:])
    body: dict = {'body':markdown(body_string, extensions=[CodeHiliteExtension(linenums=0)])}
    output: dict = generate_title_url(metadata | body)
    return output

def generate_title_url(input: dict) -> dict:
    try:
        title_url = input.get('title').lower().replace(' ','-')
    except AttributeError:
        title_url = re.sub(r"<.*?>", "", input.get('body')[:15]).lower().replace(' ','-')
    output: dict = {'title_url': title_url}
    return input | output

    
def main() -> None:
    pass
if __name__ == "__main__":
    main()