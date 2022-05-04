from DataStructure_sort_filter.filter import Filtering
from DataStructure_sort_filter.iterable import IterableDataStructure
from DataStructure_sort_filter.iterable_dictionary import IterableDataStructureDictionary
from repository.repository_exception import RepositoryException


class DisciplineRepository:
    def __init__(self):
        self.__discipline = IterableDataStructureDictionary()

    def discipline_list_to_dictionary(self):
        return {self.__discipline[index].get_discipline_id(): (self.__discipline[index].get_discipline_name())
                for index in range(len(self.__discipline))}

    def store_discipline(self, discipline):
        """
        Stores a discipline in the repository
        in case the id of the discipline to be added already exists, a RepositoryException is raised
        :param discipline: the discipline that is stored
        :return: -
        """
        if discipline.get_discipline_id() in self.__discipline:
            raise RepositoryException("Discipline ID already exists!")
        self.__discipline[discipline.get_discipline_id()] = discipline

    def delete_discipline(self, discipline_id):
        """
        deletes from the repository the discipline with the given id
        if the id of the discipline is not found an exception is raised
        :param discipline_id: the id of the discipline that needs to be deleted
        :return:-
        """
        if discipline_id not in self.__discipline:
            raise RepositoryException("No discipline with that ID!")
        del self.__discipline[discipline_id]

    def update_discipline(self, discipline):
        """
        updates a discipline from the repository (changes its name)
        if the discipline's id is not found an exception is raised
        :param discipline: the new discipline with which the old one is updated
        :return: -
        """
        if discipline.get_discipline_id() not in self.__discipline:
            raise RepositoryException("No discipline with that ID!")
        self.__discipline[discipline.get_discipline_id()] = discipline

    def get_size_repository_disciplines(self):
        """
        returns how many disciplines are stored in the repository
        """
        return len(self.__discipline)


    def get_discipline(self):
        """
        returns a list of all the disciplines in the repository
        """

        return list(self.__discipline.values())

    def find_discipline_by_id(self, discipline_id):
        """
        returns the discipline having that id
        exception is raised if the discipline is not found
        :param discipline_id: the id of the discipline that is searched
        :return: the discipline with the given id
        """
        if discipline_id not in self.__discipline:
            raise RepositoryException("No discipline with that ID!")
        return self.__discipline[discipline_id]

    def find_discipline_by_name(self,discipline_name):
        """
        returns the discipline(s) having the specified name
        the search is case insensitive and also partial string matching
        :param discipline_name: the name of the discipline that is searched
        :return: a list of disciplines having the specified name (even partially)
        """
        discipline_list = self.get_discipline()

        def keep_discipline(discipline):
            return discipline_name.lower() in discipline.get_discipline_name().lower()

        Filtering.filter(discipline_list, key=keep_discipline)
        if len(discipline_list) > 0:
            return discipline_list
        raise RepositoryException("No disciplines with that name!")
        # discipline_list = []
        # for id in self.__discipline:
        #     if (discipline_name.lower() in self.__discipline[id].get_discipline_name().lower()):
        #         discipline_list.append(self.__discipline[id])
        # if len(discipline_list) > 0:
        #     return discipline_list
        # raise RepositoryException("No disciplines with that name!")

