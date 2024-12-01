from .base_repository import BaseRepository
from app.models import Applicant, SpecializationApplicant
from app.models import EducationalInstitutionApplicant
from typing import Tuple


class ApplicantRepository(BaseRepository):
    table_name = "applicant"

    @BaseRepository.execute_query
    def add(self, applicant: Applicant) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name}
            (last_name, first_name, middle_name, age, passport_number,
            passport_issue_date, passport_issued_by, city_id, street_id,
            house_number, phone_number, photo, education_level_id,
            education_document_id, education_document_details,
            registration_date, allowance_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s)''',
            (
                applicant.last_name,
                applicant.first_name,
                applicant.middle_name,
                applicant.age,
                applicant.passport_number,
                applicant.passport_issue_date,
                applicant.passport_issued_by,
                applicant.city_id,
                applicant.street_id,
                applicant.house_number,
                applicant.phone_number,
                applicant.photo,
                applicant.education_level_id,
                applicant.education_document_id,
                applicant.education_document_details,
                applicant.registration_date,
                applicant.allowance_id,
            ),
        )


class SpecializationApplicantRepository(BaseRepository):
    table_name = "specialization_applicant"

    @BaseRepository.execute_query
    def add(self, specialization:
            SpecializationApplicant) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name}
            (applicant_id, specialization_id, work_experience)
            VALUES (%s, %s, %s)''',
            (
                specialization.applicant_id,
                specialization.specialization_id,
                specialization.work_experience,
            ),
        )


class EducationalInstitutionApplicantRepository(BaseRepository):
    table_name = "educational_institution_applicant"

    @BaseRepository.execute_query
    def add(self, educational_institution_applicant:
            EducationalInstitutionApplicant) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name}
            (applicant_id, educational_institution_id)
            VALUES (%s, %s)''',
            (
                educational_institution_applicant.applicant_id,
                educational_institution_applicant.educational_institution_id,
            )
        )
