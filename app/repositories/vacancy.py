from .base_repository import BaseRepository
from app.models import Vacancy, VacancyFieldOfActivity
from app.models import VacancyApplicantRequirements
from typing import Tuple


class VacancyRepository(BaseRepository):
    table_name = "vacancy"

    @BaseRepository.execute_query
    def add(self, vacancy: Vacancy) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name}
            (id, position_title, lower_limit_of_salary, upper_limit_of_salary,
            employer_id) VALUES (%s, %s, %s, %s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                vacancy.position_title,
                vacancy.lower_limit_of_salary,
                vacancy.upper_limit_of_salary,
                vacancy.employer_id,
            )
        )

    @BaseRepository.execute_query
    def update(self, vacancy: Vacancy) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            position_title = %s,
            lower_limit_of_salary = %s,
            upper_limit_of_salary = %s,
            employer_id = %s
            WHERE id = %s''',
            (
                vacancy.position_title,
                vacancy.lower_limit_of_salary,
                vacancy.upper_limit_of_salary,
                vacancy.employer_id,
                vacancy.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: str = 'id',
               order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID",
            position_title AS "Должность",
            COALESCE(
                CASE
                    WHEN lower_limit_of_salary IS NULL
                        AND upper_limit_of_salary IS NULL THEN 'Не указано'
                    WHEN lower_limit_of_salary IS NULL
                        THEN 'до ' || upper_limit_of_salary
                    WHEN upper_limit_of_salary IS NULL
                        THEN 'от ' || lower_limit_of_salary
                    ELSE lower_limit_of_salary || ' - ' ||
                        upper_limit_of_salary
                END, 'Не указано'
            ) AS "Зарплата",
            employer_id AS "ID Работодатель"
            FROM {self.table_name}
            ORDER BY {order_by} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))

    @BaseRepository.fetch_results_with_head
    def select_with_join(self, limit: int, offset: int, order_by: str = 'id',
                         order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID",
            position_title AS "Должность",
            lower_limit_of_salary AS "Нижняя граница зарплаты",
            upper_limit_of_salary AS "Верхняя граница зарплаты",
            employer.name AS "Работодатель"
            FROM {self.table_name}
            JEFT JOIN employer ON employer.id = employer_id
            ORDER BY {order_by} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s''',
            (limit, offset))


class VacancyApplicantRequirementsRepository(BaseRepository):
    table_name = "vacancy_applicant_requirements"

    @BaseRepository.execute_query
    def add(self, vacancy_applicant_requirements: VacancyApplicantRequirements
            ) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, vacancy_id,
            applicant_requirements_id) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                vacancy_applicant_requirements.vacancy_id,
                vacancy_applicant_requirements.applicant_requirements_id,
            )
        )

    @BaseRepository.execute_query
    def update(self, vacancy_applicant_requirements:
               VacancyApplicantRequirements) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            applicant_requirements_id = %s
            vacancy_id = %s
            WHERE id = %s''',
            (
                vacancy_applicant_requirements.applicant_requirements_id,
                vacancy_applicant_requirements.vacancy_id,
                vacancy_applicant_requirements.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: str = 'id',
               order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID",
            applicant_requirements_id AS "ID Требования к соискателю",
            vacancy_id AS "ID Вакансия"
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))

    @BaseRepository.fetch_results_with_head
    def select_with_join(self, limit: int, offset: int, order_by: str = 'id',
                         order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID"
            applicant_requirements_id AS "Требования к соискателю",
            vacancy.name AS "Вакансия"
            JOIN applicant_requirements ON applicant_requirements.id
            = applicant_requirements_id
            JOIN vacancy ON vacancy.id = vacancy_id
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))


class VacancyFieldOfActivityRepository(BaseRepository):
    table_name = "vacancy_field_of_activity"

    @BaseRepository.execute_query
    def add(self, vacancy_field_of_activity: VacancyFieldOfActivity
            ) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (id, vacancy_id,
            field_of_activity_id) VALUES (%s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                vacancy_field_of_activity.vacancy_id,
                vacancy_field_of_activity.field_of_activity_id,
            )
        )

    @BaseRepository.execute_query
    def update(self, vacancy_field_of_activity: VacancyFieldOfActivity
               ) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            field_of_activity_id = %s,
            vacancy_id = %s
            WHERE vacancy_id = %s''',
            (
                vacancy_field_of_activity.field_of_activity_id,
                vacancy_field_of_activity.vacancy_id,
                vacancy_field_of_activity.id,
            )
        )

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: str = 'id',
               order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID",
            field_of_activity_id AS "ID Сферы деятельности",
            vacancy_id AS "ID Вакансия"
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))

    @BaseRepository.fetch_results_with_head
    def select_with_join(self, limit: int, offset: int, order_by: str = 'id',
                         order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID"
            field_of_activity_id AS "Сферы деятельности",
            vacancy.name AS "Вакансия"
            JOIN field_of_activity ON field_of_activity.id
            = field_of_activity_id
            JOIN vacancy ON vacancy.id = vacancy_id
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))
