import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="192.168.0.29",
  user="user",
  passwd="pass",
  database="thesaurus"
)

cursor = mydb.cursor()


def scalar(V1,V2):
    s = 0
    for i in range(len(V1)):
        s += V1[i] * V2[i]
    return s
#def setTermsCapacity(mp,request):
    
#def vectorSearch(request):
#    request
#    searchTermsWeight=dict()
#    for term in request:
#        weight=1
#        searchTermsWeight[term]=weight
#    documentsTermsWeight=map()

#    documentsTermsWeight.add(dict())
#    documentsTerms=list()#TODO получить термы документа
#    for term in documentsTerms:
#        weight=0#TODO получить вес терма
#        documentsTermsWeight[i][term]=weight
#    allDocuments=map()
#    n=0
#    for i in range(n):
#        relevant=scalar(documentsTermsWeight[i],searchTermsWeight)
#        allDocuments[i]=relevant
#    print("Векторный способ:/n")
#    print(allDocuments)
def fileTermsWeight(termsList):
    sql = """SELECT f.file_name, t.term, tof.term_count FROM Files f
    JOIN TermsOfFiles tof ON f.id = tof.file_id
    JOIN Terms t ON tof.term_id = t.id
    WHERE term IN ("""

    endSql = """)
    ORDER BY f.file_name, t.term"""
   
    wordToAdd = ""
    if len(termsList) > 0:
        for word in termsList[:50:]:
            wordToAdd = "'"+word + "',"
            sql += wordToAdd

        sql = sql[0:-1]
        sql += endSql
        cursor.execute(sql)

        res = cursor.fetchall()
    else:
        res = list()
    return res

def allTermsWeight(termsList):
    sql = """SELECT t.term, SUM(tof.term_count) FROM Files f
    JOIN TermsOfFiles tof ON f.id = tof.file_id
    JOIN Terms t ON tof.term_id = t.id
    WHERE term IN ("""

    endSql = """)
    GROUP BY f.file_name, t.term"""
   
    wordToAdd = ""
    if len(termsList) > 0:
        for word in termsList[:30:]:
            wordToAdd = "'"+word + "',"
            sql += wordToAdd

        sql = sql[0:-1]
        sql += endSql
        cursor.execute(sql)

        res = cursor.fetchall()
    else:
        res = list()
    return res

def vectorSearch(listWord):
    
    termsWeight = allTermsWeight(listWord)
    terms = list(map(lambda x: x[0], termsWeight))
    ftw = fileTermsWeight(terms)
    mapp = {}

    for row in ftw:
        if row[0] not in mapp:
            mapp.update({row[0]: [0 for i in range(len(terms))]})
        mapp[row[0]][terms.index(row[1])] = row[2]

    for key, vec in mapp.items():
        for i in range(len(vec)):
            vec[i] /= float(termsWeight[i][1])
            
    res = list(map(lambda kv: (kv[0], scalar(kv[1], [1 for i in range(len(terms))])) , mapp.items()))
    res.sort(key = lambda x: x[1])
    res.reverse()
    for row in res:
        print (row[0])
   
        