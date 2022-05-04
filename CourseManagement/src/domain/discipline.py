class Discipline:
    def __init__(self, discipline_id, discipline_name):
        self.__discipline_id = discipline_id
        self.__discipline_name = discipline_name

    def get_discipline_id(self):
        return self.__discipline_id

    def get_discipline_name(self):
        return self.__discipline_name

    def set_discipline_id(self, discipline_id):
        self.__discipline_id = discipline_id

    def set_discipline_name(self, discipline_name):
        self.__discipline_name = discipline_name

    # def __eq__(self, other_discipline):
    #     """
    #     Two disciplines are equal if they have the same discipline id so we compare the current discipline
    #     with the other one based on their id
    #     :param other_discipline: the discipline with which we compare the current discipline
    #     :return: a truth value based on whether the two are equal or not
    #     """
    #     return self.get_discipline_id() == other_discipline.get_discipline_id()

    def __str__(self):
        return str(
            "Discipline ID: " + str(self.__discipline_id) + " | " + "Discipline name: " + str(self.__discipline_name))
