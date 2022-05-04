import pickle

from repository.student_repository import StudentRepository


class BinaryFileStudentRepository(StudentRepository):
    def __init__(self,file_name):
        super().__init__()
        self.__file_name=file_name
        self.__load_from_binary()

    def __save_to_binary(self):
        file=open(self.__file_name,"wb")
        pickle.dump(super().get_student(),file)
        file.close()

    def __load_from_binary(self):
        file=open(self.__file_name,"rb")
        try:
            students=pickle.load(file)
        except EOFError:
            students=[]
        file.close()
        for student in students:
            super().store_student(student)

    def store_student(self, student):
        super().store_student(student)
        self.__save_to_binary()

    def delete_student(self, student_id):
        super().delete_student(student_id)
        self.__save_to_binary()

    def update_student(self, student):
        super().update_student(student)
        self.__save_to_binary()