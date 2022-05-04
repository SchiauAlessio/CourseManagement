from domain.student import Student
from repository.student_repository import StudentRepository


class FileStudentRepository(StudentRepository):
    def __init__(self, file_name):
        StudentRepository.__init__(self)
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
            student_id = int(attributes[0])
            student_name = attributes[1]
            student = Student(student_id, student_name)
            StudentRepository.store_student(self, student)
            line = file.readline().strip()
        file.close()

    def __store_to_file(self):
        file = open(self.__file_name, "w")
        student_list = StudentRepository.get_student(self)
        for student in student_list:
            student_id = student.get_student_id()
            student_name = student.get_student_name()
            write_in_file = str(student_id) + "," + str(student_name)+"\n"
            file.write(write_in_file)
        file.close()

    def store_student(self, student):
        StudentRepository.store_student(self, student)
        self.__store_to_file()

    def update_student(self, student):
        StudentRepository.update_student(self, student)
        self.__store_to_file()

    def delete_student(self, student_id):
        StudentRepository.delete_student(self, student_id)
        self.__store_to_file()

    # def find_student_by_id(self, student_id):
    #     StudentRepository.find_student_by_id(self, student_id)
    #     self.__store_to_file()
    #
    # def find_student_by_name(self, student_name):
    #     StudentRepository.find_student_by_name(self, student_name)
    #     self.__store_to_file()
