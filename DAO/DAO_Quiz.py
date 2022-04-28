import datetime
from DAO.Connexion_BDD import BaseDeDonnee
from Classe.CLASSE_Type import Type
from Classe.CLASSE_Quiz import Quiz

now = datetime.date.today()
now = now.strftime("%d/%m/%Y")

class DataAccessObjectQuiz:
    @staticmethod
    def create(quiz: Quiz):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()

        type = quiz.get_type()

        curseur.execute(f"INSERT INTO quiz(id_type, question, reponse, date_creation) "
                        f"VALUES({type.get_id()},'{quiz.get_question()}', '{quiz.get_reponse()}','{now}')")

        connexion.commit()
        connexion.close()
        return

    @staticmethod
    def read(id_type: int = None):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()
        liste_quiz = []

        requete = ("SELECT quiz.id, type_quiz.id, type_quiz.nom, type_quiz.date_creation, " 
                   "quiz.question, quiz.reponse, quiz.date_creation FROM quiz " 
                   "LEFT JOIN type_quiz ON quiz.id_type = type_quiz.id")

        if id_type is not None:
            requete = requete + f" WHERE id_type={id_type}"


        requete = requete + " LIMIT 5"

        resultat = curseur.execute(requete)
        resultat = resultat.fetchall()

        for ligne in resultat:
            type = Type(ligne[1], ligne[2], ligne[3])

            quiz = Quiz(
                ligne[0],
                type,
                ligne[4],
                ligne[5],
                ligne[6]
            )
            liste_quiz.append(quiz)

        connexion.commit()
        connexion.close()
        return liste_quiz

    @staticmethod
    def update(quiz: Quiz):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()

        curseur.execute(f"UPDATE utilisateur SET id_type={quiz.get_type().get_id()}, question='{quiz.get_question()}', " 
                        f"reponse='{quiz.get_reponse()}' WHERE id={quiz.get_id()}")

        connexion.commit()
        connexion.close()
        return

    @staticmethod
    def delete(quiz: Quiz):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()

        curseur.execute(f"DELETE FROM quiz WHERE id={quiz.get_id()}")

        connexion.commit()
        connexion.close()
        return
