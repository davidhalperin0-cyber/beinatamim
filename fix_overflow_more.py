import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix header media query that had width:100vw and overflow-x:hidden which clips the logo
header_media_match = r'@media\(max-width:900px\)\{\s*header\{[^}]*\}'
new_header_media = '''@media(max-width:900px){
  header{
    padding-inline:0.75rem;
    min-height:72px;
    flex-wrap:nowrap;
    direction:rtl;
    width:100%;
    box-sizing:border-box;
  }'''
text = re.sub(header_media_match, new_header_media, text)

# Remove explicit max-width:100vw!important from everywhere except html/body globally
# The problem is that max-width:100vw doesn't account for scrollbars! Use 100% instead!
text = text.replace('max-width:100vw', 'max-width:100%')

# Fix background radial gradients that bleed off-screen on the right/left
text = re.sub(r'right:\s*-[0-9]+%?;\s*width:\s*500px;\s*height:\s*500px;', r'right:0;width:500px;height:500px;max-width:100%;', text)
text = re.sub(r'left:\s*-[0-9]+%?;\s*width:\s*500px;\s*height:\s*500px;', r'left:0;width:500px;height:500px;max-width:100%;', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done8")
