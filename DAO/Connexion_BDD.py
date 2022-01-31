import sqlite3 as sql

class BaseDeDonnee:
    __chemin = 'conf/easy_quiz_bdd.db'

    def connecter(self):
        connexion = sql.connect(self.__chemin)
        return connexion
