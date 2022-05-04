from domain.discipline import Discipline


class DisciplineService:
    def __init__(self,discipline_repository,discipline_validator):
        self.__discipline_repository=discipline_repository
        self.__discipline_validator=discipline_validator

    def add_discipline(self,discipline_id,discipline_name):
        """
        adds a discipline to the repository
        :param discipline_id: the id of the discipline to be added
        :param discipline_name: the name of the discipline to be added
        :return: -
        """
        discipline=Discipline(discipline_id,discipline_name)
        self.__discipline_validator.validate(discipline)
        self.__discipline_repository.store_discipline(discipline)

    def delete_discipline(self,discipline_id):
        """
        deletes a discipline from the repository having the specified id
        :param discipline_id: the id of the discipline that is deleted
        :return:-
        """
        self.__discipline_repository.delete_discipline(discipline_id)

    def update_discipline(self,discipline_id,discipline_name):
        """
        updates a discipline in the repository
        :param discipline_id: the id of the discipline that is modified
        :param discipline_name: the name of the discipline that is modified
        :return: -
        """
        discipline=Discipline(discipline_id,discipline_name)
        self.__discipline_validator.validate(discipline)
        self.__discipline_repository.update_discipline(discipline)

    def find_disciplines_by_id(self,discipline_id):
        """
        searches for the discipline with the specified id
        :param discipline_id: the discipline id that is searched
        :return: a discipline with the specified id
        """
        discipline=self.__discipline_repository.find_discipline_by_id(discipline_id)
        return discipline

    def find_disciplines_by_name(self,discipline_name):
        """
        returns the list of all disciplines with the specified name
        :param discipline_name: the name that is searched
        :return: the list of all disciplines with that name
        """
        discipline_list=self.__discipline_repository.find_discipline_by_name(discipline_name)
        return discipline_list

    def get_all_disciplines(self):
        return self.__discipline_repository.get_discipline()
