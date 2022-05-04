import pickle

from repository.grade_repository import GradeRepository


class BinaryFileGradeRepository(GradeRepository):
    def __init__(self,file_name):
        super().__init__()
        self.__file_name=file_name
        self.__load_from_binary()

    def __load_from_binary(self):
        file=open(self.__file_name,"rb")
        try:
            grades=pickle.load(file)
        except EOFError:
            grades=[]
        file.close()
        for grade in grades:
            super().store_grade(grade)

    def __save_to_binary(self):
        file=open(self.__file_name,"wb")
        pickle.dump(super().get_grade(),file)
        file.close()

    def store_grade(self, grade):
        super().store_grade(grade)
        self.__save_to_binary()

    def delete_all_grades_by_discipline_id(self, discipline_id):
        super().delete_all_grades_by_discipline_id(discipline_id)
        self.__save_to_binary()

    def delete_all_grades_by_student_id(self, student_id):
        super().delete_all_grades_by_student_id(student_id)
        self.__save_to_binary()

    def delete_grade_student_discipline_byvalue(self, discipline_id, student_id, grade_value):
        super().delete_grade_student_discipline_byvalue(discipline_id,student_id,grade_value)
        self.__save_to_binary()
