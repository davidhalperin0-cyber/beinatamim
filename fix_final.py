import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure html/body are truly constrained to 100% and overflow-x hidden
if 'html, body' not in text:
    text = re.sub(r'<style>', '<style>\nhtml, body { overflow-x: hidden !important; width: 100% !important; max-width: 100% !important; margin: 0; padding: 0; }\n*, *::before, *::after { box-sizing: border-box !important; }\n', text)

# The hero filter scaling might push things out, so ensure hero overflow is hidden
text = text.replace('.hero{', '.hero{overflow:hidden;')
text = text.replace('.strip{', '.strip{overflow:hidden;')

# Search for any width: 100vw; and change it to 100%
text = text.replace('width:100vw', 'width:100%')

# Add one global wrap just to be safe if any specific child breaks it
text = text.replace('</head>\n<body>', '</head>\n<body>\n<div style="overflow-x:hidden;width:100%;max-width:100%;position:relative;">')
text = text.replace('</body>\n</html>', '</div>\n</body>\n</html>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done9")
