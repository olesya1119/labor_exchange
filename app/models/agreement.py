from .base_model import BaseModel
from datetime import date


class Agreement(BaseModel):
    '''Класс, описывающий соглашение'''
    def __init__(
        self,
        id: int | None,
        applicant_id: int | str,
        vacancy_id: int | str,
        signature_date: str | date
    ):
        super().__init__(id)

        self.applicant_id = int(applicant_id)
        self.vacancy_id = int(vacancy_id)

        if isinstance(signature_date, str):
            self.signature_date = date.fromisoformat(signature_date)
        else:
            self.signature_date = signature_date
