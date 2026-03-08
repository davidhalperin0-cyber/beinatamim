import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure html and body have overflow-x: hidden and width: 100%
if 'overflow-x:hidden;' not in content and 'overflow-x: hidden;' not in content:
    content = re.sub(r'html\s*\{', r'html{overflow-x:hidden;width:100%;', content)
    content = re.sub(r'body\s*\{', r'body{overflow-x:hidden;width:100%;max-width:100vw;', content)

# Header fixes
content = re.sub(r'header\{([^}]*)\}', r'header{\1 max-width:100vw; overflow-x:hidden; box-sizing:border-box;}', content)

# Check padding-inline-end in header which might cause overflow
content = re.sub(r'padding-inline-end:\s*calc\([^)]+\);', 'padding-inline-end: 5%;', content)
content = re.sub(r'padding-inline-end:\s*3rem;', 'padding-inline-end: 0.75rem;', content)

# Hero section fixes
content = re.sub(r'\.hero\{([^}]*)\}', r'.hero{\1 max-width:100%; box-sizing:border-box;}', content)

# Marquee fixes
content = re.sub(r'\.marquee\{([^}]*)\}', r'.marquee{\1 max-width:100%;}', content)

# Check for any explicit width or min-width that might cause overflow
content = re.sub(r'min-width:\s*320px;', 'min-width:100%;', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
