

# from service.handlers import UndoHandler
# from service.undo import UndoManager
# from enum import Enum
#
# def add_student_handler(student_service, student_id, student_name):
#     student_service.add_student(student_id, student_name)
#     UndoManager.register_operation(student_service,UndoHandler.ADD_STUDENT,student_id)
#
#
# def delete_student_handler(student_service, student_id):
#     student_name=student_service.find_students_by_id(student_id).get_student_name()
#     student_service.delete_student(student_id)
#     UndoManager.register_operation(student_service,UndoHandler.DELETE_STUDENT,student_id,student_name)
#
#
# def update_student_handler(student_service, student_id, student_name):
#     old_name=student_service.find_students_by_id().get_student_name()
#     student_service.update_student(student_id, student_name)
#     UndoManager.register_operation(student_service,UndoHandler.UPDATE_STUDENT,student_id,old_name)
#
#
# def add_discipline_handler(discipline_service, discipline_id, discipline_name):
#     discipline_service.add_discipline(discipline_id, discipline_name)
#     UndoManager.register_operation(discipline_service,UndoHandler.ADD_DISCIPLINE,discipline_id)
#
#
# def delete_discipline_handler(discipline_service, discipline_id):
#     discipline_name=discipline_service.find_disciplines_by_id(discipline_id)
#     discipline_service.delete_discipline(discipline_id)
#     UndoManager.register_operation(discipline_service,UndoHandler.DELETE_DISCIPLINE,discipline_id,discipline_name)
#
#
# def update_discipline_handler(discipline_service, discipline_id, discipline_name):
#     old_discipline_name=discipline_service.find_disciplines_by_id(discipline_id)
#     discipline_service.update_discipline(discipline_id, discipline_name)
#     UndoManager.register_operation(discipline_service,UndoHandler.UPDATE_DISCIPLINE,discipline_id,old_discipline_name)
#
#
# def add_grade_handler(grade_service, discipline_id, student_id, grade_value):
#     grade_service.add_grade(discipline_id, student_id, grade_value)
#     UndoManager.register_operation(grade_service,UndoHandler.ADD_GRADE,discipline_id,student_id,grade_value)
#
#
# def delete_all_grades_of_student_handler(grade_service, student_id):
#     objects_grades_list=grade_service.find_object_grade_list_by_student_id(student_id)
#     grade_service.delete_all_grades_of_student(student_id)
#     UndoManager.register_operation(grade_service,UndoHandler.DELETE_STUDENT_GRADES,objects_grades_list)
#
#
# def delete_all_grades_at_discipline_handler(grade_service, discipline_id):
#     objects_grades_list=grade_service.find_object_grade_list_at_discipline(discipline_id)
#     grade_service.delete_all_grades_at_discipline(discipline_id)
#     UndoManager.register_operation(grade_service,UndoHandler.DELETE_DISCIPLINE_GRADES,objects_grades_list)
#
#
# class RedoHandler(Enum):
#     ADD_STUDENT = add_student_handler
#     DELETE_STUDENT = delete_student_handler
#     UPDATE_STUDENT = update_student_handler
#     ADD_DISCIPLINE = add_discipline_handler
#     DELETE_DISCIPLINE = delete_discipline_handler
#     UPDATE_DISCIPLINE = update_discipline_handler
#     ADD_GRADE = add_grade_handler
#     DELETE_STUDENT_GRADES = delete_all_grades_of_student_handler
#     DELETE_DISCIPLINE_GRADES = delete_all_grades_at_discipline_handler
