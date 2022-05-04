from domain.grade import Grade
from domain.validators import ValidatorException
from repository.repository_exception import RepositoryException


class GradeService:
    def __init__(self, grade_repository, grade_validator,student_service,discipline_service):
        self.__grade_validator = grade_validator
        self.__grade_repository = grade_repository
        self.__student_service=student_service
        self.__discipline_service=discipline_service

    def add_grade(self, discipline_id, student_id, grade_value):
        """
        adds to the repository of grades the given grade
        both the discipline and student id are validated
        a student that does not exist can not be validated, same with discipline
        grade value is also validated
        :param discipline_id: the discipline id component of the grade to be added
        :param student_id: the student id component of the grade to be added
        :param grade_value: the value of the grade to be added
        :return:
        """
        grade = Grade(discipline_id, student_id, grade_value)
        self.__grade_validator.validate(grade,self.__student_service,self.__discipline_service)
        self.__grade_repository.store_grade(grade)

    def find_grade_list_by_student_id(self, student_id):
        """
        returns a list of grade values consisting of all the grades(values) of a student (at all disciplines)
        not the grade type, the value of the grades
        :param student_id: the id of the student whose grades are searched
        :return: a list of grade values
        """
        grades_value_list = self.__grade_repository.find_grades_by_student_id(student_id)
        return grades_value_list

    def find_grade_list_by_discipline_id(self, discipline_id):
        """
        returns a list of grade values consisting of all the grades(values) at a discipline (all disciplines)
        not the grade type, the value of the grades
        :param discipline_id: the id of the discipline at which the grades are searched
        :return: a list of grade values
        """
        grades_value_list = self.__grade_repository.find_grades_by_discipline_id(discipline_id)
        return grades_value_list

    def find_object_grade_list_by_student_id(self,student_id):
        object_grades_list=self.__grade_repository.find_grades_of_student_by_id(student_id)
        return object_grades_list

    def find_object_grade_list_at_discipline(self,discipline_id):
        object_grades_list=self.__grade_repository.find_grades_at_discipline_by_id(discipline_id)
        return object_grades_list

    def find_grade_list_by_discipline_and_student_id(self, discipline_id, student_id):
        """
        return all the grades of a specified student at a specified discipline
        :param discipline_id: the id of the discipline
        :param student_id: the id of the student
        :return: a list of grades of the specified student at the specified discipline
        """
        grades_list = self.__grade_repository.find_grade_by_discipline_andstudent_id(discipline_id, student_id)
        return grades_list

    def delete_all_grades_of_student(self,student_id):
        self.__grade_repository.delete_all_grades_by_student_id(student_id)

    def delete_all_grades_at_discipline(self,discipline_id):
        self.__grade_repository.delete_all_grades_by_discipline_id(discipline_id)

    def delete_grade_ofstudent_atdiscipline_byvalue(self,discipline_id,student_id,grade_value):
        self.__grade_repository.delete_grade_student_discipline_byvalue(discipline_id,student_id,grade_value)

    def get_all_grades(self):
        return self.__grade_repository.get_grade()

    def get_average_of_student_at_discipline(self,student_id,discipline_id):
        """
        computes the average of a specified student at a specified discipline
        :param student_id: the id of the student whose average is calculated
        :param discipline_id: the discipline at which the student is graded
        :return: float variable representing the average of the given student at the discipline
        or -1 if the student is not graded at that discipline
        """
        grade=Grade(discipline_id,student_id,4)
        try:
            self.__grade_validator.validate(grade, self.__student_service, self.__discipline_service)
        except ValidatorException:
            return -1
        except RepositoryException:
            return -1
        try:
            grades_of_a_student_at_discipline=self.__grade_repository.find_grade_by_discipline_andstudent_id(discipline_id,student_id)
        except RepositoryException:
            return -1
        sum_of_grades=0
        for grade in grades_of_a_student_at_discipline:
            sum_of_grades=sum_of_grades+grade
        student_average_at_given_discipline=sum_of_grades/len(grades_of_a_student_at_discipline)
        return student_average_at_given_discipline

    def get_aggregated_average_of_students(self):
        """
        creates o list of sub-lists formed with the student's id, their name and their aggregated average
        :return: a list of lists of sub-lists with the properties listed above
        """
        student_index = 0
        aggregated_averages_list=[]
        students_list = self.__student_service.get_all_students()
        while student_index < len(students_list):
            discipline_index = 0
            discipline_list = self.__discipline_service.get_all_disciplines()
            averages_list=[]
            student_id = students_list[student_index].get_student_id()
            while discipline_index < len(discipline_list):
                discipline_id = discipline_list[discipline_index].get_discipline_id()
                current_student_average = self.get_average_of_student_at_discipline(student_id,discipline_id)
                if current_student_average!=-1:
                    averages_list.append(current_student_average)
                discipline_index = discipline_index + 1
            if len(averages_list)>0:
                sum_averages=0
                for average in averages_list:
                    sum_averages=sum_averages+average
                student_aggregated_average=sum_averages/len(averages_list)
                student_name=students_list[student_index].get_student_name()
                to_be_added=[student_id,student_name,student_aggregated_average]
                aggregated_averages_list.append(to_be_added)
            student_index = student_index + 1
        return aggregated_averages_list

    def get_aggregated_average_at_disciplines(self):
        """
            creates o list of sub-lists formed with the discipline's id, the name and the aggregated average
            grade at that discipline
            :return: a list of sub-lists with the properties listed above
        """
        discipline_index = 0
        aggregated_averages_list = []
        disciplines_list = self.__discipline_service.get_all_disciplines()
        while discipline_index < len(disciplines_list):
            student_index = 0
            students_list = self.__student_service.get_all_students()
            averages_list = []
            discipline_id = disciplines_list[discipline_index].get_discipline_id()
            while student_index < len(students_list):
                student_id = students_list[student_index].get_student_id()
                current_discipline_average = self.get_average_of_student_at_discipline(student_id, discipline_id)
                if current_discipline_average != -1:
                    averages_list.append(current_discipline_average)
                student_index = student_index + 1
            if len(averages_list) > 0:
                sum_averages = 0
                for average in averages_list:
                    sum_averages = sum_averages + average
                discipline_aggregated_average = sum_averages / len(averages_list)
                discipline_name = disciplines_list[discipline_index].get_discipline_name()
                to_be_added = [discipline_id, discipline_name, discipline_aggregated_average]
                aggregated_averages_list.append(to_be_added)
            discipline_index = discipline_index + 1
        return aggregated_averages_list


