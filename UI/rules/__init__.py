import os
import shutil

def init():
    with open("./rules/template.svg") as template_file:
        template = template_file.read()
    with open("./rules/text.svg") as text_file:
        text_template = text_file.read()    
    with open("./rules/rules.txt") as rules_file:
        rules  = rules_file.read().split("\n")
        
    #clear svg rulses folder
    svg_rules_folder = "./assets/rules"
    shutil.rmtree(svg_rules_folder)
    os.mkdir(svg_rules_folder)
    
    for i, rule in enumerate(rules):
        #create svg content
        content = []
        len_word_chunk = 5
        height = 10
        words = rule.split(" ")
        chunks = [" ".join(words[i:i+len_word_chunk]) for i in range(0, len(words), len_word_chunk)]
        total_height = len(chunks) * height
        line_height = 95 - (total_height / 2)
        for chunk in chunks:
            content.append(text_template.format(height = int(line_height), content = chunk))
            line_height += height * 2
        svg_content = template.replace("%", "\n".join(content))
        
        #save svg file
        with open(f"{svg_rules_folder}/rule{i}.svg", "w") as svg_file:
            svg_file.write(svg_content)
         
        