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
            (id, last_name, first_name, middle_name, age, passport_number,
            passport_issue_date, passport_issued_by, city_id, street_id,
            house_number, phone_number, photo, education_level_id,
            education_document_id, education_document_details,
            registration_date, allowance_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
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

    @BaseRepository.execute_query
    def update(self, applicant: Applicant) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            last_name = %s,
            first_name = %s,
            middle_name = %s,
            age = %s,
            passport_number = %s,
            passport_issue_date = %s,
            passport_issued_by = %s,
            city_id = %s,
            street_id = %s,
            house_number = %s,
            phone_number = %s,
            photo = %s,
            education_level_id = %s,
            education_document_id = %s,
            education_document_details = %s,
            registration_date = %s,
            allowance_id = %s
            WHERE id = %s''',
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
                applicant.id,
            ),
        )


class SpecializationApplicantRepository(BaseRepository):
    table_name = "specialization_applicant"

    @BaseRepository.execute_query
    def add(self, specialization_applicant:
            SpecializationApplicant) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name}
            (id, applicant_id, specialization_id, work_experience)
            VALUES (%s, %s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                specialization_applicant.applicant_id,
                specialization_applicant.specialization_id,
                specialization_applicant.work_experience,
            ),
        )

    def update(self, specialization: SpecializationApplicant
               ) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            applicant_id = %s,
            specialization_id = %s,
            work_experience = %s
            WHERE id = %s''',
            (
                specialization.applicant_id,
                specialization.specialization_id,
                specialization.work_experience,
                specialization.id,
            ),
        )


class EducationalInstitutionApplicantRepository(BaseRepository):
    table_name = "educational_institution_applicant"

    @BaseRepository.execute_query
    def add(self, educational_institution_applicant:
            EducationalInstitutionApplicant) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name}
            (id, applicant_id, educational_institution_id)
            VALUES (%s, %s, %s)''',
            (
                self.get_last_id()[0][0] + 1,
                educational_institution_applicant.applicant_id,
                educational_institution_applicant.educational_institution_id,
            )
        )

    @BaseRepository.execute_query
    def update(self, educational_institution_applicant:
               EducationalInstitutionApplicant) -> Tuple[str, tuple]:
        return (
            f'''UPDATE {self.table_name} SET
            applicant_id = %s,
            educational_institution_id = %s
            WHERE id = %s''',
            (
                educational_institution_applicant.applicant_id,
                educational_institution_applicant.educational_institution_id,
                educational_institution_applicant.id,
            ),
        )
