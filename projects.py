import os
from markdown import markdown
import yaml
import json
    
def projects_json() -> None:
    project_list = [
        f'./projects/{entry}' for entry
        in os.listdir('projects')
        ]
    projects_db = []
    for entry in project_list:
        md_file = markdown_meta(entry)
        result: dict = md_file[0]
        result['body'] = md_file[1]
        projects_db.append(result)
    with open('projects_db.json', 'w') as file:
        json.dump(projects_db, file, indent=4)


def markdown_meta(input: str) -> tuple[dict, str]:
    '''
    Accept a file path to a markdown file. Seperates that markdown
    file into a tuple (metadata: dict, body: str)
    '''
    metadata = {}
    with open(input, 'r') as file:
        lines: list[str] = file.readlines()

    if lines[0].strip() != '---':
        body: str = ''.join(lines)
        return metadata, markdown(body)

    frontmatter: list[str] = []
    end_frontmatter_index: int = 0
    lines.pop(0)
    for line in lines:
        if line.strip() == '---':
            end_frontmatter_index = lines.index(line) + 1
            break
        frontmatter.append(line)
    metadata: yaml = yaml.safe_load(''.join(frontmatter))
    body: str = ''.join(lines[end_frontmatter_index:])
    return metadata, markdown(body)
    
def main() -> None:
    projects_json()

if __name__ == "__main__":
    main()