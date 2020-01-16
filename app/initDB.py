import sqlite3
from app import app

conn = sqlite3.connect(app.database_url)
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='users'")
if cursor.fetchone()[0] == 0:
	cursor.execute("""CREATE TABLE "users" (
		"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
		"username"	TEXT NOT NULL,
		"password"	TEXT NOT NULL,
		"last_survey"		INTEGER DEFAULT 0
	);
	""")
	cursor.execute("""CREATE TABLE "questions" (
		"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
		"quest"	TEXT NOT NULL,
		"type"	TEXT NOT NULL,
		"answer" TEXT NOT NULL
	);
	""")
	cursor.execute("""CREATE TABLE "answers" (
		"question_id"	INTEGER NOT NULL,
		"name"	TEXT NOT NULL,
		"value"	TEXT NOT NULL
	)
	""")
	cursor.execute("""CREATE TABLE "results" (
		"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
		"user_id"	INTEGER,
		"last_survey"	INTEGER,
		"question"	INTEGER
	);
	""")
	cursor.execute("""CREATE TABLE "ans" (
		"result_id"	INTEGER,
		"value"	TEXT
	);
	""")
	cursor.execute("INSERT INTO questions (id, quest, type, answer) VALUES (?,?,?,?)", [1,'Сколько дней в 2020 году', 'default', '366; '])
	cursor.execute("INSERT INTO questions (id, quest, type, answer) VALUES (?,?,?,?)", [2,'Самое большое млекопитающее', 'radio', 'Синий кит; '])
	cursor.execute("INSERT INTO answers (question_id, name, value) VALUES (?,?,?)", [2,'v1', 'Слон'])
	cursor.execute("INSERT INTO answers (question_id, name, value) VALUES (?,?,?)", [2,'v2', 'Синий кит'])
	cursor.execute("INSERT INTO answers (question_id, name, value) VALUES (?,?,?)", [2,'v3', 'Жираф'])
	cursor.execute("INSERT INTO questions (id, quest, type, answer) VALUES (?,?,?,?)", [3,'Какие страны входят в СНГ', 'checkbox', 'Казахстан; Украина; Молдова; '])
	cursor.execute("INSERT INTO answers (question_id, name, value) VALUES (?,?,?)", [3,'v1', 'Казахстан'])
	cursor.execute("INSERT INTO answers (question_id, name, value) VALUES (?,?,?)", [3,'v2', 'Украина'])
	cursor.execute("INSERT INTO answers (question_id, name, value) VALUES (?,?,?)", [3,'v3', 'Латвия'])
	cursor.execute("INSERT INTO answers (question_id, name, value) VALUES (?,?,?)", [3,'v4', 'Польша'])
	cursor.execute("INSERT INTO answers (question_id, name, value) VALUES (?,?,?)", [3,'v5', 'Молдова'])
	conn.commit()