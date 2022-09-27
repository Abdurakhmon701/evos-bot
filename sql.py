import sqlite3

connect = sqlite3.connect("Telegram-bot.db")
cursor = connect.cursor()


def tablitsa():
	"foydalanuvchilar tablitsasini hosil qilish "
	cursor.execute("""CREATE TABLE IF NOT EXISTS Foydalanuvchilar (
		id Integer PRIMARY KEY AUTOINCREMENT,
		idisi varchar(20), 
		ismi varchar(20),
		taxallusi varchar(25),
		raqami varchar(15) NULL,
		joylashuvi_x varchar(30) NULL,
		joylashuvi_y varchar(30) NULL
		 )""")

def qushish(idi,ism,taxallus):
	'foydalanuvchilarni qushish'
	cursor.execute(f"INSERT INTO Foydalanuvchilar (idisi,ismi,taxallusi) VALUES ('{idi}','{ism}','{taxallus}')")
	return connect.commit()

def selekt_id(idisi):
	"Id bo'yicha olib beradi"
	cursor.execute(f"SELECT * FROM Foydalanuvchilar where idisi = {idisi}")
	info = cursor.fetchall()
	return info

def raqam_qushish(raqami,idisi):
	cursor.execute(f"UPDATE Foydalanuvchilar SET raqami = '{raqami}' where idisi = '{idisi}'")
	return connect.commit()

def location_qushish(x,y,idisi):
	cursor.execute(f"UPDATE Foydalanuvchilar SET joylashuvi_x = '{x}',joylashuvi_y = '{y}' where idisi = '{idisi}'")
	return connect.commit()



# connect.commit()
# connect.close()