from .base_model import BaseModel


class Vacancy(BaseModel):
    '''Класс, описывающий вакансию'''
    def __init__(
        self,
        id: int | None,
        position_title: str,
        lower_limit_of_salary: int | str,
        upper_limit_of_salary: int | str,
        employer_id: int | str
    ) -> None:
        super().__init__(id)
        self.position_title = position_title
        self.lower_limit_of_salary = int(lower_limit_of_salary)
        self.upper_limit_of_salary = int(upper_limit_of_salary)
        self.employer_id = int(employer_id)


class VacancyApplicantRequirements(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int | str | None, vacancy_id: int | str,
                 applicant_requirements_id: int | str
                 ) -> None:
        super().__init__(id)
        self.vacancy_id = int(vacancy_id)
        self.applicant_requirements_id = int(applicant_requirements_id)


class VacancyFieldOfActivity(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int | str | None, vacancy_id: int | str,
                 field_of_activity_id: int | str
                 ) -> None:
        super().__init__(id)
        self.vacancy_id = int(vacancy_id)
        self.field_of_activity_id = int(field_of_activity_id)
