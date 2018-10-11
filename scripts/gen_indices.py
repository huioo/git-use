import os
import re

current_path = os.path.abspath(__file__)
root_path = os.path.dirname(os.path.dirname(current_path))
target = os.path.join(root_path, 'README.md')
headline_pat = re.compile(r'#+ (?:[\d\.]{2}|A\d)')

def fprint(base, level, fmt='{0}- [{1}](#{2})'):
    print(fmt.format((level-1)*'  ', base, base.replace('.', '').replace(':', '').replace(' ', '-')))

print(target)
with open(target, 'r', encoding='utf8') as fp:
    for line in fp:
        match_obj = headline_pat.match(line)
        if not match_obj:
            continue
        title = line.strip('#').strip()
        level = len(match_obj.group())-2
        fprint(title, level)
        



