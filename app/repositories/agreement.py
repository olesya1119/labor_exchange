from .base_repository import BaseRepository
from app.models import Agreement
from typing import Tuple


class AgreementRepository(BaseRepository):
    table_name = 'agreement'

    @BaseRepository.execute_query
    def add(self, agreement: Agreement) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, applicant_id, vacancy_id,
            signature_date) VALUES (%s, %s, %s, %s)''',
            (self.get_last_id + 1,
             agreement.applicant_id,
             agreement.vacancy_id,
             agreement.signature_date))

    @BaseRepository.execute_query
    def update(self, agreement: Agreement) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            applicant_id = %s,
            vacancy_id = %s,
            signature_date = %s
            WHERE id = %s
            ''',
            (agreement.applicant_id,
             agreement.vacancy_id,
             agreement.signature_date,
             agreement.id))
