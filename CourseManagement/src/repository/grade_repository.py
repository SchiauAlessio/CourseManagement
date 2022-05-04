from DataStructure_sort_filter.iterable import IterableDataStructure
from repository.repository_exception import RepositoryException


class GradeRepository:
    def __init__(self):
        self.__grade_list = IterableDataStructure()

    def store_grade(self, grade):
        """
        adds a grade in the grades list
        :param grade: the grade to be added
        :return: -
        """
        self.__grade_list.append(grade)

    def find_grades_by_student_id(self, student_id):
        """
        searches the grades of a student with a certain id
        raises RepositoryException in case no students with that id are graded/exist
        :param student_id: the student id that is searched
        :return: a list of grades consisting of all the grade values of the student with the specified id
        """
        grades_of_a_student = []
        for grades in self.__grade_list:
            current_student_id = grades.get_student_id()
            if current_student_id == student_id:
                grade_value = grades.get_grade_value()
                grades_of_a_student.append(grade_value)
        if len(grades_of_a_student) > 0:
            return grades_of_a_student
        raise RepositoryException("This student has no grades!")

    def find_grades_of_student_by_id(self, student_id):
        """
        searches the grades of a student with a certain id and returns a list of grade objects
        raises RepositoryException in case no students with that id are graded/exist
        :param student_id: the student id that is searched
        :return: a list of grades consisting of all the grades of the student with the specified id
        those grades are the objects, not the grade values
        """
        object_grades_list_of_a_student = []
        for grade in self.__grade_list:
            current_student_id = grade.get_student_id()
            if current_student_id == student_id:
                object_grades_list_of_a_student.append(grade)
        return object_grades_list_of_a_student

    def find_grades_at_discipline_by_id(self, discipline_id):
        """
        searches the grades of all students at a discipline with a certain id and returns a list of grade objects
        raises RepositoryException in case no disciplines with that id are graded/exist
        :param discipline_id: the discipline id that is searched
        :return: a list of grades consisting of all the grades at the discipline with the specified id
        those grades are the objects, not the grade values
        """
        object_grades_list_of_a_student = []
        for grade in self.__grade_list:
            current_discipline_id = grade.get_discipline_id()
            if current_discipline_id == discipline_id:
                object_grades_list_of_a_student.append(grade)
        return object_grades_list_of_a_student

    def find_grades_by_discipline_id(self, discipline_id):
        """
        searches the grades of all students at a discipline with a certain id
        raises RepositoryException in case no students are graded at that discipline are graded/exist
        :param discipline_id: the discipline id that is searched
        :return: a list of grades consisting of all the grades of the student at the discipline with the specified id
        """
        grades_of_a_student = []
        for grades in self.__grade_list:
            current_discipline_id = grades.get_discipline_id()
            if current_discipline_id == discipline_id:
                grade_value = grades.get_grade_value()
                grades_of_a_student.append(grade_value)
        if len(grades_of_a_student) > 0:
            return grades_of_a_student
        raise RepositoryException("This discipline has no grades!")

    def find_grade_by_discipline_andstudent_id(self, discipline_id, student_id):
        """
        searches the grade of a student at a discipline with a certain id
        raises excpetion in case no students with that id are graded/exist at that discipline
        :param discipline_id: the student id that is searched
        :return: a list of grades representing all the grades of a certain student at a certain discipline
        """
        grades_of_a_student = []
        for grades in self.__grade_list:
            current_discipline_id = grades.get_discipline_id()
            current_student_id = grades.get_student_id()
            if current_discipline_id == discipline_id and current_student_id == student_id:
                grade_value = grades.get_grade_value()
                grades_of_a_student.append(grade_value)
        if len(grades_of_a_student) > 0:
            return grades_of_a_student
        raise RepositoryException("This student has no grades at this discipline!")

    def delete_all_grades_by_student_id(self, student_id):
        """
        deletes all the grades of the student having the specified student_id
        :param student_id: the id of the student whose grades are deleted
        :return: -
        """
        index = 0
        while index < len(self.__grade_list):
            current_student_id = self.__grade_list[index].get_student_id()
            if current_student_id == student_id:
                del self.__grade_list[index]
            else:
                index = index + 1

    def delete_all_grades_by_discipline_id(self, discipline_id):
        """
        deletes all the grades at a certain discipline having the specified discipline_id
        all the grades at that discipline are deleted
        :param discipline_id: the id of the discipline at which all grades will be deleted
        :return: -
        """
        index = 0
        while index < len(self.__grade_list):
            current_discipline_id = self.__grade_list[index].get_discipline_id()
            if current_discipline_id == discipline_id:
                del self.__grade_list[index]
            else:
                index = index + 1

    def delete_grade_student_discipline_byvalue(self, discipline_id, student_id, grade_value):
        index = 0
        while index < len(self.__grade_list):
            current_discipline_id = self.__grade_list[index].get_discipline_id()
            current_student_id = self.__grade_list[index].get_student_id()
            current_grade_value = self.__grade_list[index].get_grade_value()
            if current_student_id == student_id and current_grade_value == grade_value and current_discipline_id == discipline_id:
                del self.__grade_list[index]
                break
            else:
                index = index + 1

    def get_grade(self):
        return list(self.__grade_list)

    def get_number_of_grades(self):
        return len(self.__grade_list)

    def get_graded_student_id(self):
        return self.__grade_list[0]

    def get_graded_discipline_id(self):
        return self.__grade_list[1]

    def get_grade_value(self):
        return self.__grade_list[2]
