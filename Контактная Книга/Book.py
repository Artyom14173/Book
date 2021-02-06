import sqlite3
import argparse

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
	userid INT PRIMARY KEY,
	lname text,
	fname text,
	gender text,
	tlphnnumber text,
	address text,
	other text);
""")

conn.commit()
exit = 0

parser = argparse.ArgumentParser()
parser.add_argument("--move", "-me", default = None, type = int,
					help="Введите id пользователя что бы вывести данные пользователя пример ((путь) --move 5 / -me 2)")

args = parser.parse_args()
move = args.move

if move != None:
	usertable = [(move)]
	cur.execute('''SELECT * FROM users WHERE userid = ?''', usertable)
	one_result = cur.fetchall()
	print(one_result)

while exit != 5:

	exit = int(input('Введите 1 хотите ли ввести в контактную книгу нового человека \nВведите 2 если хотите удалить человека из контактной книги\nВведите 3 если хотите заменить чьи-то данные\nВведите 4 если хотите просмотреть записи\nВведите 5 если хотите выйти из программы\n--> '))
	if exit == 4:
		cur.execute("SELECT * FROM users;")
		one_result = cur.fetchall()
		print(one_result)

	if exit == 5:
		break

	if exit == 1:
		print('Внимание, вы должны ввести id которое НЕ повторяется')
		print('Если id не написан он будет заменён на 0')
		userid = input('Введите число (id) под которым вам будет легче всего найти человека\n--> ')
		userlname = input('Введите фамилию человека\n--> ')
		username = input('Введите имя человека\n--> ')
		usergender = input('Введите пол человека\n--> ')
		usertlphnnumber = input('Введите номер телефона человека\n--> ')
		useraddress = input('Введите адрес человека\n--> ')
		userother = input('Введите другую информацию о человеке или оставьте графу пустой\n--> ')
		if userother == '':
			userother += 'Пусто'
		if userid == '':
			userid = 0
		usertable = [(userid, userlname, username, usergender, usertlphnnumber, useraddress, userother)]
		cur.executemany('''INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)''', usertable)
		conn.commit()

	if exit == 2:
		print('Введите id человека коорого хотите выписать из контактной книги')
		cur.execute('DELETE FROM users WHERE userid = ?', (str(input("--> "))))
		conn.commit()

	if exit == 3:
		print('Введите id человека у которого хотите заменить данные')
		cur.execute('DELETE FROM users WHERE userid = ?', (str(input("--> "))))
		conn.commit()
		userid = input('Введите новые\nid на которое хотите заменить\n--> ')
		userlname = input('Введите фамилию человека\n--> ')
		username = input('Введите Имя человека\n--> ')
		usergender = input('Введите пол человека\n--> ')
		usertlphnnumber = input('Введите номер телефона человека\n--> ')
		useraddress = input('Введите адрес человека\n--> ')
		userother = input('Введите другую информацию о человеке или оставьте графу пустой\n-->')
		if userother == '':
			userother = 'Пусто'
		if userid == '':
			userid = 0
		usertable = [(userid, username, userlname, usergender, usertlphnnumber, useraddress, userother)]
		cur.executemany('''INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)''', usertable)
		conn.commit()
	input('')
