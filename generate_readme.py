import os
from collections import defaultdict


def covnert_to_md(data):
    lines = []
    for header, items in data.items():
        lines.append(f"## {header.replace('_', ' ').title()}")  # Convert header to Title Case if needed
        for item in items:
            name = item.split(".md")[0]
            path = './' + header + '/' + item.replace(' ', '%20')
            lines.append(f'- [{name}]({path})')
        lines.append('\n')
    return '\n'.join(lines)


directories = [i for i in os.listdir() if os.path.isdir(i)]

problems = set()
bookmarks = defaultdict(list)
for dirt in directories:
    for file in os.listdir(dirt):
        if file.endswith('.md'):
            if file == 'README.md':
                continue
            number, name = file.split('. ')
            bookmarks[dirt].append(file)
            problems.add(file)
for h, i in bookmarks.items():
    bookmarks[h] = sorted(bookmarks[h])


with open('README.md', 'w', encoding='utf-8') as f:
    f.write('# :computer: Notes for Leetcoding. :smirk: \n\n')
    f.write(f'Total Problems: {len(problems)} \n\n')
    f.write(covnert_to_md(bookmarks))