import datetime

now = datetime.date.today()
now = now.strftime("%d/%m/%Y")

class Utilisateur:
    __id: int
    __pseudo: str
    __mot_de_passe: str
    __parties: list = []
    __date_creation: str

    def __init__(self, id: int, pseudo: str, mot_de_passe: str, date_creation: str):
        self.__id = id
        self.__pseudo = pseudo
        self.__mot_de_passe = mot_de_passe

        if date_creation == '':
            date_creation = now

        self.__date_creation = date_creation

    def get_id(self):
        return self.__id

    def set_id(self, _id: int):
        self.__id = _id
        return

    def get_pseudo(self):
        return self.__pseudo

    def set_pseudo(self, pseudo: str):
        self.__pseudo = pseudo
        return

    def get_mot_de_passe(self):
        return self.__mot_de_passe

    def set_mot_de_passe(self, mot_de_passe: str):
        self.__mot_de_passe = mot_de_passe
        return

    def get_parties(self):
        return self.__parties

    def set_parties(self, parties):
        self.__parties = parties
        return

    def get_date_creation(self):
        return self.__date_creation

    def set_date_creation(self, date_creation: str):
        self.__date_creation = date_creation
        return
