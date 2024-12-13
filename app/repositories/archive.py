from .base_repository import BaseRepository
from app.models import Archive
from typing import Tuple


class ArchiveRepository(BaseRepository):
    table_name = "archive"

    @BaseRepository.execute_query
    def add(self, archive: Archive) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, applicant_id, archive_date,
            performed_by) VALUES (%s, %s, %s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                archive.applicant_id,
                archive.archive_date,
                archive.performed_by,
            )
        )

    @BaseRepository.execute_query
    def update(self, archive: Archive) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            applicant_id = %s,
            archive_date = %s,
            performed_by = %s
            WHERE id = %s''',
            (
                archive.applicant_id,
                archive.archive_date,
                archive.performed_by,
                archive.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: str = 'id',
               order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID",
            applicant_id AS "ID Соискатель",
            archive_date AS "Дата перевода в архив",
            performed_by AS "Лицо, выполнившее операцию"
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))

    @BaseRepository.fetch_results_with_head
    def select_with_join(self, limit: int, offset: int, order_by: str = 'id',
                         order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID"
            applicant.last_name | ' ' | applicant.first_name |
            ' ' | applicant.middle_name AS "Соискатель",
            archive_date AS "Дата перевода в архив",
            performed_by AS "Лицо, выполнившее операцию"
            JOIN applicant ON applicant.id = applicant_id
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))
