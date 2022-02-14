import datetime
from Classe.CLASSE_Type import Type

now = datetime.date.today()
now = now.strftime("%d/%m/%Y")

class Quiz:
    __id: int
    __type: Type
    __question: str
    __reponse: list = []
    __date_creation: str

    def __init__(self, id: int, type: Type, question: str, reponse: str,  date_creation: str):
        self.__id = id
        self.__type = type
        self.__question = question
        self.__reponse = reponse

        if date_creation == '':
            date_creation = now

        self.__date_creation = date_creation

    def get_id(self):
        return self.__id

    def set_id(self, _id: int):
        self.__id = _id
        return

    def get_type(self):
        return self.__type

    def set_type(self, type: Type):
        self.__type = type
        return

    def get_question(self):
        return self.__question

    def set_question(self, question: str):
        self.__question = question
        return

    def get_reponse(self):
        return self.__reponse

    def set_reponse(self, reponse:str):
        self.__reponse = reponse
        return

    def get_date_creation(self):
        return self.__date_creation

    def set_date_creation(self, date_creation: str):
        self.__date_creation = date_creation
        return

    def to_string(self):
        return f"[ID: {self.__id}, Type: {self.__type().to_string()}, Question: {self.__question}, " \
               f"Réponse: {self.__reponse}, Date Création: {self.__date_creation}]"
