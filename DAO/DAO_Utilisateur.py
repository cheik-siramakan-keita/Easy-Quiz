import datetime
from DAO.Connexion_BDD import BaseDeDonnee
from Classe.CLASSE_Utilisateur import Utilisateur

now = datetime.date.today()
now = now.strftime("%d/%m/%Y")

class DataAccessObjectUser:
    @staticmethod
    def create(utilisateur: Utilisateur):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()

        curseur.execute(f"INSERT INTO utilisateur(pseudo, mot_de_passe, date_creation)"
                        f"VALUES('{utilisateur.get_pseudo()}','{utilisateur.get_mot_de_passe()}', '{now}')")

        connexion.commit()
        connexion.close()
        return

    @staticmethod
    def read(pseudo: str = None):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()
        liste_utilisateur = []

        requete = "SELECT id, pseudo, mot_de_passe, date_creation FROM utilisateur"

        if pseudo is not None:
            requete = requete + f" WHERE pseudo='{pseudo}'"

        resultat = curseur.execute(requete)
        resultat = resultat.fetchall()

        for ligne in resultat:
            utilisateur = Utilisateur(
                ligne['id'],
                ligne['pseudo'],
                ligne['mot_de_passe'],
                ligne['date_creation']
            )
            liste_utilisateur.append(utilisateur)

        connexion.commit()
        connexion.close()
        return liste_utilisateur

    @staticmethod
    def update(utilisateur: Utilisateur):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()

        curseur.execute(f"UPDATE utilisateur SET pseudo='{utilisateur.get_pseudo()}', " 
                        f"mot_de_passe='{utilisateur.get_mot_de_passe()}' WHERE id={utilisateur.get_id()}")

        connexion.commit()
        connexion.close()
        return

    @staticmethod
    def delete(utilisateur: Utilisateur):
        bdd = BaseDeDonnee()
        connexion = bdd.connecter()
        curseur = connexion.cursor()

        curseur.execute(f"DELETE FROM utilisateur WHERE id={utilisateur.get_id()}")

        connexion.commit()
        connexion.close()
        return