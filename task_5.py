class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self._age = age

    def __str__(self):
        return f'{self.__name} {self.__surname}, {self._age}'

    def set_age(self, age):
        if age != 1:
            print('Ошибка: нельзя менять значение более, чем на единицу')
        else:
            self._age += age

    def get_full_name(self):
        return f'{self.__name} {self.__surname}'
