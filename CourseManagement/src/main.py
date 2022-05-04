from UI.menu import Menu
from domain.validators import StudentValidator, DisciplineValidator, GradeValidator
from repository.discipline_repository import DisciplineRepository
from repository.file_discipline_repository import FileDisciplineRepository
from repository.file_grade_repository import FileGradeRepository
from repository.file_student_repository import FileStudentRepository
from repository.grade_repository import GradeRepository
from repository.pickle_file_discipline_repo import BinaryFileDisciplineRepository
from repository.pickle_file_grade_repository import BinaryFileGradeRepository
from repository.pickle_file_student_repository import BinaryFileStudentRepository
#from repository.repository_exception import RepositoryException
from repository.student_repository import StudentRepository
#from service.handlers import UndoHandler
from service.populate import Populate
from service.service_discipline import DisciplineService
from service.service_grade import GradeService
from service.service_student import StudentService
# from service.undo import UndoManager
from settings.settings import Settings
#from testing.tests import Tests

if __name__ == "__main__":

    # tests = Tests()
    # tests.run_all_tests()

    student_validator = StudentValidator()
    discipline_validator = DisciplineValidator()
    grade_validator = GradeValidator()
    settings = Settings("settings.properties")
    if settings.get_repository_type() == "inmemory":
        student_repository = StudentRepository()
        discipline_repository = DisciplineRepository()
        grade_repository = GradeRepository()
    elif "text" in settings.get_repository_type():
        file_student_name = settings.get_student_file_name()
        student_repository = FileStudentRepository(file_student_name)
        file_discipline_name = settings.get_discipline_file_name()
        discipline_repository = FileDisciplineRepository(file_discipline_name)
        grade_file_name = settings.get_grade_file_name()
        grade_repository = FileGradeRepository(grade_file_name)
    else:
        file_student_name = settings.get_student_file_name()
        student_repository = BinaryFileStudentRepository(file_student_name)
        file_discipline_name = settings.get_discipline_file_name()
        discipline_repository = BinaryFileDisciplineRepository(file_discipline_name)
        grade_file_name = settings.get_grade_file_name()
        grade_repository = BinaryFileGradeRepository(grade_file_name)

    student_service = StudentService(student_repository, student_validator)
    discipline_service = DisciplineService(discipline_repository, discipline_validator)
    grade_service = GradeService(grade_repository, grade_validator, student_service, discipline_service)
    population = Populate(student_service, discipline_service, grade_service)
    if student_repository.get_size_repository_students() == 0:
        population.populate_with_students()
    if discipline_repository.get_size_repository_disciplines() == 0:
        population.populate_with_disciplines()
    if grade_repository.get_number_of_grades() == 0:
        population.populate_with_grades()

    console = Menu(student_service, discipline_service, grade_service)
    console.run_menu()


#copy in text files
#"C:\Users\Alessio\Documents\Github\a9-916-Schiau-Alessio\src\student.txt"
#"C:\Users\Alessio\Documents\Github\a9-916-Schiau-Alessio\src\discipline.txt"
#"C:\Users\Alessio\Documents\Github\a9-916-Schiau-Alessio\src\grade.txt"
