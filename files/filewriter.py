text = "\nHello from Python"
with open('data/out.txt', 'at', encoding='utf-8') as content_file:
    content_file.write(text)
