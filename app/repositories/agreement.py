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
            applicant_d = %s,
            vacancy_id = %s,
            signature_date = %s
            WHERE id = %s
            ''',
            (agreement.applicant_id,
             agreement.vacancy_id,
             agreement.signature_date,
             agreement.id))

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: int = 0,
               order_acs: bool = True) -> Tuple[str, tuple]:
        title = ['id', 'agreement.id', 'vacancy_id', 'signature_date']

        return (
            f'''SELECT id AS "ID",
            agreement.id AS "ID Соискатель",
            vacancy_id AS "ID Вакансия",
            signature_date AS "Дата подписания"
            FROM {self.table_name}
            ORDER BY {title[order_by]} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))

    @BaseRepository.fetch_results_with_head
    def select_with_join(self, limit: int, offset: int, order_by: int = 0,
                         order_acs: bool = True) -> Tuple[str, tuple]:
        title = ['id', 'applicant.last_name, applicant.first_name, '
                 'applicant.middle_name', 'vacancy.position_title',
                 'signature_date']
        return (
            f'''SELECT agreement.id AS "ID"
            applicant.last_name | ' ' | applicant.first_name |
            ' ' | applicant.middle_name AS "Соискатель",
            vacancy.position_title AS "Вакансия",
            signature_date AS "Дата подписания"
            LEFT JOIN applicant ON applicant.id = applicant_id
            LEFT JOIN vacancy ON vacancy.id = vacancy_id
            FROM {self.table_name}
            ORDER BY {title[order_by]} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))
