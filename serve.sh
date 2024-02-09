# copy source docs
rm -rf docs/*
cp -a /Users/akshay/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/Fundamentals/. ./docs/

# copy JS
cp -r ./javascripts ./docs/

mkdocs serve
