from DataStructure_sort_filter.filter import Filtering
from DataStructure_sort_filter.iterable import IterableDataStructure
from DataStructure_sort_filter.iterable_dictionary import IterableDataStructureDictionary
from repository.repository_exception import RepositoryException


class StudentRepository:
    def __init__(self):
        self.__student = IterableDataStructureDictionary()

    def student_list_to_dictionary(self):
        return {self.__student[index].get_student_id(): (self.__student[index].get_student_name())
                for index in range(len(self.__student))}

    def store_student(self, student):
        """
        Stores a student in the repository
        in case the id of the student to be added already exists, a RepositoryException is raised
        :param student: the student that is stored
        :return: -
        """
        if student.get_student_id() in self.__student:
            raise RepositoryException("Student ID already exists!")
        self.__student[student.get_student_id()] = student

    def delete_student(self, student_id):
        """
        deletes from the repository the student with the given id
        if the id of the student is not found an exception is raised
        :param student_id: the id of the student that needs to be deleted
        :return:-
        """
        if student_id not in self.__student:
            raise RepositoryException("No student with that ID!")
        del self.__student[student_id]

    def update_student(self, student):
        """
        updates a student from the repository (changes its name)
        if the student's id is not found an exception is raised
        :param student: the new student with which the old one is updated
        :return: -
        """
        if student.get_student_id() not in self.__student:
            raise RepositoryException("No student with that ID!")
        self.__student[student.get_student_id()] = student

    def get_size_repository_students(self):
        """
        returns how many students are stored in the repository
        """
        return len(self.__student)


    def get_student(self):
        """
        returns a list of all the students in the repository
        """

        return list(self.__student.values())

    def find_student_by_id(self, student_id):
        """
        returns the student having that id
        exception is raised if the student is not found
        :param student_id: the id of the student that is searched
        :return: the student with the given id
        """
        if student_id not in self.__student:
            raise RepositoryException("No student with that ID!")
        return self.__student[student_id]

    def find_student_by_name(self,student_name):
        """
        returns the student(s) having the specified name
        the search is case insensitive
        :param student_name: the name of the student that is searched
        :return:the student(s) having the specified name
        """
        # students_list=[]
        # for id in self.__student:
        #     if (student_name.lower() in self.__student[id].get_student_name().lower()):
        #         students_list.append(self.__student[id])
        # if len(students_list)>0:
        #     return students_list
        # raise RepositoryException("No students with that name!")

        student_list = self.get_student()
        def keep_student(student):
            return student_name.lower() in student.get_student_name().lower()

        Filtering.filter(student_list, key=keep_student)
        if len(student_list) > 0:
            return student_list
        raise RepositoryException("No students with that name!")

