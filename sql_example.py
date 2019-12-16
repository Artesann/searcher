import mysql.connector


mydb = mysql.connector.connect(
  host="192.168.0.29",
  user="user",
  passwd="pass",
  database="thesaurus"
)

cursor = mydb.cursor()



#sql = "INSERT INTO Terms (term) VALUES ('kekeson')"
#val = ("kukus")

#cursor.execute(sql)

#mydb.commit()

#print(cursor.rowcount, "was inserted.")


#cursor.execute("SELECT * FROM Terms")

#myresult = cursor.fetchall()

#for x in myresult:
#  print(x)

