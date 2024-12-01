from .base_repository import BaseRepository
from app.models import Agreement
from typing import Tuple


class AgreementRepository(BaseRepository):
    table_name = 'agreement'

    @BaseRepository.execute_query
    def add(self, agreement: Agreement) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (applicant_id, vacancy_id,
            signature_date) VALUES (%s, %s, %s)''',
            (agreement.applicant_id,
             agreement.vacancy_id,
             agreement.signature_date))
