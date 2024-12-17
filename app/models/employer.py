from .base_model import BaseModel


class Employer(BaseModel):
    '''Класс, описывающий работадателя'''

    def __init__(self, id: int | str, name: str, city_id: int | str,
                 street_id: int | str,
                 house_number: str,
                 phone_number: str) -> None:
        super().__init__(id)
        if len(name) > 50:
            raise Exception(f'Значение {name} слишком большое.'
                            'Введите меньше 50 символов')
        self.name = name
        try:
            self.city_id = int(city_id)
        except Exception:
            raise Exception('Введен неверный для ID Город: '
                            f'{city_id}')
        try:
            self.street_id = int(street_id)
        except Exception:
            raise Exception('Введен неверный для ID Улица: '
                            f'{street_id}')
        if len(house_number) > 5:
            raise Exception(f'Значение {house_number} слишком большое.'
                            'Введите меньше 5 символов')
        self.house_number = house_number

        if self.is_valid_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            raise Exception('Номер телефона имеет некорректный формат')
