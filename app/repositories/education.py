from .base_repository import BaseRepository
from app.models import EducationalInstitution, EducationLevel
from app.models import EducationDocument
from typing import Tuple


class EducationalInstitutionRepository(BaseRepository):
    table_name = "educational_institution"

    @BaseRepository.execute_query
    def add(self, educational_institution: EducationalInstitution
            ) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, name) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                educational_institution.name,
            )
        )

    @BaseRepository.execute_query
    def update(self, educational_institution: EducationalInstitution
               ) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            name = %s
            WHERE id = %s''',
            (
                educational_institution.name,
                educational_institution.id,
            )
        )


class EducationLevelRepository(BaseRepository):
    table_name = "education_level"

    @BaseRepository.execute_query
    def add(self, education_level: EducationLevel) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, name) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                education_level.name,
            )
        )

    @BaseRepository.execute_query
    def update(self, education_level: EducationLevel) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            name = %s
            WHERE id = %s''',
            (
                education_level.name,
                education_level.id,
            )
        )


class EducationDocumentRepository(BaseRepository):
    table_name = "education_document"

    @BaseRepository.execute_query
    def add(self, education_document: EducationDocument) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, name) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                education_document.name,
            )
        )

    @BaseRepository.execute_query
    def update(self, education_document: EducationDocument
               ) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            name = %s
            WHERE id = %s''',
            (
                education_document.name,
                education_document.id,
            )
        )
