import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure html, body has max-width: 100vw instead of just 100% or 1200px
content = re.sub(r'html\s*\{[^}]*\}', r"html{scroll-behavior:smooth;overflow-x:hidden;width:100%;max-width:100vw;background:var(--cream);box-sizing:border-box;}", content)
content = re.sub(r'body\s*\{[^}]*\}', r"body{background:var(--cream);color:var(--text);font-family:'Noto Serif Hebrew',serif;overflow-x:hidden;width:100%;max-width:100vw;margin:0 auto;box-sizing:border-box;}", content)

# Check padding on sections to ensure they use box-sizing: border-box
content = content.replace("*{margin:0;padding:0;box-sizing:border-box;}", "*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}")

# Fix potential overflows from background layers, animations, etc
# 1. Split panels .split
content = re.sub(r'\.split\s*\{([^}]*)\}', r'.split{\1 max-width:100vw; overflow-x:hidden; box-sizing:border-box;}', content)

# 2. PQ section
content = re.sub(r'\.pq\s*\{([^}]*)\}', r'.pq{\1 max-width:100vw; overflow-x:hidden; box-sizing:border-box;}', content)

# 3. .strip
content = re.sub(r'\.strip\s*\{([^}]*)\}', r'.strip{\1 max-width:100vw; overflow-x:hidden; box-sizing:border-box;}', content)

# 4. .features, .how, .services, .menu, .testimonials, .cta, .social-snap
for sec in ['.features', '.how', '.services', '.menu', '.testimonials', '.cta', '.social-snap', '.info-bar', 'footer']:
    content = re.sub(fr'\{sec}\s*\{{([^}}]*)\}}', fr'{sec}{{\1 max-width:100vw; overflow-x:hidden; box-sizing:border-box;}}', content)

# 5. Fix absolute positioned overlays that might overflow
# Look for negative left/right coordinates
content = re.sub(r'right:\s*-[0-9]+%?;', 'right: 0;', content)
content = re.sub(r'left:\s*-[0-9]+%?;', 'left: 0;', content)

# 6. Specifically fix the menu::before and social-snap::before/after which had negative right/left
content = re.sub(r'\.menu::before\s*\{([^}]*)\}', r'.menu::before{\1 right: -15%; max-width: 100vw;}', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("done2")
