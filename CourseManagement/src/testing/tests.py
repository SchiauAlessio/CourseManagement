import unittest

from domain.discipline import Discipline
from domain.grade import Grade
from domain.student import Student
from domain.validators import ValidatorException, StudentValidator, DisciplineValidator, GradeValidator
from repository.discipline_repository import DisciplineRepository
from repository.grade_repository import GradeRepository
from repository.repository_exception import RepositoryException
from repository.student_repository import StudentRepository
from service.service_discipline import DisciplineService
from service.service_grade import GradeService
from service.service_student import StudentService
#import math

class Tests(unittest.TestCase):
    def test_Discipline_class(self):
        discipline1_id = 1
        discipline1_name = "math"
        discipline1 = Discipline(discipline1_id, discipline1_name)
        self.assertEqual(discipline1.get_discipline_id(),1)
        self.assertEqual (discipline1.get_discipline_name(),"math")
        discipline2 = Discipline(discipline1_id, "asc")
        #self.assertEqual(discipline1,discipline2)
        self.assertEqual (str(discipline1), "Discipline ID: 1 | Discipline name: math")

    def test_Student_class(self):
        student1_id = 1
        student1_name = "Marcel"
        student1 = Student(student1_id, student1_name)
        self.assertEqual (student1.get_student_id(),1)
        self.assertEqual (student1.get_student_name(), "Marcel")
        student2 = Student(student1_id, "mario")
        self.assertEqual (student1 ,student2)
        self.assertEqual (str(student1) , "Student ID: 1 | Student name: Marcel")

    def test_Grade_class(self):
        discipline1_id = 1
        student1_id = 1
        grade1_value = 1
        grade1 = Grade(discipline1_id, student1_id, grade1_value)
        self.assertEqual (grade1.get_grade_value() , 1)
        self.assertEqual (grade1.get_student_id() , 1)
        self.assertEqual (grade1.get_discipline_id() , 1)
        self.assertEqual (str(grade1), "Discipline ID: 1 | Student ID: 1 | Grade value: 1")

    def testStudentValidator(self):
        validator = StudentValidator()
        student = Student(0, "")
        #try:
        self.assertRaises(ValidatorException,validator.validate,student)
        #    assert False
        #except ValidatorException as ex:
        #    assert len(ex.get_errors()) == 2
        student = Student(-4, "lalala")
        try:
            validator.validate(student)
            self.assertFalse('should not have happened')
        except ValidatorException as ex:
            self.assertEqual (len(ex.get_errors()) , 1)
        student = Student(1, "Ion")
        try:
            validator.validate(student)
            self.assertTrue('correct')
        except ValidatorException as ex:
            self.assertFalse('exception should not have been raised')  # in case it finds an exception although it should not

    def test_DisciplineValidator(self):
        validator = DisciplineValidator()
        discipline = Discipline(0, "")
        try:
            validator.validate(discipline)
            self.assertFalse('should raise exception')
        except ValidatorException as ex:
            self.assertEqual (len(ex.get_errors()) , 2)

        discipline = Discipline(-4, "lalala")
        try:
            validator.validate(discipline)
            self.assertFalse('should raise exception')
        except ValidatorException as ex:
            self.assertEqual (len(ex.get_errors()) ,1)

        discipline = Discipline(1, "jdsbchsdj")
        try:
            validator.validate(discipline)
            self.assertTrue('good')
        except ValidatorException as ex:
            self.assertFalse('should not have raised exception')  # in case it finds an exception although it should not

    def testGradeValidator(self):
        student_validator = StudentValidator()
        student_repository = StudentRepository()
        student_service = StudentService(student_repository, student_validator)
        student_service.add_student(1, "Cosmin Semenciuc")

        discipline_validator = DisciplineValidator()
        discipline_repository = DisciplineRepository()
        discipline_service = DisciplineService(discipline_repository, discipline_validator)
        discipline_service.add_discipline(1, "idk")

        validator = GradeValidator()
        grade = Grade(0, 0, 0)
        try:
            validator.validate(grade,student_service,discipline_service)
            self.assertFalse('should raise exception')
        except ValidatorException as ex:
            self.assertEqual (len(ex.get_errors()) , 5)

        grade = Grade(-4, -2, 1)
        try:
            validator.validate(grade,student_service,discipline_service)
            self.assertFalse('should raise exception')
        except ValidatorException as ex:
            self.assertEqual (len(ex.get_errors()) , 4)

        grade = Grade(-4, 1, 1)
        try:
            validator.validate(grade,student_service,discipline_service)
            self.assertFalse('should raise exception')
        except ValidatorException as ex:
            self.assertEqual (len(ex.get_errors()) ,2)

        grade = Grade(1, 1, 1)
        try:
            validator.validate(grade,student_service,discipline_service)
            self.assertTrue('correct')
        except ValidatorException as ex:
            self.assertFalse('should not have raised exception')  # in case it finds an exception although it should not


    """"""""""""""""""""""""""""""""""""""""""""
    #TEST DISCIPLINE REPOSITORY
    """"""""""""""""""""""""""""""""""""""""""""

    def test_repository_store_discipline(self):
        repository = DisciplineRepository()
        self.assertEqual (repository.get_size_repository_disciplines() , 0)

        discipline1 = Discipline(1, "Algebra")
        repository.store_discipline(discipline1)
        self.assertEqual (repository.get_size_repository_disciplines() , 1)

        discipline2 = Discipline(1, "Chemistry")
        try:
            repository.store_discipline(discipline2)
            self.assertFalse('should raise exception')
        except RepositoryException as ex:
            self.assertEqual(repository.get_size_repository_disciplines(), 1)
            self.assertEqual (str(ex.get_errors()) , "Discipline ID already exists!")

        discipline3 = Discipline(2, "IDK")
        try:
            repository.store_discipline(discipline3)
            self.assertTrue('correct')
        except RepositoryException as ex:
            self.assertFalse('should not have raised exception')

        self.assertEqual (repository.get_size_repository_disciplines() , 2)

    def test_repository_delete_discipline(self):
        repository = DisciplineRepository()
        discipline = Discipline(1, "Algebra")
        repository.store_discipline(discipline)
        self.assertEqual (repository.get_size_repository_disciplines() , 1)

        try:
            repository.delete_discipline(1)
            self.assertTrue('correct')
        except RepositoryException:
            self.assertEqual (repository.get_size_repository_disciplines() , 0)
            self.assertFalse('exception should not have been raised')

        try:
            repository.delete_discipline(1)
            self.assertFalse('should raise exception')
        except RepositoryException as ex:
            self.assertEqual (repository.get_size_repository_disciplines() , 0)
            self.assertEqual (str(ex.get_errors()) , "No discipline with that ID!")

    def test_repository_update_discipline(self):
        repository = DisciplineRepository()
        discipline = Discipline(1, "Fizica")
        repository.store_discipline(discipline)
        discipline = Discipline(2, "Fizica")
        try:
            repository.update_discipline(discipline)
            self.assertFalse('SHOULD RAISE EXCEPTION')
        except RepositoryException as ex:
            self.assertEqual (str(ex.get_errors()) , "No discipline with that ID!")

        discipline = Discipline(1, "Fizica")
        try:
            repository.update_discipline(discipline)
            self.assertTrue ('correct')
        except RepositoryException:
            self.assertFalse ('should not have raised exception')

    def test_repository_find_discipline_by_id(self):
        repository = DisciplineRepository()
        discipline = Discipline(1, "Algebra")
        repository.store_discipline(discipline)
        self.assertEqual (repository.get_size_repository_disciplines() , 1)

        try:
            repository.find_discipline_by_id(1)
            self.assertTrue('correct')
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        try:
            repository.find_discipline_by_id(2)
            self.assertFalse('should raise exception')
        except RepositoryException as ex:
            self.assertEqual (str(ex.get_errors()) , "No discipline with that ID!")

    def test_find_discipline_by_name(self):
        repository = DisciplineRepository()
        discipline = Discipline(1, "Math")
        repository.store_discipline(discipline)
        self.assertEqual (repository.get_size_repository_disciplines() , 1)
        try:
            repository.find_discipline_by_name("math")
            self.assertTrue('correct')
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        try:
            repository.find_discipline_by_name("m")
            self.assertTrue('correct')
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        discipline2=Discipline(2,"meth")
        repository.store_discipline(discipline2)
        self.assertEqual (repository.get_size_repository_disciplines() , 2)
        try:
            list_of_disciplines=repository.find_discipline_by_name("M")
            self.assertEqual (len(list_of_disciplines),2)
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        try:
            repository.find_discipline_by_name("MaTH")
            self.assertTrue('correct')
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        try:
            repository.find_discipline_by_name("Pamfil")
            self.assertFalse('should raise exception')
        except RepositoryException:
            self.assertTrue('correct')


    """"""""""""""""""""""""""""""""""""""""""""""""
    #TEST STUDENT REPOSITORY
    """"""""""""""""""""""""""""""""""""""""""""""""
    def test_repository_store_student(self):
        repository = StudentRepository()
        self.assertEqual (repository.get_size_repository_students() , 0)

        student1 = Student(1, "Mihai")
        repository.store_student(student1)
        self.assertEqual (repository.get_size_repository_students() , 1)

        student2 = Student(1, "Pamfil")
        try:
            repository.store_student(student2)
            self.assertFalse('should raise exception')
        except RepositoryException as ex:
            self.assertEqual (repository.get_size_repository_students() , 1)
            self.assertEqual (str(ex.get_errors()) , "Student ID already exists!")

        student3 = Student(2, "IDK")
        try:
            repository.store_student(student3)
            self.assertTrue('correct')
        except RepositoryException as ex:
            self.assertFalse('should not have raised exception')

        self.assertEqual (repository.get_size_repository_students() , 2)

    def test_repository_delete_student(self):
        repository = StudentRepository()
        student = Student(1, "Mihai")
        repository.store_student(student)
        self.assertEqual (repository.get_size_repository_students() , 1)

        try:
            repository.delete_student(1)
            self.assertTrue('correct')
        except RepositoryException:
            self.assertEqual (repository.get_size_repository_students() , 0)
            self.assertFalse('should not have raised exception')

        try:
            repository.delete_student(1)
            self.assertFalse('should raise exception')
        except RepositoryException as ex:
            self.assertEqual (repository.get_size_repository_students() , 0)
            self.assertEqual (str(ex.get_errors()) , "No student with that ID!")

    def test_repository_update_student(self):
        repository = StudentRepository()
        student = Student(1, "Fizica")
        repository.store_student(student)
        student = Student(2, "Fizica")
        try:
            repository.update_student(student)
            self.assertFalse('should raise exception')
        except RepositoryException as ex:
            self.assertEqual (str(ex.get_errors()) , "No student with that ID!")
        self.assertEqual (len(repository.get_student()) , 1)
        student = Student(1, "Matematica")
        try:
            repository.update_student(student)
            self.assertTrue('correct')
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        self.assertEqual (len(repository.get_student()),1)
        self.assertEqual (repository.get_student()[0].get_student_name(),"Matematica")

    def test_repository_find_student_by_id(self):
        repository = StudentRepository()
        student = Student(1, "Mihai")
        repository.store_student(student)
        self.assertEqual (repository.get_size_repository_students() , 1)

        try:
            repository.find_student_by_id(1)
            self.assertTrue('correct')
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        try:
            repository.find_student_by_id(2)
            self.assertFalse('should raise exception')
        except RepositoryException as ex:
            self.assertEqual (str(ex.get_errors()) , "No student with that ID!")

    def test_find_student_by_name(self):
        repository = StudentRepository()
        student = Student(1, "Mihai")
        repository.store_student(student)
        self.assertEqual (repository.get_size_repository_students() , 1)
        try:
            repository.find_student_by_name("Mihai")
            self.assertTrue('correct')
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        try:
            repository.find_student_by_name("m")
            self.assertTrue('correct')
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        student2=Student(2,"amalia")
        repository.store_student(student2)
        self.assertEqual (repository.get_size_repository_students() , 2)
        try:
            list_of_students=repository.find_student_by_name("M")
            assert len(list_of_students)==2
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        try:
            repository.find_student_by_name("MiHAi")
            self.assertTrue('correct')
        except RepositoryException:
            self.assertFalse('should not have raised exception')

        try:
            repository.find_student_by_name("ANA")
            self.assertFalse('should raise exception')
        except RepositoryException:
            self.assertTrue('correct')



    """"""""""""""""""""""""""""""""
    #TEST GRADE REPOSITORY
    """"""""""""""""""""""""""""""""
    def test_grade(self):
        student_id=4
        discipline_id=1
        grade_value=10
        grade=Grade(discipline_id,student_id,grade_value)
        grade_repository=GradeRepository()
        self.assertEqual (grade_repository.get_number_of_grades(),0)
        grade_repository.store_grade(grade)
        self.assertEqual (grade_repository.get_number_of_grades(),1)
        grade_repository.store_grade(grade)
        self.assertEqual (grade_repository.get_number_of_grades(),2)
        grade_list=grade_repository.find_grades_by_student_id(student_id)
        self.assertEqual(len(grade_list),2)
        grade_list=grade_repository.find_grade_by_discipline_andstudent_id(discipline_id,student_id)
        self.assertEqual(len(grade_list),2)
        try:
            grade_list=grade_repository.find_grade_by_discipline_andstudent_id(6,6)
            self.assertFalse('should raise exception')
        except RepositoryException:
            self.assertTrue('correct')

    def test_grade_delete(self):
        grade1=Grade(1,1,10)
        grade2=Grade(2,1,10)
        grade3=Grade(1,3,8)
        grade4=Grade(2,4,5)
        grade5=Grade(4,1,10)
        grade6=Grade(2,6,4)
        repository=GradeRepository()
        repository.store_grade(grade1)
        repository.store_grade(grade2)
        repository.store_grade(grade3)
        repository.store_grade(grade4)
        repository.store_grade(grade5)
        repository.store_grade(grade6)
        self.assertEqual (repository.get_number_of_grades(),6)
        repository.delete_all_grades_by_discipline_id(1)
        self.assertEqual (repository.get_number_of_grades(),4)
        repository.delete_all_grades_by_student_id(6)
        self.assertEqual (repository.get_number_of_grades(),3)
        repository.delete_all_grades_by_student_id(6)
        self.assertEqual (repository.get_number_of_grades() , 3)


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #TEST DISCIPLINE SERVICE
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def test_discipline_add_service(self):
        valid=DisciplineValidator()
        repo = DisciplineRepository()
        service = DisciplineService(repo, valid)

        service.add_discipline(1, "Socio-umane")
        list_disciplines = service.get_all_disciplines()
        self.assertEqual (len(list_disciplines) , 1)

        try:
            service.add_discipline(0, "Socio-umane")
            self.assertFalse('exception should have been raised')
        except ValidatorException:
            self.assertTrue('correct')

        try:
            service.add_discipline(2, "")
            self.assertFalse('exception should have been raised')
        except ValidatorException:
            self.assertTrue('correct')

        try:
            service.add_discipline(1, "Socio-umane")
            self.assertFalse('should raise exception')
        except RepositoryException:
            self.assertTrue('correct')
        service.add_discipline(2,"idk")
        list_disciplines = service.get_all_disciplines()
        self.assertEqual (len(list_disciplines) , 2)

    def test_discipline_delete_service(self):
        valid = DisciplineValidator()
        repo = DisciplineRepository()
        service = DisciplineService(repo, valid)
        service.add_discipline(1, "Socio-umane")
        service.add_discipline(2, "idk")
        service.add_discipline(3, "Fizica cu Pamfil")
        service.delete_discipline(2)
        list_disciplines = service.get_all_disciplines()
        self.assertEqual (len(list_disciplines),2)
        try:
            service.delete_discipline(4)
            self.assertFalse('should raise exception')
        except RepositoryException:
            self.assertTrue('correct')

        try:
            service.delete_discipline(0)
            self.assertFalse('should raise exception')
        except RepositoryException:
            self.assertTrue('correct')

    def test_average_grade_student_at_subject(self):
        student_validator = StudentValidator()
        discipline_validator = DisciplineValidator()
        grade_validator = GradeValidator()

        student_repository = StudentRepository()
        student_service = StudentService(student_repository, student_validator)
        student_service.add_student(1, "Cosmin Semenciuc")
        student_service.add_student(2, "Popa Andrei")
        student_service.add_student(3, "Serban George")
        student_service.add_student(4, "Silaschi Iasmina")
        student_service.add_student(5, "Silasi Marius")
        student_service.add_student(6, "Socaciu Serafim")
        student_service.add_student(7, "Spinu Valentin")
        student_service.add_student(8, "Stan Ioana")
        student_service.add_student(9, "Stanciu Catalin")
        student_service.add_student(10, "Stef Eduard")

        discipline_repository = DisciplineRepository()
        discipline_service = DisciplineService(discipline_repository, discipline_validator)
        discipline_service.add_discipline(1, "CSA")
        discipline_service.add_discipline(2, "CL")
        discipline_service.add_discipline(3, "FP")
        discipline_service.add_discipline(4, "Analysis")
        discipline_service.add_discipline(5, "Algebra")
        discipline_service.add_discipline(6, "C Programming")

        grade_repository = GradeRepository()
        grade_service = GradeService(grade_repository, grade_validator, student_service, discipline_service)
        grade_service.add_grade(1, 1, 10)
        grade_service.add_grade(1, 1, 8)
        grade_service.add_grade(1, 1, 10)
        grade_service.add_grade(2, 1, 10)
        grade_service.add_grade(2, 2, 10)
        grade_service.add_grade(3, 1, 10)
        grade_service.add_grade(4, 4, 10)
        grade_service.add_grade(5, 5, 6)
        grade_service.add_grade(2, 10, 10)
        grade_service.add_grade(6, 7, 10)
        average_grade=grade_service.get_average_of_student_at_discipline(1,1)
        self.assertGreater (average_grade,9)
        average_grade=grade_service.get_average_of_student_at_discipline(20,20)
        self.assertEqual (average_grade,-1)

    def run_all_tests(self):
        self.test_Discipline_class()
        self.test_Student_class()
        self.test_Grade_class()


        self.testStudentValidator()
        self.test_DisciplineValidator()
        self.testGradeValidator()


        self.test_repository_store_discipline()
        self.test_repository_delete_discipline()
        self.test_repository_update_discipline()
        self.test_repository_find_discipline_by_id()
        self.test_find_discipline_by_name()


        self.test_repository_store_student()
        self.test_repository_delete_student()
        self.test_repository_update_student()
        self.test_repository_find_student_by_id()
        self.test_find_student_by_name()


        self.test_grade()
        self.test_grade_delete()

        self.test_discipline_add_service()
        self.test_discipline_delete_service()

        self.test_average_grade_student_at_subject()

