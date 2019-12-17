import mysql.connector
import sys
import re


mydb = mysql.connector.connect(
  host="192.168.0.29",
  user="user",
  passwd="pass",
  database="thesaurus"
)

cursor = mydb.cursor()



def existTerm (term):
    try:
        cursor.execute("SELECT COUNT(term) FROM Terms WHERE term = '"+ term +"'")
    except:
        print("sql error")
    res = cursor.fetchone()
    return res[0] > 0

def existFile(file):
    try:
        cursor.execute("SELECT COUNT(file_name) FROM Files WHERE file_name = '"+ file +"'")
    except:
        print("sql error")
    res = cursor.fetchone()
    return res[0] > 0

def insert (file, terms):
    if existFile(file):
        print("file allready exist")
        return
    try:
        cursor.execute("INSERT INTO Files (file_name) VALUES ('"+ file +"')")
        cursor.execute("SELECT id FROM Files WHERE file_name = '"+ file +"'")
    except:
        print("sql error")
    fileId = cursor.fetchone()[0];
    i = 0
    for term, count in terms.items():
        i += 1
        if (i % 50 == 0): print(i)
        if not existTerm(term):
            try:
                cursor.execute("INSERT INTO Terms (term) VALUES ('"+ term +"')")
            except:
                print("sql error")
        try:
            cursor.execute("INSERT INTO TermsOfFiles VALUES (" +
                str(fileId) + ", " +
                "(SELECT id FROM Terms WHERE term = '"+ term +"')," +
                str(count) +")")
        except:
            print("sql error")

    mydb.commit()


def read_file(file):
    map = {}
    fd = open(file, 'r')
    text = fd.read()
    text = text.lower()
    fd.close()
    for word in re.split(r'\W+', text):
        if (word):
            if word not in map:
                map.update({word : 1})
            else:
                map[word] += 1
    return map


if __name__ == '__main__':
    
    for file in sys.argv[1::]:
        insert(file, read_file(file))
        print(file + " indexed")
