import re

file_path = "C:\\Users\\Hassler\\.gemini\\antigravity\\scratch\\neuro-zen-website\\style.css"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix common merged values
# padding: 100px0 -> 100px 0
content = re.sub(r'(\d+)px(\d+)', r'\1px \2', content)

# solidrgba -> solid rgba
content = re.sub(r'solidrgba', 'solid rgba', content)

# pxrgba -> px rgba
content = re.sub(r'(\d+)pxrgba', r'\1px rgba', content)

# solid# -> solid #
content = re.sub(r'solid#', 'solid #', content)

# 0%comma -> 0%,
content = re.sub(r'0%,#', '0%, #', content) # general case: 0%,# -> 0%, #

# 100%); -> 100%); (already ok usually, but check for 100%#)
content = re.sub(r'100%#', '100% #', content)

# Specific selector merges seen in the file
content = content.replace('.mission-cardp', '.mission-card p')
content = content.replace('.mission-cardh3', '.mission-card h3')

# Fix background gradients missing spaces
# #0201050% -> #020105 0%
content = re.sub(r'(#[0-9a-fA-F]{6})(\d+%)', r'\1 \2', content)

# Fix padding: 100px0 specifically if regex missed
content = content.replace('padding: 100px0;', 'padding: 100px 0;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed CSS syntax in {file_path}")
