# models/__init__.py.
# flake8: noqa
from .agreement import Agreement
from .applicant import Applicant, SpecializationApplicant, EducationalInstitutionApplicant
from .archive import Archive
from .base_model import BaseModel
from .education import EducationalInstitution, EducationLevel, EducationDocument
from .location import City, Street
from .specialization import Specialization, Allowance, ApplicantRequirements, FieldOfActivity
from .vacancy import Vacancy, VacancyApplicantRequirements, VacancyFieldOfActivity
from .employer import Employer
