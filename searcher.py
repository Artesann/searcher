import mysql.connector


mydb = mysql.connector.connect(
  host="192.168.0.29",
  user="user",
  passwd="pass",
  database="thesaurus"
)

cursor = mydb.cursor()

def boolSearch(wordList):
    sql = """SELECT f.file_name FROM Files f
    JOIN TermsOfFiles tof ON f.id = tof.file_id
    JOIN Terms t ON tof.term_id = t.id
    WHERE term IN ("""

    endSql = """)
    GROUP BY f.file_name
    ORDER BY COUNT(f.id) DESC;"""
    wordToAdd = ""
    for word in wordList:
        wordToAdd = "'"+word + "',"
        sql += wordToAdd

    sql = sql[0:-1]
    sql += endSql
    cursor.execute(sql)

    res = cursor.fetchall()
    res = list(map(lambda x: x[0], res))

    return res