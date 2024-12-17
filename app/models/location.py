from .base_model import BaseModel


class City(BaseModel):
    '''Класс, описывающий город'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        if len(name) > 25:
            raise Exception(f'Значение {name} слишком большое.'
                            'Введите меньше 25 символов')
        self.name = name


class Street(BaseModel):
    '''Класс, описывающий улицу'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        if len(name) > 25:
            raise Exception(f'Значение {name} слишком большое.'
                            'Введите меньше 25 символов')
        self.name = name
