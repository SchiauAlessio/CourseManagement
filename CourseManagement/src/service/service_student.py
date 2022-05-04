from domain.student import Student


class StudentService:
    def __init__(self, student_repository, student_validator):
        self.__student_repository = student_repository
        self.__student_validator = student_validator

    def add_student(self, student_id, student_name):
        """
        adds a student to the repository
        :param student_id: the id of the student to be added
        :param student_name: the name of the student to be added
        :return: -
        """
        student = Student(student_id, student_name)
        self.__student_validator.validate(student)
        self.__student_repository.store_student(student)

    def delete_student(self, student_id):
        """
        deletes a student from the repository having the specified id
        :param student_id: the id of the student that is deleted
        :return:-
        """
        self.__student_repository.delete_student(student_id)

    def update_student(self, student_id, student_name):
        """
        updates a student in the repository
        :param student_id: the id of the student that is modified
        :param student_name: the name of the student that is modified
        :return: -
        """
        student = Student(student_id, student_name)
        self.__student_validator.validate(student)
        self.__student_repository.update_student(student)

    def find_students_by_id(self, student_id):
        """
        returns the student with the given id
        :param student_id: the id of the student that is searched
        :return: a student with the specified id
        """
        student = self.__student_repository.find_student_by_id(student_id)
        return student

    def find_students_by_name(self, student_name):
        """
        returns a list of all the students with the given name/partial name
        :param student_name: the given name
        :return: a list of students with that name
        """
        student_list = self.__student_repository.find_student_by_name(student_name)
        return student_list

    def get_all_students(self):
        return self.__student_repository.get_student()
