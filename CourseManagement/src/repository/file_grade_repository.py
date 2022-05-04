from domain.grade import Grade
from repository.grade_repository import GradeRepository


class FileGradeRepository(GradeRepository):
    def __init__(self, file_name):
        GradeRepository.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        try:
            file = open(self.__file_name, "r")
        except IOError:
            print("this file does not exist!")
            return
        line = file.readline().strip()
        while line != "":
            attributes = line.split(',')
            discipline_id = int(attributes[0])
            student_id = int(attributes[1])
            grade_value = int(attributes[2])
            grade = Grade(discipline_id, student_id, grade_value)
            GradeRepository.store_grade(self, grade)
            line = file.readline().strip()
        file.close()

    def __store_to_file(self):
        file = open(self.__file_name, "w")
        grade_list = GradeRepository.get_grade(self)
        for grade in grade_list:
            discipline_id = grade.get_discipline_id()
            student_id = grade.get_student_id()
            grade_value = grade.get_grade_value()
            write_in_file = str(discipline_id) + "," + str(student_id) + "," + str(grade_value) + "\n"
            file.write(write_in_file)
        file.close()

    def store_grade(self, grade):
        GradeRepository.store_grade(self, grade)
        self.__store_to_file()

    def delete_all_grades_by_student_id(self, student_id):
        GradeRepository.delete_all_grades_by_student_id(self, student_id)
        self.__store_to_file()

    def delete_all_grades_by_discipline_id(self, discipline_id):
        GradeRepository.delete_all_grades_by_discipline_id(self, discipline_id)
        self.__store_to_file()

    def delete_grade_student_discipline_byvalue(self, discipline_id, student_id, grade_value):
        GradeRepository.delete_grade_student_discipline_byvalue(self, discipline_id, student_id, grade_value)
        self.__store_to_file()
