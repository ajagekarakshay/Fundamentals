import os
import re

def absoluteFilePaths(directory):
    files = []
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            if ".md" in f:
                files.append( os.path.abspath(os.path.join(dirpath, f)) )
    return files

files = absoluteFilePaths('docs/')

def process_equations(text):
    idxs = [m.start() for m in re.finditer('$$', text)]
    assert len(idxs) % 2 == 0

    subs = text.split("$$")
    mod_text = subs[0]

    for i in range(1, len(subs), 2):
        mod_text += "\\\[" + subs[i] + "\\\]" + subs[i+1]

    return mod_text

admonitions = ["info", "hint", "warning", "error", "note"]
def process_admonitions(text):
    pass

## Process md files
for file in files:
    with open(file) as f:
        text = f.read()
    mod_text = process_equations(file)
    with open(file, "w+") as f:
        f.write(mod_text)