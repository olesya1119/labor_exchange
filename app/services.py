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

    def __init__(self, repository: BaseRepository, Model, limit=10, offset=0
                 ) -> None:
        self.limit = limit
        self.offset = offset
        self.order_by = 0
        self.acs = True
        self.filter = ''
        self.__repository = repository
        self.__Model = Model

    def set_page(self, page: int) -> None:
        '''Установаить страницу'''
        if page > self.get_count_pages():
            self.offset = self.limit
        else:
            self.offset = self.limit * (page - 1)
        if self.offset < 0:
            self.offset = 0

    def set_limit(self, limit: int) -> None:
        '''Обновить значение переменной limit'''
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
            self.__repository.update(model)

    def get_count_pages(self) -> int:
        '''Получить общее количество страниц'''
        count_entry = len(self.__repository.select(None, 0, self.order_by,
                                                   self.acs, self.filter)) - 1
        count_page = count_entry // self.limit
        if count_entry % self.limit != 0:
            count_page += 1
        return count_page

    def get_page_number(self) -> int:
        '''Получить номер текущей страницы'''
        return self.offset // self.limit + 1

    def get_table(self, view_mode: str = 'readonly') -> dict:
        '''Получить данные таблицы'''
        if view_mode == 'editable':
            return self.__repository.select(self.limit, self.offset,
                                            self.order_by, self.acs,
                                            self.filter)
        else:
            return self.__repository.select_with_join(self.limit, self.offset,
                                                      self.order_by, self.acs,
                                                      self.filter)

    def set_sort(self, order_by: int, acs: bool) -> None:
        self.order_by = order_by
        self.acs = acs

    def set_filter(self, filter: str) -> None:
        self.filter = filter

    def delete_entry(self, id: int):
        '''Получить данные из таблицы'''
        self.__repository.delete_by_id(id)


class ApplicantService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(ApplicantRepository(), Applicant, limit, offset)


class AgreementService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(AgreementRepository(), Agreement, limit, offset, )


class SpecializationApplicantService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(SpecializationApplicantRepository(),
                         SpecializationApplicant, limit, offset)


class EducationalInstitutionApplicantService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(EducationalInstitutionApplicantRepository(),
                         EducationalInstitutionApplicant, limit, offset)


class ArchiveService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(ArchiveRepository(), Archive, limit, offset)


class EducationalInstitutionService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(EducationalInstitutionRepository(),
                         EducationalInstitution, limit, offset)


class EducationLevelService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(EducationLevelRepository(), EducationLevel,
                         limit, offset)


class EducationDocumentService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(EducationDocumentRepository(), EducationDocument,
                         limit, offset)


class EmployerService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(EmployerRepository(), Employer, limit, offset)


class CityService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(CityRepository(), City, limit, offset)


class StreetService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(StreetRepository(), Street, limit, offset)


class SpecializationService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(SpecializationRepository(), Specialization,
                         limit, offset)


class AllowanceService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(AllowanceRepository(), Allowance, limit, offset)


class ApplicantRequirementsService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(ApplicantRequirementsRepository(),
                         ApplicantRequirements, limit, offset)


class FieldOfActivityService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(FieldOfActivityRepository(), FieldOfActivity,
                         limit, offset)


class VacancyService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(VacancyRepository(), Vacancy, limit, offset)


class VacancyApplicantRequirementsService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(VacancyApplicantRequirementsRepository(),
                         VacancyApplicantRequirements, limit, offset)


class VacancyFieldOfActivityService(BaseService):

    def __init__(self, limit=10, offset=0):
        super().__init__(VacancyFieldOfActivityRepository(),
                         VacancyFieldOfActivity, limit, offset)
