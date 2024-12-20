# models/__init__.py.
# flake8: noqa
from .agreement import AgreementRepository
from .applicant import ApplicantRepository, SpecializationApplicantRepository, EducationalInstitutionApplicantRepository
from .archive import ArchiveRepository
from .education import EducationalInstitutionRepository, EducationLevelRepository, EducationDocumentRepository
from .location import CityRepository, StreetRepository
from .specialization import SpecializationRepository, AllowanceRepository, ApplicantRequirementsRepository, FieldOfActivityRepository
from .vacancy import VacancyRepository, VacancyApplicantRequirementsRepository, VacancyFieldOfActivityRepository
from .employer import EmployerRepository
from .base_repository import BaseRepository
from .auth import get_user_by_id, add_user, get_user_id, update_password
from .pages_controller import get_menu_by_id, get_activ_page

#  TODO: много запросов неправильных. id не одноpначных, нет order by ..