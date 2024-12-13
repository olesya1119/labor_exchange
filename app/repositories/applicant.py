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

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: str = 'id',
               order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID", last_name AS Фамилия, first_name AS Имя,
            middle_name AS Отчество, age AS Возраст,
            passport_number AS "Номер паспорта",
            passport_issue_date AS "Дата выдачи паспорта",
            passport_issued_by AS "Кем выдан паспорт",
            city_id AS "ID Город", street_id AS "ID Улица",
            house_number AS "Номер дома", phone_number AS "Номер телефона",
            photo AS "Фотография",
            education_level_id AS "ID Уровень образования",
            education_document_id AS "ID Документ об образовании",
            education_document_details AS "Данные документа об образовании",
            registration_date AS "Дата постановки на учет",
            allowance_id AS "ID Пособие"
            FROM {self.table_name}
            ORDER BY {order_by} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s
            ''',
            (
                limit,
                offset,
            ),
        )

    @BaseRepository.fetch_results_with_head
    def select_with_join(self, limit: int, offset: int,
                         order_by: str = 'applicant.id', order_acs: bool = True
                         ) -> Tuple[str, tuple]:
        return (
            f'''SELECT applicant.id AS "ID", last_name AS Фамилия,
            first_name AS Имя,
            middle_name AS Отчество, age AS Возраст,
            passport_number AS "Номер паспорта",
            passport_issue_date AS "Дата выдачи паспорта",
            passport_issued_by AS "Кем выдан паспорт",
            'г. ' || city.name || ', ул. ' || street.name || ', д. '
            || house_number AS Адрес,
            phone_number AS "Номер телефона",
            photo AS "Фотография",
            education_level.name AS "Уровень образования",
            education_document.name AS "Документ об образовании",
            education_document_details AS "Данные документа об образовании",
            registration_date AS "Дата постановки на учет",
            allowance.amount AS "Размер пособия"
            FROM {self.table_name}
            LEFT JOIN city ON city.id = city_id
            LEFT JOIN street ON street.id = street_id
            LEFT JOIN education_level ON education_level.id =
            education_level_id
            LEFT JOIN education_document ON education_document.id =
            education_document_id
            LEFT JOIN allowance ON allowance.id = allowance_id
            ORDER BY {order_by} {'ASC' if order_acs else 'DESC'}
            LIMIT %s OFFSET %s
            ''',
            (
                limit,
                offset,
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

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: str = 'id',
               order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID",
            applicant_id AS "ID Соискатель",
            specialization_id AS "ID Специальность",
            work_experience AS "Стаж работы"
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))

    @BaseRepository.fetch_results_with_head
    def select_with_join(self, limit: int, offset: int, order_by: str = 'id',
                         order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID"
            applicant.last_name | ' ' | applicant.first_name |
            ' ' | applicant.middle_name AS "Соискатель",
            specialization.name AS "Специальность",
            work_experience AS "Стаж работы"
            JOIN applicant ON applicant.id = applicant_id
            JOIN specialization ON specialization.id = specialization_id
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))


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

    @BaseRepository.fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: str = 'id',
               order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID",
            applicant_id AS "ID Соискатель",
            educational_institution_id AS "ID Учебное заведение"
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))

    @BaseRepository.fetch_results_with_head
    def select_with_join(self, limit: int, offset: int, order_by: str = 'id',
                         order_acs: bool = True) -> Tuple[str, tuple]:
        return (
            f'''SELECT id AS "ID"
            applicant.last_name | ' ' | applicant.first_name |
            ' ' | applicant.middle_name AS "Соискатель",
            educational_institution.name AS "Учебное заведение"
            JOIN applicant ON applicant.id = applicant_id
            JOIN educational_institution ON educational_institution.id =
            educational_institution_id
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset))
