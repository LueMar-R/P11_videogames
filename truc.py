import mysql.connector

class Bdd :

    @classmethod
    def connect(cls):
        cls.bdd = mysql.connector.connect(
            user='root', 
            password='root', 
            host='localhost', 
            port='8081',
            database='vgsales') 
        cls.curs = cls.bdd.cursor()

    @classmethod
    def close(cls):
        cls.curs.close()
        cls.bdd.close()


    @classmethod
    def get_con(cls):
        cls.connect()
        cls.curs.execute("call jeu_genre ('Action')", multi=True)
        test = cls.curs.fetchall()
        cls.close
        return test        



