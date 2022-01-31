from Classe.CLASSE_Utilisateur import Utilisateur

class Partie:
    __id: int
    __utilisateur: Utilisateur
    __score: int
    __date_creation: str

    def __init__(self, utilisateur: Utilisateur, score: int, date_creation: str):
        self.__utilisateur = utilisateur
        self.__score = score
        self.__date_creation = date_creation
