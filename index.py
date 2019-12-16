import mysql.connector


mydb = mysql.connector.connect(
  host="192.168.0.29",
  user="user",
  passwd="pass",
  database="thesaurus"
)

cursor = mydb.cursor()

def existTerm (term):
    cursor.execute("SELECT COUNT(term) FROM Terms WHERE term = '"+ term +"'")
    res = cursor.fetchone()
    return res[0] > 0

def existFile(file):
    cursor.execute("SELECT COUNT(file_name) FROM Files WHERE file_name = '"+ file +"'")
    res = cursor.fetchone()
    return res[0] > 0

def insert (file, terms):
    if existFile(file):
        print("file allready exist")
        return
    cursor.execute("INSERT INTO Files (file_name) VALUES ('"+ file +"')")
    cursor.execute("SELECT id FROM Files WHERE file_name = '"+ file +"'")
    fileId = cursor.fetchone()[0];
    for term, count in terms.items():
        if not existTerm(term):
            cursor.execute("INSERT INTO Terms (term) VALUES ('"+ term +"')")
            cursor.execute("INSERT INTO TermsOfFiles VALUES (" +
                str(fileId) + ", " +
                "(SELECT id FROM Terms WHERE term = '"+ term +"')," +
                str(count) +")")

    mydb.commit()

