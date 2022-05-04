import unittest

from DataStructure_sort_filter.filter import Filtering
from DataStructure_sort_filter.iterable import IterableDataStructure
from DataStructure_sort_filter.iterable_dictionary import IterableDataStructureDictionary
from DataStructure_sort_filter.sorting import Sorting
from domain.student import Student


class Test(unittest.TestCase):
    def test_iterable_list(self):
        repository = IterableDataStructure()
        repository.append(Student(1, 'student1'))
        repository.append(Student(2, 'student2'))
        self.assertEqual(len(repository), 2)
        self.assertListEqual(repository.elements,[Student(1, 'student1'),Student(2, 'student2')])
        repository[0] = Student(1, 'student1')
        repository[1] = Student(2, 'student2')
        self.assertEqual(repository[0], Student(1, 'student1'))
        iter(repository)
        self.assertEqual(next(repository), Student(1, 'student1'))
        self.assertEqual(next(repository), Student(2, 'student2'))
        self.assertRaises(StopIteration, next, repository)
        del repository[0]

    def test_iterable_dictionary(self):
        repository=IterableDataStructureDictionary()
        repository[0]=Student(1,'student1')
        repository[1]=Student(2, 'student2')
        self.assertEqual(len(repository),2)
        self.assertEqual(repository[0], Student(1, 'student1'))
        self.assertListEqual(repository.values(),[Student(1,'student1'),Student(2, 'student2')])
        del repository[0]
        self.assertEqual(repository[1],Student(2,'student2'))
        del repository[1]
        self.assertEqual(len(repository),0)
        repository[0] = Student(1, 'student1')
        repository[1] = Student(2, 'student2')
        iter(repository)


    def test_sorting(self):
        number_list = [-1, 12, -9, 7, 2, 1, 3]
        Sorting.sort(number_list)
        self.assertListEqual(number_list, [-9, -1, 1, 2, 3, 7, 12])
        Sorting.sort(number_list, reverse=True)
        self.assertListEqual(number_list, [12, 7, 3, 2, 1, -1, -9])
        Sorting.sort(number_list)
        self.assertListEqual(number_list, number_list)
        student1=Student(1, 'd')
        student2=Student(7, 'c')
        student3=Student(3, 'a')
        student4=Student(4, 'e')
        student5 =Student(2, 'c')
        people_list = [student1,student2,student3,student4,student5]
        Sorting.sort(people_list, key=lambda student: student.get_student_id())
        self.assertListEqual(people_list, [student1, student5, student3, student4, student2])
        Sorting.sort(people_list, key=lambda student: student.get_student_name())
        self.assertListEqual(people_list, [student3,student5,student2,student1,student4])

        def student_less_than(student1, student2):
            # name descending,id descending
            if student1.get_student_name().lower() == student2.get_student_name().lower():
                return student1.get_student_id() > student2.get_student_id()
            return student1.get_student_name().lower() > student2.get_student_name().lower()

        people_list = [student1, student2, student3, student4, student5]
        Student.__lt__ = student_less_than
        Student.__gt__ = lambda student1, student2: not student_less_than(student1, student2)
        Sorting.sort(people_list)
        self.assertListEqual(people_list,[student4,student1,student2,student5,student3])

        def true(x, y):
            return True

        people_list = [student1, student2, student3, student4, student5]
        Student.__lt__ = true
        Student.__gt__ = lambda x, y: not true(x, y)
        Sorting.sort(people_list)
        self.assertListEqual(people_list, [student1, student2, student3, student4, student5])

    def test_filter(self):
        number_list = [-1, 12, -9, 7, 2, 1, 3]
        Filtering.filter(number_list)
        self.assertListEqual(number_list, [-1, 12, -9, 7, 2, 1, 3])

        def keep_number(x):
            return x >= 0

        Filtering.filter(number_list, key=keep_number)
        self.assertListEqual(number_list, [12, 7, 2, 1, 3])

        p1=Student(1, 'bro')
        p2=Student(2, 'bro2')
        p3=Student(3, 'Bun')
        p4=Student(4, 'Alt bun')
        p5=Student(5, 'bro bun de sters')
        people_list = [p1, p2, p3, p4, p5]

        def keep_person(student):
            return 'bro' not in student.get_student_name().lower()

        Filtering.filter(people_list, key=keep_person)
        self.assertListEqual(people_list, [p3, p4])
