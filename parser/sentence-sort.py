#Сортирует предложения по типу (вопросительное, утвердительное, восклицательное) - и сохраняет в папку соответствующего типа

from os import listdir

res = {k: [] for k in '.!?'}
for filename in listdir(sentences):
	with open('sentences/' + filename) as f:
		f = f.read()
		res[f[-1]].append(f)
for el in res:
	for i in range(len(res[el])):
		with open('sort' + el + '/' + str(i), 'w') as f:
			f.write(f)

