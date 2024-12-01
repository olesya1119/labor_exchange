from .base_model import BaseModel


class City(BaseModel):
    '''Класс, описывающий город'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self.name = name


class Street(BaseModel):
    '''Класс, описывающий улицу'''

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self.name = name
