import datetime
from DAO.DAO_Utilisateur import DataAccessObjectUser

now = datetime.date.today()
now = now.strftime("%d/%m/%Y")

class RepositoryUtilisateur:
    def enregistrer(self):
        DAO = DataAccessObjectUser()

        return