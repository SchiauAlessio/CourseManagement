
from repository.repository_exception import RepositoryException



class ValidatorException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def get_errors(self):
        return self.errors


class StudentValidator:

    def validate(self, student):
        """
        throw ValidatorException if fields are empty or the id is a negative integer or = 0
        """
        errors = []
        if student.get_student_id()<=0: errors.append("ID needs to be a positive integer")
        if student.get_student_name()=="": errors.append("Name can not be empty!")
        if len(errors)>0:
            raise ValidatorException(errors)

class DisciplineValidator:

    def validate(self,discipline):
        """
            throw ValidatorException if fields are empty or the id is a negative integer or = 0
        """
        errors = []
        if discipline.get_discipline_id() <= 0: errors.append("ID needs to be a positive integer")
        if discipline.get_discipline_name() == "": errors.append("Name can not be empty!")
        if len(errors) > 0:
            raise ValidatorException(errors)

class GradeValidator():

    def validate(self,grade,student_service,discipline_service):
        """
            raise ValidatorException if the IDs are negative integers or equal to 0
            or grade is <1 or >10
            or the student/discipline the user is trying to grade does not exist in the repository
        """
        errors=[]
        try:
            student_service.find_students_by_id(grade.get_student_id())
        except RepositoryException as re:
            errors.append("There is no student with this id")
        try:
            discipline_service.find_disciplines_by_id(grade.get_discipline_id())
        except RepositoryException as re:
            errors.append("There is no discipline with this id")
        if grade.get_student_id() <= 0: errors.append("Student ID needs to be a positive integer")
        if grade.get_discipline_id() <= 0: errors.append("Discipline ID needs to be a positive integer")
        if grade.get_grade_value()<=0: errors.append("Grade needs to be a positive integer!")
        if grade.get_grade_value()>10: errors.append("Any student's grade can not exceed 10")
        if len(errors) > 0:
            raise ValidatorException(errors)
