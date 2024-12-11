from flask import Blueprint, render_template
from flask_login import current_user  # type: ignore
from .table_routes import TableRoutes
from app.services import SpecializationService, EducationLevelService
from app.services import EducationDocumentService, AllowanceService
from app.services import EducationalInstitutionService
from app.services import ApplicantRequirementsService
from app.services import FieldOfActivityService
from app.services import CityService, StreetService
from app.repositories import get_activ_page, get_menu_by_id


directories_blueprint = Blueprint('directories', __name__,
                                  url_prefix='/directories',)


@directories_blueprint.route("/")
def render_directories():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("directories/directories.html",
                           active_page=get_activ_page(
                               pages,
                               'directories.render_directories'),
                           pages=pages)


class SpecializationsRoutes(TableRoutes):
    def __init__(self):
        super().__init__(SpecializationService(), 'specializations',
                         '/directories/specializations',
                         'directories')


class EducationLevelRoutes(TableRoutes):
    def __init__(self):
        super().__init__(EducationLevelService(), 'education_levels',
                         '/directories/education_levels',
                         'directories')


class EducationalInstitutionRoutes(TableRoutes):
    def __init__(self):
        super().__init__(EducationalInstitutionService(),
                         'educational_institutions',
                         '/directories/educational_institutions',
                         'directories')


class EducationDocumentRoutes(TableRoutes):
    def __init__(self):
        super().__init__(EducationDocumentService(), 'education_documents',
                         '/directories/education_documents',
                         'directories')


class AllowanceRoutes(TableRoutes):
    def __init__(self):
        super().__init__(AllowanceService(), 'allowances',
                         '/directories/allowances',
                         'directories')


class ApplicantRequirementsRoutes(TableRoutes):
    def __init__(self):
        super().__init__(ApplicantRequirementsService(),
                         'applicant_requirements',
                         '/directories/applicant_requirements',
                         'directories')


class FieldOfActivityRoutes(TableRoutes):
    def __init__(self):
        super().__init__(FieldOfActivityService(), 'fields_of_activity',
                         '/directories/fields_of_activity',
                         'directories')


class CityRoutes(TableRoutes):
    def __init__(self):
        super().__init__(CityService(), 'cities',
                         '/directories/cities',
                         'directories')


class StreetRoutes(TableRoutes):
    def __init__(self):
        super().__init__(StreetService(), 'streets',
                         '/directories/streets',
                         'directories')


specializations_routes = SpecializationsRoutes()
education_level_routes = EducationLevelRoutes()
educational_institution_routes = EducationalInstitutionRoutes()
education_document_routes = EducationDocumentRoutes()
allowance_routes = AllowanceRoutes()
applicant_requirements_routes = ApplicantRequirementsRoutes()
field_of_activity_routes = FieldOfActivityRoutes()
city_routes = CityRoutes()
street_routes = StreetRoutes()

directories_blueprints = {
    'directories_blueprint.render_table': directories_blueprint,
    'specializations.render_table': specializations_routes.get_blueprint(),
    'education_level.render_table': education_level_routes.get_blueprint(),
    'educational_institution.render_table':
        educational_institution_routes.get_blueprint(),
    'education_document.render_table':
        education_document_routes.get_blueprint(),
    'allowance.render_table': allowance_routes.get_blueprint(),
    'applicant.render_table': applicant_requirements_routes.get_blueprint(),
    'field.render_table': field_of_activity_routes.get_blueprint(),
    'city.render_table': city_routes.get_blueprint(),
    'street.render_table': street_routes.get_blueprint()
}
