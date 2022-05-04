class Grade:
    def __init__(self, discipline_id, student_id, grade_value):
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    def get_discipline_id(self):
        return self.__discipline_id

    def get_student_id(self):
        return self.__student_id

    def get_grade_value(self):
        return self.__grade_value

    def set_grade_value(self,grade_value):
        self.__grade_value=grade_value

    def __str__(self):
        return "Discipline ID: "+str(self.get_discipline_id())+" | "+"Student ID: "+str(self.get_student_id())+" | Grade value: "+str(self.get_grade_value())
