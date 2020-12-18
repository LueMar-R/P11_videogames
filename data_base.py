import mysql.connector

class Bdd :

    @classmethod
    def connect(cls):
        cls.bdd = mysql.connector.connect(user='root', password='root', host='localhost', port="8081", database='vgsales')
        cls.curs = cls.bdd.cursor()

    @classmethod
    def close(cls):
        cls.curs.close()
        cls.bdd.close()

    @classmethod
    def get_v_ventes(cls):
        cls.connect()
        cls.curs.execute("select * from v_ventes")
        for result in cls.curs.stored_results():
            return result.fetchall()
        cls.close()

    @classmethod
    def jeux_genre(cls, genre):
        cls.connect()
        cls.curs.callproc("jeu_genre", [genre])
        for result in cls.curs.stored_results():
            return result.fetchall()
        cls.close()

    @classmethod
    def jeux_publisher(cls, publisher):
        cls.connect()
        cls.curs.callproc("jeu_publisher", [publisher])
        for result in cls.curs.stored_results():
            return result.fetchall()
        cls.close()

    @classmethod
    def jeux_plateforme(cls, plateforme):
        cls.connect()
        cls.curs.callproc("jeu_plateforme", [plateforme])
        for result in cls.curs.stored_results():
            return result.fetchall()
        cls.close()

    @classmethod
    def date_fixe(cls, annee):
        cls.connect()
        cls.curs.callproc("jeu_date_fixe", [annee])
        for result in cls.curs.stored_results():
            return result.fetchall()
        cls.close()

    @classmethod
    def date_sup(cls, annee):
        cls.connect()
        cls.curs.callproc("jeu_date_sup", [annee])
        for result in cls.curs.stored_results():
            return result.fetchall()
        cls.close()

    @classmethod
    def date_inf(cls, annee):
        cls.connect()
        cls.curs.callproc("jeu_date_inf", [annee])
        for result in cls.curs.stored_results():
            return result.fetchall()
        cls.close()

    @classmethod
    def global_inf(cls, montant_en_million):
        cls.connect()
        cls.curs.callproc("jeu_global_inf", [montant_en_million])
        for result in cls.curs.stored_results():
            return result.fetchall()
        cls.close()

    @classmethod
    def global_inf(cls, montant_en_million):
        cls.connect()
        cls.curs.callproc("jeu_global_inf", [montant_en_million])
        for result in cls.curs.stored_results():
            return result.fetchall()
        cls.close()

    @classmethod
    def get_truc(cls):
        cls.connect()
        cls.curs.execute("select * from genre")
        test = cls.curs.fetchall()
        cls.close
        return test      

print(Bdd.get_truc())
