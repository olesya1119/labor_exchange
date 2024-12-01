from .base_model import BaseModel
from .location import Street, City
from .education import EducationLevel, EducationDocument
from .education import EducationalInstitution
from .specialization import Allowance, Specialization
from datetime import date


class Applicant(BaseModel):
    '''Класс, описывающий безработного(соискателя)'''

    def __init__(self, id: int, last_name: str, first_name: str,
                 middle_name: str | None, age: int, passport_number: int,
                 passport_issue_date: date,  passport_issued_by: str,
                 city: City, street: Street, house_number: str,
                 phone_number: str, photo: str,
                 education_level: EducationLevel,
                 education_document: EducationDocument,
                 education_document_details: str, registration_date: date,
                 allowance: Allowance | None) -> None:
        super().__init__(id)
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age
        self.passport_number = passport_number
        self.passport_issue_date = passport_issue_date
        self.passport_issued_by = passport_issued_by
        self.city = city
        self.street = street
        self.house_number = house_number
        self.phone_number = phone_number
        self.photo = photo
        self.education_level = education_level
        self.education_document = education_document
        self.education_document_details = education_document_details
        self.registration_date = registration_date
        self.allowance = allowance


class SpecializationApplicant(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int, applicant: Applicant,
                 specialization: Specialization, work_experience: float
                 ) -> None:
        super().__init__(id)
        self.applicant = applicant
        self.specialization = specialization
        self.work_experience = work_experience


class EducationalInstitutionApplicant(BaseModel):
    '''Класс, описывающий учебные заведения соискателей'''

    def __init__(self, id: int, applicant: Applicant,
                 educational_institution: EducationalInstitution
                 ) -> None:
        super().__init__(id)
        self.applicant = applicant
        self.educational_institution = educational_institution
