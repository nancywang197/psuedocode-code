import json

full_text = ""
full_code = ""
data = []


def add_indents(i, str):
    result = ""
    if i != 0:
        spaces = " " * 2 * i
        result += spaces
    result += str
    return result


with open(r'C:\Users\nancy\OneDrive\Desktop\SPoC\script\train-test.txt') as file:
    for line in file:
        split = line.split('\t')
        for s in split:
            text = split[0]
            code = split[1]
            line_num = int(split[5])
            indent = int(split[6])
        if (line_num == 0):
            data.append([full_text, full_code])
            
            full_text = ""
            full_code = ""
    
        full_text += add_indents(indent,text) + "\n"
        full_code += add_indents(indent,code) + "\n"

with open("test.json", "a") as outfile:
    json.dump(data, outfile, indent = 4)
    




