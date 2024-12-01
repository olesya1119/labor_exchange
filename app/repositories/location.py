from .base_repository import BaseRepository
from app.models import City, Street
from typing import Tuple


class CityRepository(BaseRepository):
    table_name = "city"

    @BaseRepository.execute_query
    def add(self, city: City) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (name) VALUES (%s)''',
            (city.name,)
        )


class StreetRepository(BaseRepository):
    table_name = "street"

    @BaseRepository.execute_query
    def add(self, street: Street) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (name) VALUES (%s)''',
            (street.name,)
        )
