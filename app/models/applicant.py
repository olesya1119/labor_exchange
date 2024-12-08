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

        self.applicant_id = int(applicant_id)
        self.specialization_id = int(specialization_id)

        if isinstance(work_experience, str):
            self.work_experience = float(work_experience)
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

        self.applicant_id = int(applicant_id)
        self.educational_institution_id = int(educational_institution_id)
