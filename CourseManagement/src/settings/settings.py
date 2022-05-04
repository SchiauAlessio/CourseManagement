class Settings:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__repository_type = ''
        self.__students_file = ''
        self.__disciplines_file = ''
        self.__grades_file = ''
        self.__content = self.__read_properties_file()

    def __read_properties_file(self):
        file_name_separator = '"'
        with open(self.__file_name) as file:
            content = []
            for line in file:
                if file_name_separator in line:
                    line_content = line.split(file_name_separator, 2)
                    current_information = line_content[1].strip()
                    content.append(current_information)
                else:
                    if '=' in line:
                        line_content = line.split('=', 1)
                        current_information = line_content[1].strip()
                        content.append(current_information)
            return content

    def get_repository_type(self):
        return self.__content[0]

    def set_repository_type(self):
        self.__repository_type = self.__content[0]

    def get_student_file_name(self):
        return self.__content[1]

    def set_student_file_name(self):
        self.__students_file = self.__content[1]

    def get_discipline_file_name(self):
        return self.__content[2]

    def set_discipline_file_name(self):
        self.__disciplines_file = self.__content[2]

    def get_grade_file_name(self):
        return self.__content[3]

    def set_grade_file_name(self):
        self.__grades_file = self.__content[3]

    def file_decisions(self):
        self.set_repository_type()
        self.set_student_file_name()
        self.set_discipline_file_name()
        self.set_grade_file_name()


