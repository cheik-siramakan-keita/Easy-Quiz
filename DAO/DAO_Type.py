import datetime
from DAO.Connexion_BDD import BaseDeDonnee
from Classe.CLASSE_Type import Type

now = datetime.date.today()
now = now.strftime("%d/%m/%Y")

class DataAccessObjectType:
    @staticmethod
    def create(type: Type):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()

        curseur.execute(f"INSERT INTO type_quiz(nom, date_creation) VALUES('{type.get_nom()}', '{now}')")

        connexion.commit()
        connexion.close()
        return

    @staticmethod
    def read(nom: str = None):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()
        liste_type = []

        requete = "SELECT id, nom, date_creation FROM type_quiz"

        if nom is not None:
            requete = requete + f" WHERE nom='{nom}'"

        resultat = curseur.execute(requete)
        resultat = resultat.fetchall()

        for ligne in resultat:
            type = Type(
                ligne[0],
                ligne[1],
                ligne[2]
            )
            liste_type.append(type)

        connexion.commit()
        connexion.close()
        return liste_type

    @staticmethod
    def update(type: Type):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()

        curseur.execute(f"UPDATE type_quiz SET nom='{type.get_nom()}', WHERE id={type.get_id()}")

        connexion.commit()
        connexion.close()
        return

    @staticmethod
    def delete(type: Type):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()

        curseur.execute(f"DELETE FROM type_quiz WHERE id={type.get_id()}")

        connexion.commit()
        connexion.close()
        return
