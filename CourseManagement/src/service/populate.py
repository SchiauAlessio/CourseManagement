
class Populate:
    def __init__(self,student_service,discipline_service,grade_service):
        self.__student_service=student_service
        self.__discipline_service=discipline_service
        self.__grade_service=grade_service

    def populate_with_students(self):
        self.__student_service.add_student(1, "Cosmin Semenciuc")
        self.__student_service.add_student(2, "Popa Andrei")
        self.__student_service.add_student(3, "Serban George")
        self.__student_service.add_student(4, "Silaschi Iasmina")
        self.__student_service.add_student(5, "Silasi Marius")
        self.__student_service.add_student(6, "Socaciu Serafim")
        self.__student_service.add_student(7, "Spinu Valentin")
        self.__student_service.add_student(8, "Stan Ioana")
        self.__student_service.add_student(9, "Stanciu Catalin")
        self.__student_service.add_student(10, "Stef Eduard")
        self.__student_service.add_student(11, "guy that is failing")

    def populate_with_disciplines(self):
        self.__discipline_service.add_discipline(1, "CSA")
        self.__discipline_service.add_discipline(2, "CL")
        self.__discipline_service.add_discipline(3, "FP")
        self.__discipline_service.add_discipline(4, "Analysis")
        self.__discipline_service.add_discipline(5, "Algebra")
        self.__discipline_service.add_discipline(6, "C Programming")

    def populate_with_grades(self):
        self.__grade_service.add_grade(1, 1, 10)
        self.__grade_service.add_grade(1, 1, 8)
        self.__grade_service.add_grade(1, 1, 10)
        self.__grade_service.add_grade(2, 1, 10)
        self.__grade_service.add_grade(2, 2, 10)
        self.__grade_service.add_grade(3, 1, 10)
        self.__grade_service.add_grade(4, 4, 10)
        self.__grade_service.add_grade(5, 5, 6)
        self.__grade_service.add_grade(2, 10, 10)
        self.__grade_service.add_grade(6, 7, 10)
        self.__grade_service.add_grade(1, 11, 4)
