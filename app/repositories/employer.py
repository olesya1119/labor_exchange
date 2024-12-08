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
