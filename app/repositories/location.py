from .base_repository import BaseRepository
from app.models import City, Street
from typing import Tuple


class CityRepository(BaseRepository):
    table_name = "city"

    @BaseRepository.execute_query
    def add(self, city: City) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, name) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                city.name,
            )
        )

    @BaseRepository.execute_query
    def update(self, city: City) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            name = %s
            WHERE id = %s''',
            (
                city.name,
                city.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: str = 'id',
               order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID",
            name AS "Название города",
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))

    def select_with_join(self, limit: int, offset: int, order_by: str = 'id',
                         order_acs: bool = True):
        self.select(self, limit, offset, order_by, order_acs)


class StreetRepository(BaseRepository):
    table_name = "street"

    @BaseRepository.execute_query
    def add(self, street: Street) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, name) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                street.name,
            )
        )

    @BaseRepository.execute_query
    def update(self, street: Street) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            name = %s
            WHERE id = %s''',
            (
                street.name,
                street.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: str = 'id',
               order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID",
            name AS "Название улицы",
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))

    def select_with_join(self, limit: int, offset: int, order_by: str = 'id',
                         order_acs: bool = True):
        self.select(self, limit, offset, order_by, order_acs)
