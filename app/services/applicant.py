# flake8: noqa
from app.repositories import ApplicantRepository
from app.models import Applicant

class ApplicantService:
    table_fields: tuple = ('id', 'Фамилия', 'Имя', 'Отчетсво', 'Возраст', 'Номер паспорта', 'Дата выдачи паспорта', 'Кем выдан паспорт', 
                    'id-Город', 'id-Улица', 'Номер дома', 'Номер телефона', 'Фотография', 'id-Уровень образования', 
                    'id-Документ об образовании', 'Данные документа об образовании', 'Дата потсановки на учет', 'id-Пособие')
    
    __repository = ApplicantRepository()

    def __init__(self, limit = 10, offset = 0) -> None:
        self.limit = limit
        self.offset = offset
        self.table = self.__repository.get_paginated(limit, offset)

    def this_last_page(self) -> bool:
        return  bool(self.__repository.get_paginated(self.limit, self.offset + self.limit))

    def next_page(self) -> None:
        if not self.this_last_page():
            self.offset += self.limit
            self.table = self.__repository.get_paginated(self.limit, self.offset)

    def update_limit_and_offset(self, limit: int, offset: int) -> None:
        self.limit = limit
        self.offset = offset
        self.table = self.__repository.get_paginated(self.limit, self.offset)

    def update_table(self, data: dict) -> None:
        apl = Applicant(*data.values())
        values = apl.get_values()
        self.__repository.update_by_id(values.pop('id'), values) 
        self.table = self.__repository.get_paginated(self.limit, self.offset)

    def get_count(self) -> int:
        count = self.__repository.get_count()
        return count[0][0]
