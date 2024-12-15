from flask import Blueprint, render_template
from flask_login import current_user  # type: ignore
from .table_routes import TableRoutes
from app.services import SpecializationApplicantService
from app.services import EducationalInstitutionApplicantService
from app.services import VacancyApplicantRequirementsService
from app.services import VacancyFieldOfActivityService
from app.services import AgreementService
from app.repositories import get_activ_page, get_menu_by_id


intermediate_tables_blueprint = Blueprint('intermediate_tables', __name__,
                                          url_prefix='/intermediate_tables',)


@intermediate_tables_blueprint.route("/")
def render_intermediate_tables():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("intermediate_tables/intermediate_tables.html",
                           active_page=get_activ_page(
                            pages,
                            'intermediate_tables.render_intermediate_tables'),
                           pages=pages)


class SpecializationApplicantRoutes(TableRoutes):
    def __init__(self):
        super().__init__(SpecializationApplicantService(),
                         'specialization_applicant',
                         '/intermediate_tables/specialization_applicant',
                         'intermediate_tables')


class EducationalInstitutionApplicantRoutes(TableRoutes):
    def __init__(self):
        super().__init__(EducationalInstitutionApplicantService(),
                         'educational_institution_applicant',
                         '/intermediate_tables/'
                         'educational_institution_applicant',
                         'intermediate_tables')


class VacancyApplicantRequirementsRoutes(TableRoutes):
    def __init__(self):
        super().__init__(VacancyApplicantRequirementsService(),
                         'vacancy_applicant_requirements',
                         '/intermediate_tables/vacancy_applicant_requirements',
                         'intermediate_tables')


class VacancyFieldOfActivityRoutes(TableRoutes):
    def __init__(self):
        super().__init__(VacancyFieldOfActivityService(),
                         'vacancy_field_of_activity',
                         '/intermediate_tables/vacancy_field_of_activity',
                         'intermediate_tables')


class AgreementRoutes(TableRoutes):
    def __init__(self):
        super().__init__(AgreementService(),
                         'agreement',
                         '/intermediate_tables/agreement',
                         'intermediate_tables')


specialization_applicant_routes = SpecializationApplicantRoutes()
educational_institution_applicant_routes = \
    EducationalInstitutionApplicantRoutes()
vacancy_applicant_requirements_routes = VacancyApplicantRequirementsRoutes()
vacancy_field_of_activity_routes = VacancyFieldOfActivityRoutes()
agreement_routes = AgreementRoutes()

intermediate_tables_blueprints = {
    'intermediate_tables.render_intermediate_tables':
    intermediate_tables_blueprint,
    'specialization_applicant.render_table':
    specialization_applicant_routes.get_blueprint(),
    'educational_institution_applicant.render_table':
    educational_institution_applicant_routes.get_blueprint(),
    'vacancy_applicant_requirements.render_table':
        vacancy_applicant_requirements_routes.get_blueprint(),
    'vacancy_field_of_activity.render_table':
    vacancy_field_of_activity_routes.get_blueprint(),
    'agreement.render_table': agreement_routes.get_blueprint(),

}
