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
