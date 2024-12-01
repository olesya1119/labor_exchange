from .base_model import BaseModel
from .applicant import Applicant
from .vacancy import Vacancy
from datetime import date


class Agreement(BaseModel):
    '''Класс, описывающий соглашение'''
    def __init__(self, id: int, applicant: Applicant, vacancy: Vacancy,
                 signature_date: date) -> None:
        super().__init__(id)
        self.applicant = applicant
        self.vacancy = vacancy
        self.signature_date = signature_date
