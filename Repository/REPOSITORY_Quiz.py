import datetime
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
    def recuperer():
        DAO = DataAccessObjectQuiz


        return

    @staticmethod
    def verifier_existance(quiz: Quiz):
        dao = DataAccessObjectQuiz.read(quiz.get_id())

        if len(dao) > 0:
            return True
        else:
            return False
