from .base_model import BaseModel
from datetime import date


class Archive(BaseModel):
    '''Класс, описывающий архив'''
    def __init__(
        self,
        id: int | None,
        applicant_id: int | str,
        archive_date: str | date,
        performed_by: str
    ):
        super().__init__(id)
        self.applicant_id = int(applicant_id)

        if isinstance(archive_date, str):
            self.archive_date = date.fromisoformat(archive_date)
        else:
            self.archive_date = archive_date

        self.performed_by = performed_by
