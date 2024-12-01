from .base_model import BaseModel
from .applicant import Applicant
from datetime import date


class Archive(BaseModel):
    '''Класс, описывающий архив'''
    def __init__(self, id: int, applicant: Applicant, archive_date: date,
                 performed_by: str) -> None:
        super().__init__(id)
        self.applicant = applicant
        self.archive_date = archive_date
        self.performed_by = performed_by
