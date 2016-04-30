#Берет абзацы из paragraphs и разбивает на отдельные предложения, сохраняя их в sentences

from os import listdir #this is a magical function that makes a list of files in a directory

res = []
for filename in listdir(paragraphs):
    with open(paragraphs + '/' + filename) as f:
	ns = ''
        for s in f.read():
			ns += s
            if s == '.' or s == '?' or s == '!':
                res.append(ns)
for i in range(len(res)):
    with open('sentences/' + str(i) + '.txt', 'w') as h:
        h.write(res[i])

