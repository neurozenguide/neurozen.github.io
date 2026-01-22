
file_path = 'style.css'
line_to_check = 628 # Index 628 (Line 629 in editor)

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
if line_to_check < len(lines):
    line = lines[line_to_check]
    print(f"Line {line_to_check+1} repr: {repr(line)}")
    print(f"Line {line_to_check+1} hex: {line.encode('utf-8').hex()}")
else:
    print("Line not found")
