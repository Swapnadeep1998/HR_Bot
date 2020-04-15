import sqlite3

db = sqlite3.connect('HR_bot.db')

cr = db.cursor()
cr.execute("CREATE TABLE applicants_data(Date DATE NOT NULL, Time text NOT NULL,Name text NOT NULL, Mail_id text NOT NULL, Prefd_Jobrole text NOT NULL, Exp_pts INTEGER NOT NULL, Skills_pts INTEGER NOT NULL,Projects_pts INTEGER NOT NULL, Total_pts INETGER NOT NULL)")

db.commit()
db.close()

