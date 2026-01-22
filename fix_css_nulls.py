
file_path = 'style.css'
start_line_idx = 627 # Line 628
end_line_idx = 932   # Line 933

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixed_lines = []
for i, line in enumerate(lines):
    if start_line_idx <= i < end_line_idx:
        # Remove null bytes
        s = line.replace('\x00', '')
        fixed_lines.append(s)
    else:
        fixed_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("Fixed CSS file by removing null bytes.")
