#Берет абзацы из paragraphs и разбивает на отдельные предложения, сохраняя их в sentences

from os import listdir #this is a magical function that makes a list of files in a directory

res = []
for filename in listdir(paragraphs):
    with open(paragraphs + '/' + filename) as f:
        for s0 in f.split('...'):
            for s1 in s0.split('!'):
                for s2 in s1.split('?'):
                    for s3 in s2.split('.'):
                        res.append(s3)
for i in range(len(res)):
    with open('sentences/' + str(i) + '.txt', 'w') as h:
        h.write(res[i])

