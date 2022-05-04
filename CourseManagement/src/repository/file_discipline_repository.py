from domain.discipline import Discipline
from repository.discipline_repository import DisciplineRepository


class FileDisciplineRepository(DisciplineRepository):
    def __init__(self, file_name):
        DisciplineRepository.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        """
        read data from a file and add it to the repository
        """
        try:
            file = open(self.__file_name, "r")
        except IOError:
            print("this file does not exist!")
            return
        line = file.readline().strip()
        while line != "":
            attributes = line.split(',')
            discipline_id = int(attributes[0])
            discipline_name = attributes[1]
            discipline = Discipline(discipline_id, discipline_name)
            DisciplineRepository.store_discipline(self, discipline)
            line = file.readline().strip()
        file.close()

    def __store_to_file(self):
        file = open(self.__file_name, "w")
        discipline_list = DisciplineRepository.get_discipline(self)
        for discipline in discipline_list:
            discipline_id = discipline.get_discipline_id()
            discipline_name = discipline.get_discipline_name()
            write_in_file = str(discipline_id) + "," + str(discipline_name)+"\n"
            file.write(write_in_file)
        file.close()

    def store_discipline(self, discipline):
        DisciplineRepository.store_discipline(self, discipline)
        self.__store_to_file()

    def update_discipline(self, discipline):
        DisciplineRepository.update_discipline(self, discipline)
        self.__store_to_file()

    def delete_discipline(self, discipline_id):
        DisciplineRepository.delete_discipline(self, discipline_id)
        self.__store_to_file()

