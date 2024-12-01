from .base_model import BaseModel


class Specialization(BaseModel):
    '''Класс, описывающий специальность'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self.name = name


class Allowance(BaseModel):
    '''Класс, описывающий пособие'''

    def __init__(self, id: int, amount: float) -> None:
        super().__init__(id)
        self.amount = amount


class ApplicantRequirements(BaseModel):
    '''Класс, описывающий требования к работнику'''

    def __init__(self, id: int, amount: float) -> None:
        super().__init__(id)
        self.amount = amount


class FieldOfActivity(BaseModel):
    '''Класс, описывающий сферы Деятельности'''

    def __init__(self, id: int, amount: float) -> None:
        super().__init__(id)
        self.amount = amount
