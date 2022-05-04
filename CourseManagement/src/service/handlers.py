from enum import Enum

from service.undo import UndoManager


def add_student_handler(student_service, student_id):
    student_name = student_service.find_students_by_id(student_id).get_student_name()
    student_service.delete_student(student_id)
    UndoManager.register_operation_redo(student_service,RedoHandler.ADD_STUDENT,student_id,student_name)


def delete_student_handler(student_service, student_id, student_name):
    student_service.add_student(student_id, student_name)
    UndoManager.register_operation_redo(student_service,RedoHandler.DELETE_STUDENT,student_id)


def update_student_handler(student_service, student_id, old_student_name):
    student_name = student_service.find_students_by_id(student_id).get_student_name()
    student_service.update_student(student_id, old_student_name)
    UndoManager.register_operation_redo(student_service,RedoHandler.UPDATE_STUDENT,student_id,student_name)


def add_discipline_handler(discipline_service, discipline_id):
    discipline_name=discipline_service.find_disciplines_by_id(discipline_id).get_discipline_name()
    discipline_service.delete_discipline(discipline_id)
    UndoManager.register_operation_redo(discipline_service,RedoHandler.ADD_DISCIPLINE,discipline_id,discipline_name)


def delete_discipline_handler(discipline_service, discipline_id, discipline_name):
    discipline_service.add_discipline(discipline_id, discipline_name)
    UndoManager.register_operation_redo(discipline_service,RedoHandler.DELETE_DISCIPLINE,discipline_id)


def update_discipline_handler(discipline_service, discipline_id, old_discipline_name):
    discipline_name=discipline_service.find_disciplines_by_id(discipline_id).get_discipline_name()
    discipline_service.update_discipline(discipline_id, old_discipline_name)
    UndoManager.register_operation_redo(discipline_service,RedoHandler.UPDATE_DISCIPLINE,discipline_id,discipline_name)


def add_grade_handler(grade_service, discipline_id, student_id, grade_value):
    grade_service.delete_grade_ofstudent_atdiscipline_byvalue(discipline_id, student_id, grade_value)
    UndoManager.register_operation_redo(grade_service,RedoHandler.ADD_GRADE,discipline_id,student_id,grade_value)

def delete_all_grades_of_student_handler(grade_service, student_id,object_grades_list):
    for grade in object_grades_list:
        student_id = grade.get_student_id()
        discipline_id = grade.get_discipline_id()
        grade_value = grade.get_grade_value()
        grade_service.add_grade(discipline_id, student_id, grade_value)
    UndoManager.register_operation_redo(grade_service,RedoHandler.DELETE_STUDENT_GRADES,student_id)


def delete_all_grades_at_discipline_handler(grade_service, discipline_id,object_grades_list):
    for grade in object_grades_list:
        student_id = grade.get_student_id()
        discipline_id = grade.get_discipline_id()
        grade_value = grade.get_grade_value()
        grade_service.add_grade(discipline_id, student_id, grade_value)
    UndoManager.register_operation_redo(grade_service,RedoHandler.DELETE_DISCIPLINE_GRADES,discipline_id)


class UndoHandler(Enum):
    ADD_STUDENT = add_student_handler
    DELETE_STUDENT = delete_student_handler
    UPDATE_STUDENT = update_student_handler
    ADD_DISCIPLINE = add_discipline_handler
    DELETE_DISCIPLINE = delete_discipline_handler
    UPDATE_DISCIPLINE = update_discipline_handler
    ADD_GRADE = add_grade_handler
    DELETE_STUDENT_GRADES = delete_all_grades_of_student_handler
    DELETE_DISCIPLINE_GRADES = delete_all_grades_at_discipline_handler

#==========================================================================================
#REDO HANDLERS
#==========================================================================================
def redo_add_student_handler(student_service, student_id, student_name):
    student_service.add_student(student_id, student_name)
    UndoManager.register_operation(student_service,UndoHandler.ADD_STUDENT,student_id)


def redo_delete_student_handler(student_service, student_id):
    student_name=student_service.find_students_by_id(student_id).get_student_name()
    student_service.delete_student(student_id)
    UndoManager.register_operation(student_service,UndoHandler.DELETE_STUDENT,student_id,student_name)


def redo_update_student_handler(student_service, student_id, student_name):
    old_name=student_service.find_students_by_id(student_id).get_student_name()
    student_service.update_student(student_id, student_name)
    UndoManager.register_operation(student_service,UndoHandler.UPDATE_STUDENT,student_id,old_name)


def redo_add_discipline_handler(discipline_service, discipline_id, discipline_name):
    discipline_service.add_discipline(discipline_id, discipline_name)
    UndoManager.register_operation(discipline_service,UndoHandler.ADD_DISCIPLINE,discipline_id)


def redo_delete_discipline_handler(discipline_service, discipline_id):
    discipline_name=discipline_service.find_disciplines_by_id(discipline_id).get_discipline_name()
    discipline_service.delete_discipline(discipline_id)
    UndoManager.register_operation(discipline_service,UndoHandler.DELETE_DISCIPLINE,discipline_id,discipline_name)


def redo_update_discipline_handler(discipline_service, discipline_id, discipline_name):
    old_discipline_name=discipline_service.find_disciplines_by_id(discipline_id).get_discipline_name()
    discipline_service.update_discipline(discipline_id, discipline_name)
    UndoManager.register_operation(discipline_service,UndoHandler.UPDATE_DISCIPLINE,discipline_id,old_discipline_name)


def redo_add_grade_handler(grade_service, discipline_id, student_id, grade_value):
    grade_service.add_grade(discipline_id, student_id, grade_value)
    UndoManager.register_operation(grade_service,UndoHandler.ADD_GRADE,discipline_id,student_id,grade_value)


def redo_delete_all_grades_of_student_handler(grade_service, student_id):
    objects_grades_list=grade_service.find_object_grade_list_by_student_id(student_id)
    grade_service.delete_all_grades_of_student(student_id)
    UndoManager.register_operation(grade_service,UndoHandler.DELETE_STUDENT_GRADES,student_id,objects_grades_list)


def redo_delete_all_grades_at_discipline_handler(grade_service, discipline_id):
    objects_grades_list=grade_service.find_object_grade_list_at_discipline(discipline_id)
    grade_service.delete_all_grades_at_discipline(discipline_id)
    UndoManager.register_operation(grade_service,UndoHandler.DELETE_DISCIPLINE_GRADES,discipline_id,objects_grades_list)


class RedoHandler(Enum):
    ADD_STUDENT = redo_add_student_handler
    DELETE_STUDENT = redo_delete_student_handler
    UPDATE_STUDENT = redo_update_student_handler
    ADD_DISCIPLINE = redo_add_discipline_handler
    DELETE_DISCIPLINE = redo_delete_discipline_handler
    UPDATE_DISCIPLINE = redo_update_discipline_handler
    ADD_GRADE = redo_add_grade_handler
    DELETE_STUDENT_GRADES = redo_delete_all_grades_of_student_handler
    DELETE_DISCIPLINE_GRADES = redo_delete_all_grades_at_discipline_handler