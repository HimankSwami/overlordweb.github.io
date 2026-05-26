import glob
import re
import os

files = glob.glob('*.html')

for fl in files:
    with open(fl, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all links
    new_content = re.sub(
        r'href="\./overlord-characters\.html"',
        'href="./index.html"',
        content
    )
    new_content = re.sub(
        r"href='\./overlord-characters\.html'",
        "href='./index.html'",
        new_content
    )

    with open(fl, 'w', encoding='utf-8') as f:
        f.write(new_content)

# Rename the file itself
if os.path.exists('overlord-characters.html'):
    os.rename('overlord-characters.html', 'index.html')

print("Renamed to index.html and updated all internal links.")
