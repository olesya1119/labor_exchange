from .base_repository import BaseRepository
from app.models import Archive
from typing import Tuple


class ArchiveRepository(BaseRepository):
    table_name = "archive"

    @BaseRepository.execute_query
    def add(self, archive: Archive) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (applicant_id, archive_date,
            performed_by) VALUES (%s, %s, %s)''',
            (
                archive.applicant_id,
                archive.archive_date,
                archive.performed_by,
            )
        )
