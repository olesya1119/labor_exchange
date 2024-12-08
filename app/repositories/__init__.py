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
