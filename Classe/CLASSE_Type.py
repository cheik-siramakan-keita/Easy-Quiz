import datetime

now = datetime.date.today()
now = now.strftime("%d/%m/%Y")

class Type:
    __id: int
    __nom: str
    __date_creation: str

    def __init__(self, id: int, nom: str, date_creation: str):
        self.__id = id
        self.__nom = nom

        if date_creation == '':
            date_creation = now

        self.__date_creation = date_creation

    def get_id(self):
        return self.__id

    def set_id(self, _id: int):
        self.__id = _id
        return

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom: str):
        self.__nom = nom
        return

    def get_date_creation(self):
        return self.__date_creation

    def set_date_creation(self, date_creation: str):
        self.__date_creation = date_creation
        return

    def to_string(self):
        return f"[ID: {self.__id}, Nom: {self.__nom}, Date Création: {self.__date_creation}]"
