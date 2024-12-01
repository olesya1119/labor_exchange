from .base_repository import BaseRepository
from app.models import Employer
from typing import Tuple


class EmployerRepository(BaseRepository):
    table_name = "employer"

    @BaseRepository.execute_query
    def add(self, employer: Employer) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (name, city_id, street_id,
            house_number, phone_number) VALUES (%s, %s, %s, %s, %s)''',
            (
                employer.name,
                employer.city_id,
                employer.street_id,
                employer.house_number,
                employer.phone_number,
            )
        )
