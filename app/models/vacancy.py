from .base_model import BaseModel


class Vacancy(BaseModel):
    '''Класс, описывающий вакансию'''
    def __init__(self, id: int, position_title: str,
                 lower_limit_of_salary: int, upper_limit_of_salary: int,
                 employer_id: int
                 ) -> None:
        super().__init__(id)
        self.position_title = position_title
        self.lower_limit_of_salary = lower_limit_of_salary
        self.upper_limit_of_salary = upper_limit_of_salary
        self.employer_id = employer_id


class VacancyApplicantRequirements(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int, vacancy_id: int,
                 applicant_requirements_id: int
                 ) -> None:
        super().__init__(id)
        self.vacancy_id = vacancy_id
        self.applicant_requirements_id = applicant_requirements_id


class VacancyFieldOfActivity(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int, vacancy_id: int,
                 field_of_activity_id: int
                 ) -> None:
        super().__init__(id)
        self.vacancy_id = vacancy_id
        self.field_of_activity_id = field_of_activity_id
