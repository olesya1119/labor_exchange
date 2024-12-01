from .base_model import BaseModel
from .location import Street, City


class Employer(BaseModel):
    '''Класс, описывающий работадателя'''
    def __init__(self, id: int, name: str, city: City,
                 street: Street, house_number: str, phone_number: str) -> None:
        super().__init__(id)
        self.name = name
        self.city = city
        self.street = street
        self.house_number = house_number
        self.phone_number = phone_number
