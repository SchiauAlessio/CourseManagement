from dataclasses import dataclass


class UndoException(Exception):
    """
    Exception class for undo
    """
    pass


class RedoException(Exception):
    """
    Exception class for redo
    """
    pass


@dataclass
class UndoOperation:
    target_object: object
    handler: object
    arguments: tuple


class UndoManager:
    __undo_operations = []
    __redo_operations = []

    @staticmethod
    def initialise_redo_list_empty():
        UndoManager.__redo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *arguments):
        UndoManager.__undo_operations.append(UndoOperation(target_object, handler, arguments))

    @staticmethod
    def register_operation_redo(target_object, handler, *arguments):
        UndoManager.__redo_operations.append(UndoOperation(target_object, handler, arguments))

    @staticmethod
    def undo():
        """
        Undo the most recent user action
        If the most recent one is the deletion of a student/discipline then the next
        operation must be undone too, which is the deletion of the grades, which happened
        simultaneously with the deletion of the student/discipline
        """
        if len(UndoManager.__undo_operations) == 0:
            raise UndoException("No operations to undo!")
        undo_operation = UndoManager.__undo_operations.pop()
        if "delete" in str(undo_operation.handler):
            undo_operation2 = UndoManager.__undo_operations.pop()
            undo_operation.handler(undo_operation.target_object, *undo_operation.arguments)
            undo_operation2.handler(undo_operation2.target_object, *undo_operation2.arguments)
        else:
            undo_operation.handler(undo_operation.target_object, *undo_operation.arguments)

    @staticmethod
    def redo():
        """
        Redo the most recent undone user action
        If the most recent one is the deletion of a student/discipline then the next
        operation must be undone too, which is the deletion of the grades, which happened
        simultaneously with the deletion of the student/discipline
        """
        if len(UndoManager.__redo_operations) == 0:
            raise RedoException("No operations to redo!")
        redo_operation = UndoManager.__redo_operations.pop()
        if "delete" in str(redo_operation.handler):
            redo_operation2 = UndoManager.__redo_operations.pop()
            redo_operation.handler(redo_operation.target_object, *redo_operation.arguments)
            redo_operation2.handler(redo_operation2.target_object, *redo_operation2.arguments)
        else:
            redo_operation.handler(redo_operation.target_object, *redo_operation.arguments)

    # @staticmethod
    # def undo():
    #     undo_operation = UndoManager.__undo_operations.pop()
    #     UndoManager.__undone_operations.append(undo_operation)
    #     if len(UndoManager.__redone_operations)>0:
    #         undone_redone_operation=UndoManager.__redone_operations.pop()
    #         index_to_be_inserted_at = len(UndoManager.__redo_operations) - len(UndoManager.__undone_operations)+1
    #         UndoManager.__redo_operations.insert(index_to_be_inserted_at,undone_redone_operation)
    #     if "delete" in str(undo_operation.handler):
    #         undo_operation2 = UndoManager.__undo_operations.pop()
    #         UndoManager.__undone_operations.append(undo_operation2)
    #         if len(UndoManager.__redone_operations) > 0:
    #             undone_redone_operation = UndoManager.__redone_operations.pop()
    #             index_to_be_inserted_at = len(UndoManager.__redo_operations) - len(UndoManager.__undone_operations) + 1
    #             UndoManager.__redo_operations.insert(index_to_be_inserted_at, undone_redone_operation)
    #         undo_operation.handler(undo_operation.target_object, *undo_operation.arguments)
    #         undo_operation2.handler(undo_operation2.target_object, *undo_operation2.arguments)
    #     else:
    #         undo_operation.handler(undo_operation.target_object, *undo_operation.arguments)

    # @staticmethod
    # def redo():
    #     number_of_operation_tobe_redone=len(UndoManager.__redo_operations)-len(UndoManager.__undone_operations)
    #     redo_operation = UndoManager.__redo_operations[number_of_operation_tobe_redone]
    #     redone_undone_operation=UndoManager.__undone_operations.pop()
    #     UndoManager.__undo_operations.append(redone_undone_operation)
    #     UndoManager.__redone_operations.append(redo_operation)
    #     del UndoManager.__redo_operations[number_of_operation_tobe_redone]
    #     ##redo_operation = UndoManager.__redo_operations[0]
    #     ##del UndoManager.__redo_operations[0]
    #     if "delete" in str(redo_operation.handler):
    #         ##number_of_operation_tobe_redone = len(UndoManager.__redo_operations) - len(UndoManager.__undone_operations)
    #         redo_operation2 = UndoManager.__redo_operations[number_of_operation_tobe_redone]
    #         redone_undone_operation = UndoManager.__undone_operations.pop()
    #         UndoManager.__undo_operations.append(redone_undone_operation)
    #         UndoManager.__redone_operations.append(redo_operation2)
    #         del UndoManager.__redo_operations[number_of_operation_tobe_redone]
    #         ##redo_operation2 = UndoManager.__redo_operations[0]
    #         ##del UndoManager.__redo_operations[0]
    #         redo_operation.handler(redo_operation.target_object, *redo_operation.arguments)
    #         redo_operation2.handler(redo_operation2.target_object, *redo_operation2.arguments)
    #     else:
    #         redo_operation.handler(redo_operation.target_object, *redo_operation.arguments)
