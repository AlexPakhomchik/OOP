from functools import reduce
class Student():
    def __init__(self, first_name: str, last_name: str, group: str, marks: list):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.marks = marks
    def add_mark(self, mark):
        """def add_mark() Принимает оценку и добавляет её в marks.
        Если значение меньше 0 или больше 10,
        то значение не добавляется"""
        if mark >= 0 and mark <= 10:
            self.marks.append(mark)
    def _get_average_mark(self):
        """
        def _get_average_mark()Возвращает средний балл"""
        return reduce(lambda x, y: x + y, self.marks) / len(self.marks)

    def get_scholarship(self):
        """
        def get_scholarship() Возвращает сумму стипендии.
        Если средняя оценка студента равна 5, то сумма 500, иначе 150"""
        print(f'Стипендия студента {self.first_name} {self.last_name} - {150 if self._get_average_mark() < 5 else 500}')



class Aspirant(Student):
    def __init__(self, first_name: str, last_name: str, group: str, scientific_publications: list, marks: list):
        super().__init__(first_name, last_name, group, marks)
        self.scientific_publications = scientific_publications
    def get_scholarship(self):
        print(f'Стипендия аспиранта {self.first_name} {self.last_name} - {250 if self._get_average_mark() < 5 else 700}')
