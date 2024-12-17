from .base_model import BaseModel


class Specialization(BaseModel):
    '''Класс, описывающий специальность'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self.name = name
        if len(name) > 50:
            raise Exception(f'Значение {name} слишком большое.'
                            'Введите меньше 50 символов')


class Allowance(BaseModel):
    '''Класс, описывающий пособие'''

    def __init__(self, id: int, amount: float | str) -> None:
        super().__init__(id)
        try:
            if float(amount) < 0:
                raise Exception('Значение пособия не может быть отрицательным')

            self.amount = float(amount)
        except Exception:
            raise Exception(f'Значение пособия {amount} некорректное')


class ApplicantRequirements(BaseModel):
    '''Класс, описывающий требования к работнику'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        if len(name) > 100:
            raise Exception(f'Значение {name} слишком большое.'
                            'Введите меньше 100 символов')
        self.name = name


class FieldOfActivity(BaseModel):
    '''Класс, описывающий сферы Деятельности'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        if len(name) > 50:
            raise Exception(f'Значение {name} слишком большое.'
                            'Введите меньше 50 символов')
        self.name = name
