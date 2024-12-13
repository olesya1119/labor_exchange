from .base_repository import BaseRepository
from app.models import Specialization, Allowance, FieldOfActivity
from app.models import ApplicantRequirements
from typing import Tuple


class SpecializationRepository(BaseRepository):
    table_name = "specialization"

    @BaseRepository.execute_query
    def add(self, specialization: Specialization) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, name) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                specialization.name,
            )
        )

    @BaseRepository.execute_query
    def update(self, specialization: Specialization) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            name = %s
            WHERE id = %s''',
            (
                specialization.name,
                specialization.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: int = 0,
               order_acs: bool = True) -> Tuple[str, tuple]:
        title = ['id', 'name']

        return (
            f'''SELECT id AS "ID",
            name AS "Название специализации"
            FROM {self.table_name}
            ORDER BY {title[order_by]} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))

    def select_with_join(self, limit: int, offset: int, order_by: int = 0,
                         order_acs: bool = True):
        self.select(self, limit, offset, order_by, order_acs)


class AllowanceRepository(BaseRepository):
    table_name = "allowance"

    @BaseRepository.execute_query
    def add(self, allowance: Allowance) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, amount) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                allowance.amount,
            )
        )

    @BaseRepository.execute_query
    def update(self, allowance: Allowance) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            amount = %s
            WHERE id = %s''',
            (
                allowance.amount,
                allowance.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: int = 0,
               order_acs: bool = True) -> Tuple[str, tuple]:
        title = ['id', 'amount']

        return (
            f'''SELECT id AS "ID",
            amount AS "Размер пособия"
            FROM {self.table_name}
            ORDER BY {title[order_by]} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))

    def select_with_join(self, limit: int, offset: int, order_by: int = 0,
                         order_acs: bool = True):
        self.select(self, limit, offset, order_by, order_acs)


class ApplicantRequirementsRepository(BaseRepository):
    table_name = "applicant_requirements"

    @BaseRepository.execute_query
    def add(self, applicant_requirements: ApplicantRequirements
            ) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, name) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                applicant_requirements.name,
            )
        )

    @BaseRepository.execute_query
    def update(self, applicant_requirements: ApplicantRequirements
               ) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            name = %s
            WHERE id = %s''',
            (
                applicant_requirements.name,
                applicant_requirements.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: int = 0,
               order_acs: bool = True) -> Tuple[str, tuple]:
        title = ['id', 'name']

        return (
            f'''SELECT id AS "ID",
            name AS "Требование к соискателю"
            FROM {self.table_name}
            ORDER BY {title[order_by]} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))

    def select_with_join(self, limit: int, offset: int, order_by: int = 0,
                         order_acs: bool = True):
        self.select(self, limit, offset, order_by, order_acs)


class FieldOfActivityRepository(BaseRepository):
    table_name = "field_of_activity"

    @BaseRepository.execute_query
    def add(self, field_of_activity: FieldOfActivity) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, name) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                field_of_activity.name,
            )
        )

    @BaseRepository.execute_query
    def update(self, field_of_activity: FieldOfActivity) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            name = %s
            WHERE id = %s''',
            (
                field_of_activity.name,
                field_of_activity.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: int = 0,
               order_acs: bool = True) -> Tuple[str, tuple]:
        title = ['id', 'name']

        return (
            f'''SELECT id AS "ID",
            name AS "Название сферы деятельности"
            FROM {self.table_name}
            ORDER BY {title[order_by]} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))

    def select_with_join(self, limit: int, offset: int, order_by: int = 0,
                         order_acs: bool = True):
        self.select(self, limit, offset, order_by, order_acs)
