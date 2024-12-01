from .base_model import BaseModel


class EducationalInstitution(BaseModel):
    '''Класс, описывающий учебное заведение'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self.name = name


class EducationLevel(BaseModel):
    '''Класс, описывающий уровень образования'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self.name = name


class EducationDocument(BaseModel):
    '''Класс, описывающий документ об образовании'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self.name = name
