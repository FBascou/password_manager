import sqlite3

class Database:

	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS password_data (id INTEGER PRIMARY KEY, user TEXT, password TEXT, website TEXT)")
		self.conn.commit()
	
	def insert(self, user, password, website):
		self.cur.execute("INSERT INTO password_data VALUES (NULL, ?, ?, ?)", (user, password, website))
		self.conn.commit()

	def search(self, user="", password="", website=""):
		self.cur.execute("SELECT * FROM password_data WHERE user=? OR password=? OR website=?", (user, password, website))
		rows = self.cur.fetchall()
		return rows	

	def delete(self, id):
		self.cur.execute("DELETE FROM password_data WHERE id=?",(id,))
		self.conn.commit()

	def update(self, id, user, password, website):
		self.cur.execute("UPDATE password_data SET user=? OR password=? OR website=? WHERE id=?",(user, password, website, id))
		self.conn.commit()

	def view(self):
		self.cur.execute("SELECT * FROM password_data")
		rows = self.cur.fetchall()
		return rows	

	def __del__(self):
		self.conn.close()