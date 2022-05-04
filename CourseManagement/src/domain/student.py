class Student:
    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.__student_name = student_name

    def get_student_id(self):
        return self.__student_id

    def get_student_name(self):
        return self.__student_name

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_student_name(self, student_name):
        self.__student_name = student_name

    def __eq__(self, other_student):
        """
        checks whether two students are the same based on their unique id
        (they are the same if their id is the same)
        :param other_student: the student who is checked whether they are the same as the current student
        :return: a truth value, true or false
        """
        return self.get_student_id() == other_student.get_student_id()

    def __str__(self):
        return str("Student ID: " + str(self.__student_id) + " | " + "Student name: " + str(self.__student_name))
