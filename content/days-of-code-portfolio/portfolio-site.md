---
title: Portfolio Website
author: Eoin Hayes
tags:
  - 100 Days Of Code
  - Web Development
github: https://github.com/hayeseoin/days-of-code-portfolio-website
---
# Portfolio Website

This website will showcase my 100 days of code portfolio.

This is built with Flask. 

It processes markdown documents directly into HTML pages. Every portfolio project will have a github link and categories (tags) in it's metadata

The standout part for me was making the markdown processor. It takes a markdown file, extracts the YAML frontmatter, creates a URL slug from the title (in the frontmatter) and outputs a dict with everything needed to render a page. 

The frontmatter is formatted like below. The code for the markdown processor is below. 

    #!yaml
    ---
    title: Portfolio Website
    tags:
      - 100 Days Of Code
      - Web Development
    github: https://github.com/hayeseoin/days-of-code-portfolio-website
    ---
---
    #!python
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