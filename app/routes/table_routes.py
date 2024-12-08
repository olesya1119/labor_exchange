from app.services import BaseService, ApplicantService
from app.services import ArchiveService, VacancyService, EmployerService
from flask import Blueprint, render_template, request, jsonify
from .pages_controller import get_active_page, get_all_pages

'''
Файл описывает классы, которые отвечают за маршруты всех табличных страниц.
Их функционал полностью наследуется от TableRoutes.
Здесь нет маршрутов для 'Справочники'.
Здесь есть: Соискатели, Работадатели, Вакансии, Архив.

'''


class TableRoutes():
    '''
    Класс описывает маршруты и действия для всех страниц,
    которые выводят таблицы, имеют возможность удаления/добавления/поиска
    '''

    def __init__(self, service: BaseService, app_name: str, url_prefix: str,
                 template_folder: str) -> None:
        self.blueprint = Blueprint(app_name, __name__,
                                   url_prefix=url_prefix,
                                   template_folder=template_folder)
        self.service = service
        self.app_name = app_name
        self._register_routes()

    def _register_routes(self):
        @self.blueprint.route("/", methods=["GET"])
        def render_table():
            '''Рендер страницы с таблицой'''

            # Количество строк в таблице
            records_per_page = int(request.args.get('records_per_page', 10))
            # Номер страницы
            page = int(request.args.get('page', 1))
            # Обновляем класс - сервис
            self.service.set_limit(records_per_page)
            self.service.set_page(page)

            return render_template(
                f"{self.app_name}.html",
                active_page=get_active_page(f"{self.app_name}.render_table"),
                pages=get_all_pages(),
                data=self.service.get_table(),
                head=self.service.table_fields,
                records_per_page=records_per_page,
                current_page=page,
                total_pages=self.service.get_count_pages()
            )

        @self.blueprint.route("/delete/<int:id>", methods=["DELETE"])
        def delete_entry(id):
            '''Удаление записи из таблицы'''
            try:
                self.service.delete_entry(id)
                return jsonify({"success": True})
            except Exception as e:
                return jsonify({"success": False, "error": str(e)}), 500

        @self.blueprint.route("/save", methods=["POST"])
        def save_entry():
            '''Сохранение записи в таблице'''
            data = request.json
            try:
                self.service.update_table(data)
                return jsonify({"success": True})
            except Exception as e:
                return jsonify({"success": False, "errors": [str(e)]}), 500

    def get_blueprint(self):
        return self.blueprint


class ApplicantsRoutes(TableRoutes):
    def __init__(self):
        super().__init__(ApplicantService(), 'applicants', '/applicants',
                         'templates/applicants')


class VacanciesRoutes(TableRoutes):
    def __init__(self):
        super().__init__(VacancyService(), 'vacancies', '/vacancies',
                         'templates/vacancies')


class EmployersRoutes(TableRoutes):
    def __init__(self):
        super().__init__(EmployerService(), 'employers', '/employers',
                         'employers/vacancies')


class ArchiveRoutes(TableRoutes):
    def __init__(self):
        super().__init__(ArchiveService(), 'archive', '/archive',
                         'archive/vacancies')
