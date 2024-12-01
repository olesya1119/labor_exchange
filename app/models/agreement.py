from .base_model import BaseModel
from datetime import date


class Agreement(BaseModel):
    '''Класс, описывающий соглашение'''
    def __init__(self, id: int, applicant_id: int, vacancy_id: int,
                 signature_date: date) -> None:
        super().__init__(id)
        self.applicant_id = applicant_id
        self.vacancy_id = vacancy_id
        self.signature_date = signature_date
