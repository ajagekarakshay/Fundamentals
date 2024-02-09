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

def process_equations(file):
    with open(file) as f:
        text = f.read()
    idxs = [m.start() for m in re.finditer('$$', text)]
    assert len(idxs) % 2 == 0
    return text
    #with open(file, 'w') as f:
    #    f.write(text)

for f in files:
    text = process_equations(f)
    print(text)
    break