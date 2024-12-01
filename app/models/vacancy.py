from .base_model import BaseModel
from .employer import Employer
from .specialization import ApplicantRequirements, FieldOfActivity


class Vacancy(BaseModel):
    '''Класс, описывающий вакансию'''
    def __init__(self, id: int, position_title: str,
                 lower_limit_of_salary: int, upper_limit_of_salary: int,
                 employer: Employer
                 ) -> None:
        super().__init__(id)
        self.position_title = position_title
        self.lower_limit_of_salary = lower_limit_of_salary
        self.upper_limit_of_salary = upper_limit_of_salary
        self.employer = employer


class VacancyApplicantRequirements(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int, vacancy: Vacancy,
                 applicant_requirements: ApplicantRequirements
                 ) -> None:
        super().__init__(id)
        self.vacancy = vacancy
        self.applicant_requirements = applicant_requirements


class VacancyFieldOfActivity(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int, vacancy: Vacancy,
                 field_of_activity: FieldOfActivity
                 ) -> None:
        super().__init__(id)
        self.vacancy = vacancy
        self.field_of_activity = field_of_activity
