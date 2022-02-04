#from Classe.CLASSE_Utilisateur import Utilisateur
from DAO.DAO_Utilisateur import DataAccessObjectUser

#utilisateur=Utilisateur('Test', 'Test', '')
#DataAccessObjectUser.create(utilisateur)
donnees = DataAccessObjectUser().read()

for ligne in donnees:
    print(ligne.to_string())