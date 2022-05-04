import pickle

#from domain.discipline import Discipline
from repository.discipline_repository import DisciplineRepository


class BinaryFileDisciplineRepository(DisciplineRepository):
    def __init__(self, file_name):
        DisciplineRepository.__init__(self)
        self.__file_name = file_name
        self.__load_from_binary()


    def __save_to_binary(self):
        file=open(self.__file_name,"wb")
        pickle.dump(super().get_discipline(),file)
        file.close()

    def __load_from_binary(self):
        file=open(self.__file_name,"rb")
        try:
            disciplines=pickle.load(file)
        except EOFError:
            disciplines=[]
        file.close()
        for discipline in disciplines:
            super().store_discipline(discipline)

    # def __write_to_binary(self):
    #     with open(self.__file_name, "wb") as f:
    #         pickle.dump(self.__discipline_repository, f)

    # def __append_to_binary(self, discipline):
    #     with open(self.__file_name, "ab") as f:
    #         pickle.dump(discipline, f)

    def store_discipline(self, discipline):
        DisciplineRepository.store_discipline(self, discipline)
        self.__save_to_binary()

    def delete_discipline(self, discipline_id):
        DisciplineRepository.delete_discipline(self, discipline_id)
        self.__save_to_binary()

    def update_discipline(self,discipline):
        DisciplineRepository.update_discipline(self,discipline)
        self.__save_to_binary()

