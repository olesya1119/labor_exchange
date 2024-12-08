from .base_model import BaseModel


class Employer(BaseModel):
    '''Класс, описывающий работадателя'''

    def __init__(self, id: int | str, name: str, city_id: int | str,
                 street_id: int | str,
                 house_number: str,
                 phone_number: str) -> None:
        super().__init__(id)
        self.name = name
        self.city_id = int(city_id)
        self.street_id = int(street_id)
        self.house_number = house_number
        self.phone_number = phone_number
