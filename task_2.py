class Student():
    def __init__(self, first_name: str, last_name: str, group: str, marks: list):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.marks = marks
    """def add_mark() Принимает оценку и добавляет её в marks.
    Если значение меньше 0 или больше 10, 
    то значение не добавляется"""
    def add_mark(self, mark):
        if mark >= 0 and mark <= 10:
            self.marks.append(str(mark))
    """
    def _get_average_mark()Возвращает средний балл"""
    def _get_average_mark(self):
        counter = 0
        sum = 0
        for i in self.marks:
            sum += int(i)
            counter += 1
        return sum / counter
        # print(sum / counter)
    """
    def get_scholarship() Возвращает сумму стипендии. 
    Если средняя оценка студента равна 5, то сумма 500, иначе 150"""
    def get_scholarship(self):
        scholarship_low = f'Стипендия студента {self.first_name} {self.last_name} - 150'
        scholarship_high = f'Стипендия студента {self.first_name} {self.last_name} - 500'
        if self._get_average_mark() >= 5:
            print(scholarship_high)
        else:
            print(scholarship_low)
class Aspirant(Student):
    def __init__(self, first_name: str, last_name: str, group: str, scientific_publications: list, marks: list):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.marks = marks
        self.scientific_publications = scientific_publications
    def get_scholarship(self):
        scholarship_low = f'Стипендия аспиранта {self.first_name} {self.last_name} - 250'
        scholarship_high = f'Стипендия аспиранта {self.first_name} {self.last_name} - 700'
        if self._get_average_mark() >= 5:
            print(scholarship_high)
        else:
            print(scholarship_low)

alex = Student('Alex', 'Pakhomchik', '221b', [])
alex.add_mark(5)
alex.add_mark(6)
alex.get_scholarship()

john = Aspirant('John', 'Wick', 'Continental', ['How to avenge a dog for 4 movies'], [])
john.add_mark(7)
john.add_mark(8)
john.get_scholarship()