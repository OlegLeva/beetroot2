class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def data_person(self):
        if self.gender == 'мужчина':
            return f'Это {self.gender} {self.name} ему {self.age}'
        if self.gender == 'женщина':
            return f'Это {self.gender} {self.name} ей {self.age}'


class Teacher(Person):
    def __init__(self, name, age, gender, science, academic_degrees):
        super().__init__(name, age, gender)
        self.science = science
        self.academic_degrees = academic_degrees

    def data_teacher(self):
        return f'Имеет cтепень {self.academic_degrees}, и преподаёт {self.science}'


class Student(Person):
    def __init__(self, name, age, gender, status, faculty):
        super().__init__(name, age, gender)
        self.status = status
        self.faculty = faculty


berger = Teacher('Бергер', 72, 'мужчина', 'политология', 'профессор')
print(berger.data_person(), berger.data_teacher())
leva = Student('Oleg', 42, 'мужчина', 'stacionar', 'managment')
print(leva.data_person(), leva.faculty)
