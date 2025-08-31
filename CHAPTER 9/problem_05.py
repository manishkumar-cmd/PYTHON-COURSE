words=["monkey","messi","goat"]

with open("file1.txt","r")as f:
    content=f.read()
for words in words:
    content=content.replace(words,"#"*len(words))
with open("file1.txt","w")as f:
    f.write(content)