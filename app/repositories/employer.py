from .base_repository import BaseRepository
from app.models import Employer
from typing import Tuple


class EmployerRepository(BaseRepository):
    table_name = "employer"

    @BaseRepository.execute_query
    def add(self, employer: Employer) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, name, city_id, street_id,
            house_number, phone_number) VALUES (%s, %s, %s, %s, %s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                employer.name,
                employer.city_id,
                employer.street_id,
                employer.house_number,
                employer.phone_number,
            )
        )

    @BaseRepository.execute_query
    def update(self, employer: Employer) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            name = %s,
            city_id = %s,
            street_id = %s,
            house_number = %s,
            phone_number = %s
            WHERE id = %s''',
            (
                employer.name,
                employer.city_id,
                employer.street_id,
                employer.house_number,
                employer.phone_number,
                employer.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: int = 0,
               order_acs: bool = True) -> Tuple[str, tuple]:
        title = ['id', 'name', 'city_id', 'street_id', 'house_number',
                 'phone_number']

        return (
            f'''SELECT id AS "ID",
            name AS "Название",
            city_id AS "ID Город",
            street_id AS "ID Улица",
            house_number AS "Номер дома",
            phone_number AS "Номер телефона"
            FROM {self.table_name}
            ORDER BY {title[order_by]} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))

    @BaseRepository.fetch_results_with_head
    def select_with_join(self, limit: int, offset: int, order_by: int = 0,
                         order_acs: bool = True) -> Tuple[str, tuple]:
        title = ['employer.id', 'name', 'city.name, street.name, house_number',
                 'phone_number']

        return (
            f'''SELECT employer.id AS "ID",
            name AS "Название",
            'г. ' || city.name || ', ул. ' || street.name || ', д. '
            || house_number AS Адрес,
            phone_number AS "Номер телефона"
            FROM {self.table_name}
            LEFT JOIN city ON city_id = city.id
            LEFT JOIN street ON street_id = street.id
            ORDER BY {title[order_by]} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))
