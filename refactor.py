import os
import glob
import re

directories = ['model_paper_based', 'old_syllabus_paper_based']

for d in directories:
    for filepath in glob.glob(os.path.join(d, "*.md")):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = []
        for i, line in enumerate(lines):
            line_str = line.rstrip('\n')
            clean_line = re.sub(r'\s*<br>\s*$', '', line_str.rstrip())
            
            # Check if this line is an option (A., B., C., D., E.)
            is_option = re.match(r'^[A-E]\.\s+', clean_line)
            
            # Look ahead for option A.
            is_next_line_option_A = False
            if i + 1 < len(lines):
                next_clean = re.sub(r'\s*<br>\s*$', '', lines[i+1].rstrip('\n').rstrip())
                if re.match(r'^A\.\s+', next_clean):
                    is_next_line_option_A = True
            
            if is_option:
                new_lines.append(clean_line + ' <br>\n')
            elif is_next_line_option_A and clean_line and not clean_line.endswith('```'):
                new_lines.append(clean_line + '  <br>\n')
            else:
                new_lines.append(line)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
