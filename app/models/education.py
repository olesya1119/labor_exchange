from .base_model import BaseModel


class EducationalInstitution(BaseModel):
    '''Класс, описывающий учебное заведение'''

    def __init__(self, id: int | str, name: str) -> None:
        super().__init__(id)
        if len(name) > 50:
            raise Exception(f'Значение {name} слишком большое.'
                            'Введите меньше 50 символов')
        self.name = name


class EducationLevel(BaseModel):
    '''Класс, описывающий уровень образования'''

    def __init__(self, id: int | str, name: str) -> None:
        super().__init__(id)
        if len(name) > 50:
            raise Exception(f'Значение {name} слишком большое.'
                            'Введите меньше 50 символов')
        self.name = name


class EducationDocument(BaseModel):
    '''Класс, описывающий документ об образовании'''

    def __init__(self, id: int | str, name: str) -> None:
        super().__init__(id)
        if len(name) > 50:
            raise Exception(f'Значение {name} слишком большое.'
                            'Введите меньше 50 символов')
        self.name = name
