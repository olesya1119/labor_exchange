from .base_model import BaseModel
from datetime import date


class Applicant(BaseModel):
    '''Класс, описывающий безработного(соискателя)'''

    def __init__(self, id: int, last_name: str, first_name: str,
                 middle_name: str | None, age: int, passport_number: int,
                 passport_issue_date: date,  passport_issued_by: str,
                 city_id: int, street_id: int, house_number: str,
                 phone_number: str, photo: str,
                 education_level_id: int,
                 education_document_id: int,
                 education_document_details: str, registration_date: date,
                 allowance_id: int | None) -> None:
        super().__init__(id)
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age
        self.passport_number = passport_number
        self.passport_issue_date = passport_issue_date
        self.passport_issued_by = passport_issued_by
        self.city_id = city_id
        self.street_id = street_id
        self.house_number = house_number
        self.phone_number = phone_number
        self.photo = photo
        self.education_level_id = education_level_id
        self.education_document_id = education_document_id
        self.education_document_details = education_document_details
        self.registration_date = registration_date
        self.allowance_id = allowance_id


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
