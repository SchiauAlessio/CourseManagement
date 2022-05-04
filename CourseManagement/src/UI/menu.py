from DataStructure_sort_filter.sorting import Sorting
from domain.discipline import Discipline
from domain.student import Student
from domain.validators import ValidatorException
from repository.repository_exception import RepositoryException
from service.handlers import UndoHandler
#from service.redo_handlers import RedoHandler
from service.undo import UndoManager, UndoException, RedoException


class Menu:
    def __init__(self, student_service, discipline_service, grade_service):
        self.__student_service = student_service
        self.__discipline_service = discipline_service
        self.__grade_service = grade_service
        self.__main_options = {
            1: self.manage_students,
            2: self.manage_disciplines,
            3: self.ui_manage_grades,
            4: self.ui_statistics,
            5: self.undo,
            6: self.redo

        }

    def student_register_options(self):
        print("1. Manage students")
        print("2. Manage disciplines")
        print("3. Manage grades")
        print("4. Statistics")
        print("5. Undo")
        print("6. Redo")
        print("x. Exit the application")

    def ui_list_all_grades(self):
        grades = self.__grade_service.get_all_grades()
        for grade in grades:
            print(str(grade))

    def ui_add_grade(self):
        discipline_id = int(input("Choose the discipline ID: "))
        student_id = int(input("Choose the student's ID: "))
        grade_value = int(input("Choose the grade: "))
        self.__grade_service.add_grade(discipline_id, student_id, grade_value)
        UndoManager.register_operation(self.__grade_service, UndoHandler.ADD_GRADE, discipline_id, student_id,
                                       grade_value)
        UndoManager.initialise_redo_list_empty()
        #UndoManager.register_operation_redo(self.__grade_service, RedoHandler.ADD_GRADE, discipline_id, student_id,grade_value)

    """""""""""""""""""""""""""""
    #STUDENTS
    """""""""""""""""""""""""""""

    def ui_list_students(self):
        students = self.__student_service.get_all_students()
        for student in students:
            print(str(student))

    def ui_add_students(self):
        """
        adds a students in the student repository
        :return:
        """
        student_id = int(input("Enter the student's ID: "))
        student_name = input("Enter the student's name: ")
        self.__student_service.add_student(student_id, student_name)
        UndoManager.register_operation(self.__student_service, UndoHandler.ADD_STUDENT, student_id)
        #UndoManager.register_operation_redo(self.__student_service, RedoHandler.ADD_STUDENT, student_id, student_name)
        UndoManager.initialise_redo_list_empty()

    def ui_delete_student(self):
        """
        removes a student from the student repository
        :return:
        """
        student_id = int(input("Enter the ID of the student you wish to delete: "))
        student = self.__student_service.find_students_by_id(student_id)
        student_name = student.get_student_name()
        object_grades_list = self.__grade_service.find_object_grade_list_by_student_id(student_id)
        self.__grade_service.delete_all_grades_of_student(student_id)
        UndoManager.register_operation(self.__grade_service, UndoHandler.DELETE_STUDENT_GRADES, student_id,object_grades_list)
        #UndoManager.register_operation_redo(self.__grade_service, RedoHandler.DELETE_STUDENT_GRADES, student_id)
        self.__student_service.delete_student(student_id)
        UndoManager.register_operation(self.__student_service, UndoHandler.DELETE_STUDENT, student_id, student_name)
        #UndoManager.register_operation_redo(self.__student_service, RedoHandler.DELETE_STUDENT, student_id)
        UndoManager.initialise_redo_list_empty()

    def ui_update_student(self):
        """
        updates the name of a student in the repository
        :return:
        """
        student_id = int(input("Enter the student's ID: "))
        student_name = input("Enter the new name: ")
        student = self.__student_service.find_students_by_id(student_id)
        student_old_name = student.get_student_name()
        self.__student_service.update_student(student_id, student_name)
        UndoManager.register_operation(self.__student_service, UndoHandler.UPDATE_STUDENT, student_id, student_old_name)
        #UndoManager.register_operation_redo(self.__student_service, RedoHandler.UPDATE_STUDENT, student_id,student_name)
        UndoManager.initialise_redo_list_empty()

    def ui_find_student_by_id(self):
        """
        prints the student having the user given id
        :return:
        """
        student_id = int(input("Enter the student's ID: "))
        student_with_specified_id = self.__student_service.find_students_by_id(student_id)
        print(str(student_with_specified_id))

    def ui_find_students_by_name(self):
        """
        prints all students having the name/partial name given by the user
        :return:
        """
        student_name = input("Enter the student's name/partial name: ")
        students_with_specified_name = self.__student_service.find_students_by_name(student_name)
        for student in students_with_specified_name:
            print(str(student))

    def ui_list_failing_students(self):
        """
        prints all students that are failing at at least one subject (grade<5)
        -1 is returned is returned by the get_average function in case a student is not graded so that is also checked (since -1<5)
        a special message is displayed in case no students are failing
        :return:
        """
        student_index = 0
        ok = 0
        students_list = self.__student_service.get_all_students()
        while student_index < len(students_list):
            discipline_index = 0
            discipline_list = self.__discipline_service.get_all_disciplines()
            while discipline_index < len(discipline_list):
                student_id = students_list[student_index].get_student_id()
                discipline_id = discipline_list[discipline_index].get_discipline_id()
                current_student_average = self.__grade_service.get_average_of_student_at_discipline(student_id,
                                                                                                    discipline_id)
                if current_student_average < 5 and current_student_average != -1:
                    print(str(students_list[student_index]))
                    ok = 1
                    break  # it is enough if we find one failing subject
                else:
                    discipline_index = discipline_index + 1
            student_index = student_index + 1
        if ok == 0:
            print("No students are failing!")

    def ui_list_best_performing_students(self):
        """
        all students are displayed alongside their aggregated average in descending order
        :return:
        """
        averages_list = self.__grade_service.get_aggregated_average_of_students()
        Sorting.sort(averages_list,key=lambda student_information: student_information[2],
                           reverse=True)  # student information[2] is the value of the average of the student from each sublist containing student information
        for sub_list_with_student_information in averages_list:
            student_id = sub_list_with_student_information[0]
            student_name = sub_list_with_student_information[1]
            aggregated_average = sub_list_with_student_information[2]
            student = Student(student_id, student_name)
            print(str(student) + " | average grade: " + str(aggregated_average))

    """"""""""""""""""""""""""""
    #DISCIPLINES
    """""""""""""""""""""""""""""

    def ui_list_disciplines(self):
        disciplines = self.__discipline_service.get_all_disciplines()
        for discipline in disciplines:
            print(str(discipline))

    def ui_add_disciplines(self):
        discipline_id = int(input("Enter the discipline's ID: "))
        discipline_name = input("Enter the discipline's name: ")
        self.__discipline_service.add_discipline(discipline_id, discipline_name)
        UndoManager.register_operation(self.__discipline_service, UndoHandler.ADD_DISCIPLINE, discipline_id)
        #UndoManager.register_operation_redo(self.__discipline_service, RedoHandler.ADD_DISCIPLINE, discipline_id,discipline_name)
        UndoManager.initialise_redo_list_empty()

    def ui_delete_discipline(self):
        discipline_id = int(input("Enter the ID of the discipline you wish to delete: "))
        discipline = self.__discipline_service.find_disciplines_by_id(discipline_id)
        discipline_name = discipline.get_discipline_name()
        objects_grades_list = self.__grade_service.find_object_grade_list_at_discipline(discipline_id)
        self.__grade_service.delete_all_grades_at_discipline(discipline_id)
        UndoManager.register_operation(self.__grade_service, UndoHandler.DELETE_DISCIPLINE_GRADES, discipline_id,objects_grades_list)
        #UndoManager.register_operation_redo(self.__grade_service, RedoHandler.DELETE_DISCIPLINE_GRADES, discipline_id)
        self.__discipline_service.delete_discipline(discipline_id)
        UndoManager.register_operation(self.__discipline_service, UndoHandler.DELETE_DISCIPLINE, discipline_id,
                                       discipline_name)
        #UndoManager.register_operation_redo(self.__discipline_service, RedoHandler.DELETE_DISCIPLINE, discipline_id)
        UndoManager.initialise_redo_list_empty()

    def ui_update_discipline(self):
        discipline_id = int(input("Enter the ID of the discipline you wish to modify: "))
        discipline_name = input("Enter the new name: ")
        discipline = self.__discipline_service.find_disciplines_by_id(discipline_id)
        old_discipline_name = discipline.get_discipline_name()
        self.__discipline_service.update_discipline(discipline_id, discipline_name)
        UndoManager.register_operation(self.__discipline_service, UndoHandler.UPDATE_DISCIPLINE, discipline_id,
                                       old_discipline_name)
        #UndoManager.register_operation_redo(self.__discipline_service, RedoHandler.UPDATE_DISCIPLINE, discipline_id, discipline_name)
        UndoManager.initialise_redo_list_empty()

    def ui_find_discipline_by_id(self):
        discipline_id = int(input("Enter the discipline's ID: "))
        discipline_with_specified_id = self.__discipline_service.find_disciplines_by_id(discipline_id)
        print(str(discipline_with_specified_id))

    def ui_find_disciplines_by_name(self):
        discipline_name = input("Enter the discipline's name/partial name: ")
        disciplines_with_specified_name = self.__discipline_service.find_disciplines_by_name(discipline_name)
        for discipline in disciplines_with_specified_name:
            print(str(discipline))

    def ui_list_best_graded_disciplines(self):
        """
        all disciplines are displayed alongside the average of all students at that discipline
        in descending order
        :return:
        """
        averages_list = self.__grade_service.get_aggregated_average_at_disciplines()
        Sorting.sort(averages_list,key=lambda grade_information: grade_information[2],
                           reverse=True)  # grade_information[2] is the value of the grade from each sub list containing information about grades so the sorting is done based on that value
        for grade_information_sub_list in averages_list:
            discipline_id = grade_information_sub_list[0]
            discipline_name = grade_information_sub_list[1]
            average_of_all_students = grade_information_sub_list[2]
            discipline = Discipline(discipline_id, discipline_name)
            print(str(discipline) + " | average grade: " + str(average_of_all_students))

    def manage_students(self):
        self.choices = {
            1: self.ui_add_students,
            2: self.ui_delete_student,
            3: self.ui_update_student,
            4: self.ui_list_students,
            5: self.ui_find_student_by_id,
            6: self.ui_find_students_by_name
        }
        while True:
            print("1. Add a new student")
            print("2. Remove a student")
            print("3. Update a student's information")
            print("4. List all students")
            print("5. Find a student by their ID")
            print("6. Find students by their name")
            print("x. Exit the sub-menu")
            user_choice = input("Your choice: ")
            if user_choice == "x":
                return
            try:
                print()
                self.choices[int(user_choice)]()
                print()
            except IndexError as ie:
                print("That command is not available!\n")
            except ValueError as ve:
                print("That command is not available!\n")
            except KeyError as ke:
                print("That command is not available!\n")

    def manage_disciplines(self):
        self.choices = {
            1: self.ui_add_disciplines,
            2: self.ui_delete_discipline,
            3: self.ui_update_discipline,
            4: self.ui_list_disciplines,
            5: self.ui_find_discipline_by_id,
            6: self.ui_find_disciplines_by_name
        }
        while True:
            print("1. Add a new discipline")
            print("2. Remove a discipline")
            print("3. Update a discipline's information")
            print("4. List all disciplines")
            print("5. Find a discipline by their ID")
            print("6. Find disciplines by their name/partial name")
            print("x. Exit the sub-menu")
            user_choice = input("Your choice: ")
            if user_choice == "x":
                return
            try:
                print()
                self.choices[int(user_choice)]()
                print()
            except IndexError as ie:
                print("That command is not available!\n")
            except ValueError as ve:
                print("That command is not available!\n")
            except KeyError as ke:
                print("That command is not available!\n")

    def ui_manage_grades(self):
        self.choices = {
            1: self.ui_add_grade,
            2: self.ui_list_all_grades
        }
        while True:
            print("1. Grade a student")
            print("2. List all grades")
            print("x. Exit the sub-menu")
            user_choice = input("Your choice: ")
            if user_choice == 'x':
                return
            print()
            self.choices[int(user_choice)]()
            print()

    def ui_statistics(self):
        self.choices = {
            1: self.ui_list_failing_students,
            2: self.ui_list_best_performing_students,
            3: self.ui_list_best_graded_disciplines

        }
        while True:
            print("1. Display all students failing at one or more subjects")
            print("2. Display the students with the best school situation sorted in descending order of their average")
            print("3. Display all disciplines with at least one grade, sorted in descending order of average")
            print("x. Exit sub-menu")
            choice = input("Your choice: ")
            if choice == "x":
                return
            print()
            self.choices[int(choice)]()
            print()

    def undo(self):
        try:
            UndoManager.undo()
        except UndoException as ue:
            print(str(ue))

    def redo(self):
        try:
            UndoManager.redo()
        except RedoException as re:
            print(str(re))

    def run_menu(self):
        while True:
            self.student_register_options()
            user_choice = input("Your choice: ")
            if user_choice == "x":
                return
            try:
                print()
                self.__main_options[int(user_choice)]()
                print()
            except IndexError as ie:
                print("That command is not available!\n")
            except ValueError as ve:
                print("That command is not available!\n")
            except KeyError as ke:
                print("That command is not available!\n")
            except RepositoryException as re:
                error = re.get_errors()
                print(error)
                print()
            except ValidatorException as ve:
                errors = ve.get_errors()
                for error in errors:
                    print(error)
                print()
