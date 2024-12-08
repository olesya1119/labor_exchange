from typing import Type
from app.repositories import BaseRepository
from app.models import BaseModel
from app.repositories import ApplicantRepository
from app.models import Applicant
from app.repositories import AgreementRepository
from app.models import Agreement
from app.repositories import SpecializationApplicantRepository
from app.models import SpecializationApplicant
from app.repositories import EducationalInstitutionApplicantRepository
from app.models import EducationalInstitutionApplicant
from app.repositories import ArchiveRepository
from app.models import Archive
from app.repositories import EducationalInstitutionRepository
from app.models import EducationalInstitution
from app.repositories import EducationLevelRepository
from app.models import EducationLevel
from app.repositories import EducationDocumentRepository
from app.models import EducationDocument
from app.repositories import EmployerRepository
from app.models import Employer
from app.repositories import CityRepository
from app.models import City
from app.repositories import StreetRepository
from app.models import Street
from app.repositories import SpecializationRepository
from app.models import Specialization
from app.repositories import AllowanceRepository
from app.models import Allowance
from app.repositories import ApplicantRequirementsRepository
from app.models import ApplicantRequirements
from app.repositories import FieldOfActivityRepository
from app.models import FieldOfActivity
from app.repositories import VacancyRepository
from app.models import Vacancy
from app.repositories import VacancyApplicantRequirementsRepository
from app.models import VacancyApplicantRequirements
from app.repositories import VacancyFieldOfActivityRepository
from app.models import VacancyFieldOfActivity
'''
Содержит описание всех классов - сервисов. Тк их функционал
ничем не отличается от базового, помимо используемой модели и репозитория,
то все они находтся здесь. В будущем, при увеличении функциональности,
сервисы можно переместить в отдельные классы
'''


class BaseService:

    table_fields: tuple = ('id', )
    __Model: Type[BaseModel] = BaseModel
    __repository: BaseRepository = BaseRepository()

    def __init__(self, limit=10, offset=0) -> None:
        self.limit = limit
        self.offset = offset

    def set_page(self, page: int) -> None:
        '''Установаить страницу'''
        if page > self.get_count_pages():
            self.offset = self.__repository.get_count() - self.limit
        else:
            self.offset = (self.limit * page) - 1

    def update_limit(self, limit: int) -> None:
        '''Обновить значение переменных limit и offset'''

        self.limit = limit
        self.offset = 0

    def update_table(self, data: dict) -> None:
        '''
        Обновить таблицу. В случае если id указан, то обновляем данные.
        Если нет - то добавляем новые.
        '''
        model = self.__Model(*data.values())
        if model.id is None:
            self.__repository.add(model)
        else:
            self.__repository.update(model.id, model.to_dict())

    def get_count_pages(self) -> int:
        '''Получить общее количество страниц'''
        count_entry = self.__repository.get_count()[0][0]
        count_page = count_entry // self.limit
        if count_entry % self.limit != 0:
            count_page += 1
        return count_page

    def get_page_number(self) -> int:
        '''Получить номер текущей страницы'''
        return self.offset // self.limit + 1

    def get_table(self) -> dict:
        '''Получить данные таблицы'''
        return self.__repository.get_paginated(self.limit, self.offset)


class ApplicantService:
    table_fields: tuple = ('id', 'Фамилия', 'Имя', 'Отчетсво', 'Возраст',
                           'Номер паспорта', 'Дата выдачи паспорта',
                           'Кем выдан паспорт',
                           'id-Город', 'id-Улица', 'Номер дома',
                           'Номер телефона', 'Фотография',
                           'id-Уровень образования',
                           'id-Документ об образовании',
                           'Данные документа об образовании',
                           'Дата потсановки на учет', 'id-Пособие')

    __Model = Applicant
    __repository = ApplicantRepository()


class AgreementService:
    table_fields: tuple = ('id',
                           'id-Соискатель',
                           'id-Вакансия',
                           'Дата подписания')

    __Model = Agreement
    __repository = AgreementRepository()


class SpecializationApplicantService:
    table_fields: tuple = ('id',
                           'id-Соискатель',
                           'id-Специальность',
                           'Стаж работы'
                           )

    __Model = SpecializationApplicant
    __repository = SpecializationApplicantRepository()


class EducationalInstitutionApplicantService:
    table_fields: tuple = ('id',
                           'id-Соискатель',
                           'id-Учебное заведение'
                           )

    __Model = EducationalInstitutionApplicant
    __repository = EducationalInstitutionApplicantRepository()


class ArchiveService:
    table_fields: tuple = ('id',
                           'id-Соискатель',
                           'Дата перевода в архив',
                           'Лицо, выполнившее операцию'
                           )

    __Model = Archive
    __repository = ArchiveRepository()


class EducationalInstitutionService:
    table_fields: tuple = ('id', 'Название')

    __Model = EducationalInstitution
    __repository = EducationalInstitutionRepository()


class EducationLevelService:
    table_fields: tuple = ('id', 'Название')

    __Model = EducationLevel
    __repository = EducationLevelRepository()


class EducationDocumentService:
    table_fields: tuple = ('id', 'Название')

    __Model = EducationDocument
    __repository = EducationDocumentRepository()


class EmployerService:
    table_fields: tuple = ('id', 'Название', 'id-Город',
                           'id-Улицы', 'Номер дома',
                           'Номер телефона')

    __Model = Employer
    __repository = EmployerRepository()


class CityService:
    table_fields: tuple = ('id', 'Название')

    __Model = City
    __repository = CityRepository()


class StreetService:
    table_fields: tuple = ('id', 'Название')

    __Model = Street
    __repository = StreetRepository()


class SpecializationService:
    table_fields: tuple = ('id', 'Название')

    __Model = Specialization
    __repository = SpecializationRepository()


class AllowanceService:
    table_fields: tuple = ('id', 'Размер пособия')

    __Model = Allowance
    __repository = AllowanceRepository()


class ApplicantRequirementsService:
    table_fields: tuple = ('id', 'Название')

    __Model = ApplicantRequirements
    __repository = ApplicantRequirementsRepository()


class FieldOfActivityService:
    table_fields: tuple = ('id', 'Название')

    __Model = FieldOfActivity
    __repository = FieldOfActivityRepository()


class VacancyService:
    table_fields: tuple = ('id',
                           'Название должности',
                           'Нижняя граница зарплаты',
                           'Верхняя граница зарплаты',
                           'id-Работодатель')

    __Model = Vacancy
    __repository = VacancyRepository()


class VacancyApplicantRequirementsService:
    table_fields: tuple = ('id', 'id-Вакансия', 'id-Требования к работнику')

    __Model = VacancyApplicantRequirements
    __repository = VacancyApplicantRequirementsRepository()


class VacancyFieldOfActivityService:
    table_fields: tuple = ('id', 'id-Вакансия', 'id-Сфера деятельности')

    __Model = VacancyFieldOfActivity
    __repository = VacancyFieldOfActivityRepository()
