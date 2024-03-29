import datetime, random
from DAO.DAO_Type import DataAccessObjectType
from DAO.DAO_Quiz import DataAccessObjectQuiz
from Classe.CLASSE_Quiz import Quiz

now = datetime.date.today()
now = now.strftime("%d/%m/%Y")

class RepositoryQuiz:
    @staticmethod
    def enregistrer(quiz: Quiz):
        dao = DataAccessObjectQuiz()

        if RepositoryQuiz.verifier_existance(quiz):
            dao.update(quiz)
        else:
            dao.create(quiz)
        pass

    @staticmethod
    def recuperer(id_type: int = None):
        resultat = DataAccessObjectQuiz.read(id_type)
        return resultat

    @staticmethod
    def supprimer(id: int = None):

        return

    @staticmethod
    def verifier_existance(quiz: Quiz):
        dao = DataAccessObjectQuiz.read(quiz.get_id())

        if len(dao) > 0:
            return True
        else:
            return False
