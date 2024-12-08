from app.repositories import ApplicantRepository, BaseRepository
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

    def __init__(self, repository: BaseRepository, Model, limit=10, offset=0
                 ) -> None:
        self.limit = limit
        self.offset = offset
        self.__repository = repository
        self.__Model = Model

    def set_page(self, page: int) -> None:
        '''Установаить страницу'''
        if page >= self.get_count_pages():
            self.offset = self.__repository.get_count()[0][0] - self.limit
        else:
            self.offset = self.limit * (page - 1)
        if self.offset < 0:
            self.offset = 0

    def set_limit(self, limit: int) -> None:
        '''Обновить значение переменной limit'''
        self.limit = limit

    def reset_offset(self) -> None:
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
            self.__repository.update(model)

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

    def delete_entry(self, id: int):
        '''Получить данные из таблицы'''
        self.__repository.delete_by_id(id)


class ApplicantService(BaseService):
    table_fields: tuple = ('id', 'Фамилия', 'Имя', 'Отчетсво', 'Возраст',
                           'Номер паспорта', 'Дата выдачи паспорта',
                           'Кем выдан паспорт',
                           'id-Город', 'id-Улица', 'Номер дома',
                           'Номер телефона', 'Фотография',
                           'id-Уровень образования',
                           'id-Документ об образовании',
                           'Данные документа об образовании',
                           'Дата потсановки на учет', 'id-Пособие')

    def __init__(self, limit=10, offset=0):
        super().__init__(ApplicantRepository(), Applicant, limit, offset)


class AgreementService(BaseService):
    table_fields: tuple = ('id',
                           'id-Соискатель',
                           'id-Вакансия',
                           'Дата подписания')

    def __init__(self, limit=10, offset=0):
        super().__init__(AgreementRepository(), Agreement, limit, offset, )


class SpecializationApplicantService(BaseService):
    table_fields: tuple = ('id',
                           'id-Соискатель',
                           'id-Специальность',
                           'Стаж работы'
                           )

    def __init__(self, limit=10, offset=0):
        super().__init__(SpecializationApplicantRepository(),
                         SpecializationApplicant, limit, offset)


class EducationalInstitutionApplicantService(BaseService):
    table_fields: tuple = ('id',
                           'id-Соискатель',
                           'id-Учебное заведение'
                           )

    def __init__(self, limit=10, offset=0):
        super().__init__(EducationalInstitutionApplicantRepository(),
                         EducationalInstitutionApplicant, limit, offset)


class ArchiveService(BaseService):
    table_fields: tuple = ('id',
                           'id-Соискатель',
                           'Дата перевода в архив',
                           'Лицо, выполнившее операцию'
                           )

    def __init__(self, limit=10, offset=0):
        super().__init__(ArchiveRepository(), Archive, limit, offset)


class EducationalInstitutionService(BaseService):
    table_fields: tuple = ('id', 'Название')

    def __init__(self, limit=10, offset=0):
        super().__init__(EducationalInstitutionRepository(),
                         EducationalInstitution, limit, offset)


class EducationLevelService(BaseService):
    table_fields: tuple = ('id', 'Название')

    def __init__(self, limit=10, offset=0):
        super().__init__(EducationLevelRepository(), EducationLevel,
                         limit, offset)


class EducationDocumentService(BaseService):
    table_fields: tuple = ('id', 'Название')

    def __init__(self, limit=10, offset=0):
        super().__init__(EducationDocumentRepository(), EducationDocument,
                         limit, offset)


class EmployerService(BaseService):
    table_fields: tuple = ('id', 'Название', 'id-Город',
                           'id-Улицы', 'Номер дома',
                           'Номер телефона')

    def __init__(self, limit=10, offset=0):
        super().__init__(EmployerRepository(), Employer, limit, offset)


class CityService(BaseService):
    table_fields: tuple = ('id', 'Название')

    def __init__(self, limit=10, offset=0):
        super().__init__(CityRepository(), City, limit, offset)


class StreetService(BaseService):
    table_fields: tuple = ('id', 'Название')

    def __init__(self, limit=10, offset=0):
        super().__init__(StreetRepository(), Street, limit, offset)


class SpecializationService(BaseService):
    table_fields: tuple = ('id', 'Название')

    def __init__(self, limit=10, offset=0):
        super().__init__(SpecializationRepository(), Specialization,
                         limit, offset)


class AllowanceService(BaseService):
    table_fields: tuple = ('id', 'Размер пособия')

    def __init__(self, limit=10, offset=0):
        super().__init__(AllowanceRepository(), Allowance, limit, offset)


class ApplicantRequirementsService(BaseService):
    table_fields: tuple = ('id', 'Название')

    def __init__(self, limit=10, offset=0):
        super().__init__(ApplicantRequirementsRepository(),
                         ApplicantRequirements, limit, offset)


class FieldOfActivityService(BaseService):
    table_fields: tuple = ('id', 'Название')

    def __init__(self, limit=10, offset=0):
        super().__init__(FieldOfActivityRepository(), FieldOfActivity,
                         limit, offset)


class VacancyService(BaseService):
    table_fields: tuple = ('id',
                           'Название должности',
                           'Нижняя граница зарплаты',
                           'Верхняя граница зарплаты',
                           'id-Работодатель')

    def __init__(self, limit=10, offset=0):
        super().__init__(VacancyRepository(), Vacancy, limit, offset)


class VacancyApplicantRequirementsService(BaseService):
    table_fields: tuple = ('id', 'id-Вакансия', 'id-Требования к работнику')

    def __init__(self, limit=10, offset=0):
        super().__init__(VacancyApplicantRequirementsRepository(),
                         VacancyApplicantRequirements, limit, offset)


class VacancyFieldOfActivityService(BaseService):
    table_fields: tuple = ('id', 'id-Вакансия', 'id-Сфера деятельности')

    def __init__(self, limit=10, offset=0):
        super().__init__(VacancyFieldOfActivityRepository(),
                         VacancyFieldOfActivity, limit, offset)
