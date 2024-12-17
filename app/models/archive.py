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
        try:
            self.applicant_id = int(applicant_id)
        except Exception:
            raise Exception('Введен неверный для ID Соискатель: '
                            f'{applicant_id}')

        if isinstance(archive_date, str):
            try:
                self.archive_date = date.fromisoformat(archive_date)
            except Exception:
                raise Exception('Введен неверный формат даты перевода: '
                                f'{archive_date}')
        else:
            self.archive_date = archive_date

        if len(performed_by) > 100:
            raise Exception(f'Значение {performed_by} слишком большое.'
                            'Введите меньше 100 символов')

        self.performed_by = performed_by
