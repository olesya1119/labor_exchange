from .base_model import BaseModel
from datetime import date, datetime


class Applicant(BaseModel):
    '''Класс, описывающий безработного(соискателя)'''

    def __init__(self, id: int | str | None, last_name: str | str,
                 first_name: str,
                 middle_name: str | None, age: int | str,
                 passport_number: int | str,
                 passport_issue_date: date | str,  passport_issued_by: str,
                 city_id: int | str, street_id: int | str, house_number: str,
                 phone_number: str, photo: str,
                 education_level_id: int | str,
                 education_document_id: int | str,
                 education_document_details: str,
                 registration_date: date | str,
                 allowance_id: int | None | str) -> None:
        super().__init__(id)
        if len(last_name) > 25:
            raise Exception(f'Значение {last_name} слишком большое.'
                            'Введите меньше 25 символов')
        if len(first_name) > 25:
            raise Exception(f'Значение {first_name} слишком большое.'
                            'Введите меньше 25 символов')

        if middle_name is not None and len(middle_name) > 25:
            raise Exception(f'Значение {middle_name} слишком большое.'
                            'Введите меньше 25 символов')
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

        try:
            if int(age) < 18 or int(age) > 99:
                raise Exception('Значение возраста должно быть от 18 до 99')

            self.age = int(age)
        except Exception:
            raise Exception(f'Значение возраста {age} некорректное')

        try:
            if int(passport_number) < 0:
                raise Exception('Значение номера паспорта должно быть'
                                ' положительным')

            self.passport_number = int(passport_number)
        except Exception:
            raise Exception(f'Значение номера паспорта {passport_number}'
                            ' некорректное')

        if isinstance(passport_issue_date, str):
            try:
                self.passport_issue_date = date.fromisoformat(
                    passport_issue_date)
            except Exception:
                raise Exception('Введен неверный формат даты выдачи паспорта: '
                                f'{passport_issue_date}')
        else:
            self.passport_issue_date = passport_issue_date

        try:
            self.city_id = int(city_id)
        except Exception:
            raise Exception('Введен неверный для ID Город: '
                            f'{city_id}')
        try:
            self.street_id = int(street_id)
        except Exception:
            raise Exception('Введен неверный для ID Улица: '
                            f'{street_id}')
        if len(house_number) > 5:
            raise Exception(f'Значение {house_number} слишком большое.'
                            'Введите меньше 5 символов')
        self.house_number = house_number

        if self.is_valid_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            raise Exception('Номер телефона имеет некорректный формат')

        if len(photo) > 200:
            raise Exception(f'Значение {photo} слишком '
                            'большое. Введите меньше 200 символов')
        self.photo = photo
        try:
            self.education_level_id = int(education_level_id)
        except Exception:
            raise Exception('Введен неверный для ID Уровень образования: '
                            f'{education_level_id}')
        try:
            self.education_document_id = int(education_document_id)
        except Exception:
            raise Exception('Введен неверный для ID Документ об образовании: '
                            f'{education_document_id}')
        if len(education_document_details) > 100:
            raise Exception(f'Значение {education_document_details} слишком '
                            'большое. Введите меньше 100 символов')
        self.education_document_details = education_document_details

        if isinstance(registration_date, str):
            self.registration_date = datetime.strptime(registration_date,
                                                       '%Y-%m-%d').date()
        else:
            self.registration_date = registration_date

        if allowance_id is None:
            self.allowance_id = None
        else:
            self.allowance_id = int(allowance_id)


class SpecializationApplicant(BaseModel):
    '''Класс, описывающий специальности соискателей'''
    def __init__(
        self,
        id: int | None,
        applicant_id: int | str,
        specialization_id: int | str,
        work_experience: float | str
    ):
        super().__init__(id)

        try:
            self.applicant_id = int(applicant_id)
        except Exception:
            raise Exception('Введен неверный для ID Соискатель: '
                            f'{applicant_id}')

        try:
            self.specialization_id = int(specialization_id)
        except Exception:
            raise Exception('Введен неверный для ID Специализация: '
                            f'{specialization_id}')

        if isinstance(work_experience, str):
            try:
                if float(work_experience) < 0:
                    raise Exception('Опыт работы не может быть отрицательным')
                self.work_experience = float(work_experience)
            except Exception:
                raise Exception('Значение опыта работы: {work_experience}'
                                ' некорректное')
        else:
            self.work_experience = work_experience


class EducationalInstitutionApplicant(BaseModel):
    '''Класс, описывающий учебные заведения соискателей'''
    def __init__(
        self,
        id: int | None,
        applicant_id: int | str,
        educational_institution_id: int | str
    ):
        super().__init__(id)

        try:
            self.applicant_id = int(applicant_id)
        except Exception:
            raise Exception('Введен неверный для ID Соискатель: '
                            f'{applicant_id}')

        try:
            self.educational_institution_id = int(educational_institution_id)
        except Exception:
            raise Exception('Введен неверный для ID Учебное заведение: '
                            f'{educational_institution_id}')
