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

        try:
            self.applicant_id = int(applicant_id)
        except Exception:
            raise Exception('Введен неверный для ID Соискатель: '
                            f'{applicant_id}')
        try:
            self.vacancy_id = int(vacancy_id)
        except Exception:
            raise Exception('Введен неверный для ID Вакансия: '
                            f'{vacancy_id}')

        if isinstance(signature_date, str):
            try:
                self.signature_date = date.fromisoformat(signature_date)
            except Exception:
                raise Exception('Введен неверный формат даты подписания: '
                                f'{signature_date}')
        else:
            self.signature_date = signature_date
