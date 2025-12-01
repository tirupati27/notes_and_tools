import sys

FILE_NAME = 'notes_body.html'
COUNTER = 0

try:
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        notes_body = file.readlines()
except Exception as e:
    print(f"Error reading {FILE_NAME}: {e}")
    sys.exit(1)

def get_new_line(line: str) -> str:
    m = "<section"
    if m in line:
        start_index = line.find(m)
        end_index = line.find(">", start_index) + 1
        old_tag = line[start_index:end_index]
        global COUNTER
        COUNTER += 1
        return line.replace(old_tag, f'<section id="सेक्शन_{COUNTER}">')
    return line

try:
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        file.writelines(get_new_line(line) for line in notes_body)
    print(f"Successfully updated {FILE_NAME} with {COUNTER} sections.")
except Exception as e:
    print(f"Error writing to {FILE_NAME}: {e}")
    sys.exit(1)