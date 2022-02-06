import sqlite3

# def createDatabase():

    # run this code to create a new database with the entry (0, 0)
# import sqlite3
# connection = sqlite3.connect("resources/highscore.db")
# cursor = connection.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS highscore(id INTEGER, score INTEGER)""")
# connection.commit()
# cursor.execute("INSERT INTO highscore VALUES(0, 0)")
# connection.commit()
# cursor.execute("SELECT * FROM highscore")
# for row in cursor:
#     print(row)
# connection.commit()
# connection.close()

def newScore(scoreValue):
    
    connection = sqlite3.connect("resources/highscore.db")
    cursor = connection.cursor()
    if scoreValue > getHighscore():
        cursor.execute("""UPDATE highscore SET score = ? WHERE id = 0 """, (str(scoreValue),))
        connection.commit()
        #print("new highscore commited")
    connection.close()

def getHighscore():

    connection = sqlite3.connect("resources/highscore.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM highscore""")
    for row in cursor:
        pass
    highscore = row[1]
    connection.close()

    return highscore