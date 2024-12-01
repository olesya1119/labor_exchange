from .base_repository import BaseRepository
from app.models import EducationalInstitution, EducationLevel
from app.models import EducationDocument
from typing import Tuple


class EducationalInstitutionRepository(BaseRepository):
    table_name = "educational_institution"

    @BaseRepository.execute_query
    def add(self, institution: EducationalInstitution) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (name) VALUES (%s)''',
            (institution.name,)
        )


class EducationLevelRepository(BaseRepository):
    table_name = "education_level"

    @BaseRepository.execute_query
    def add(self, level: EducationLevel) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (name) VALUES (%s)''',
            (level.name,)
        )


class EducationDocumentRepository(BaseRepository):
    table_name = "education_document"

    @BaseRepository.execute_query
    def add(self, document: EducationDocument) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (name) VALUES (%s)''',
            (document.name,)
        )
