from .base_model import BaseModel
from datetime import date, datetime


class Applicant(BaseModel):
    '''Класс, описывающий безработного(соискателя)'''

    def __init__(self, id: int | str, last_name: str | str, first_name: str,
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
        super().__init__(int(id))
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = int(age)
        self.passport_number = int(passport_number)

        if isinstance(passport_issue_date, str):
            self.passport_issue_date = datetime.strptime(passport_issue_date,
                                                         '%Y-%m-%d').date()
        else:
            self.passport_issue_date = passport_issue_date

        self.passport_issued_by = passport_issued_by
        self.city_id = city_id
        self.street_id = street_id
        self.house_number = house_number
        self.phone_number = phone_number
        self.photo = photo
        self.education_level_id = int(education_level_id)
        self.education_document_id = int(education_document_id)
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

    def get_values(self) -> dict:
        return {
            'id': self.id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'age': self.age,
            'passport_number': self.passport_number,
            'passport_issue_date': self.passport_issue_date,
            'passport_issued_by': self.passport_issued_by,
            'city_id': self.city_id,
            'street_id': self.street_id,
            'house_number': self.house_number,
            'phone_number': self.phone_number,
            'photo': self.photo,
            'education_level_id': self.education_level_id,
            'education_document_id': self.education_document_id,
            'education_document_details': self.education_document_details
            }


class SpecializationApplicant(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int, applicant_id: int,
                 specialization_id: int, work_experience: float
                 ) -> None:
        super().__init__(id)
        self.applicant_id = applicant_id
        self.specialization_id = specialization_id
        self.work_experience = work_experience


class EducationalInstitutionApplicant(BaseModel):
    '''Класс, описывающий учебные заведения соискателей'''

    def __init__(self, id: int, applicant_id: int,
                 educational_institution_id: int
                 ) -> None:
        super().__init__(id)
        self.applicant_id = applicant_id
        self.educational_institution_id = educational_institution_id
