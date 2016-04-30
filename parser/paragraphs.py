#Разбивает статьи из articles на абзацы, сохраняет результат в paragraphs
#Убирает html-разметку
from os import listdir
res = []
for filename in listdir(articles):
	with open('articles/' + filename) as f:
		res += list(f.read().split('\n'))
for i in range(len(res)):
	with open('paragraphs/' + str(i), 'w') as h:
		h.write(res[i])

		
