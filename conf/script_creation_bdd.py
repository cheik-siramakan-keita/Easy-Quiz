import datetime
import sqlite3 as sql

now = datetime.date.today()
now = now.strftime("%d/%m/%Y") 

connexion = sql.connect('easy_quiz_bdd.db')
curseur = connexion.cursor()

curseur.execute('''
            CREATE TABLE utilisateur(
                id  INTEGER PRIMARY KEY AUTOINCREMENT, 
                pseudo TEXT,
                mot_de_passe TEXT,
                date_creation TEXT
            )
''')

curseur.execute('''
            CREATE TABLE partie(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_utilisateur TEXT,
                score INTEGER,
                date_creation TEXT,
                FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id)
            )
''')

curseur.execute('''
            CREATE TABLE type_quiz(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                date_creation TEXT
            )
''')

curseur.execute('''
            CREATE TABLE quiz(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_type INTEGER,
                question TEXT,
                reponse TEXT,
                date_creation TEXT
            )
''')

curseur.execute('''
            CREATE TABLE partie_quiz(
                partie_id INTEGER,
                quizz_id INTEGER,
                date_creation TEXT
            )
''')

curseur.execute(f'''
            INSERT INTO type_quiz(nom, date_creation)
            VALUES ('Questions à Trous', '{now}'),
                   ('Questions Vrai ou Faux', '{now}'),
                   ('Questions Customisé', '{now}')
''')

connexion.commit()
connexion.close()
