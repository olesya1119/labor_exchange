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
