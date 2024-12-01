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
            (position_title, lower_limit_of_salary, upper_limit_of_salary,
            employer_id) VALUES (%s, %s, %s, %s)''',
            (
                vacancy.position_title,
                vacancy.lower_limit_of_salary,
                vacancy.upper_limit_of_salary,
                vacancy.employer_id,
            )
        )


class VacancyApplicantRequirementsRepository(BaseRepository):
    table_name = "vacancy_applicant_requirements"

    @BaseRepository.execute_query
    def add(self, req: VacancyApplicantRequirements) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (vacancy_id,
            applicant_requirements_id) VALUES (%s, %s)''',
            (req.vacancy_id, req.applicant_requirements_id)
        )


class VacancyFieldOfActivityRepository(BaseRepository):
    table_name = "vacancy_field_of_activity"

    @BaseRepository.execute_query
    def add(self, activity: VacancyFieldOfActivity) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (vacancy_id,
            field_of_activity_id) VALUES (%s, %s)''',
            (activity.vacancy_id, activity.field_of_activity_id)
        )
