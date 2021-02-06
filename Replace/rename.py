import os

clear = '.'
clear += input('Введите файлы у какого формата нужно заменить название\n')
file = filere = input('Введите будущее название файлов\n')

a = counter = 0

way = os.path.abspath('clear.py')

way = way[:way.rfind('\\') + 1]

print('''Файлы которые подлежат замене начинаються от''', way, '''Введите 1 если вы подтверждаете выбо
Будте аккуратнее ведь заменяются все файлы данного типа''')
chel = input()
if chel == '1':

	for i in os.walk(way):
		pass

	while len(i) > a:
		correct = (i[a])
		a += 1

	while a > 0:
		cleaner = correct[counter]
		a -= 1
		counter += 1
		file = filere
		check = cleaner[cleaner.rfind('.'):]
		if check == clear:
			file += str(counter)
			file += clear
			os.rename(cleaner, file)

input()