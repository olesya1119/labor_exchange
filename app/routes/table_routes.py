from app.services import BaseService, ApplicantService
from app.services import ArchiveService, VacancyService, EmployerService
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user  # type: ignore
from app.repositories import get_activ_page, get_menu_by_id

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
                                   url_prefix=url_prefix)
        self.service = service
        self.app_name = app_name
        self.template_folder = template_folder
        self._register_routes()

    def _register_routes(self):
        @self.blueprint.route("/", methods=["GET"])
        @login_required
        def render_table():
            pages = get_menu_by_id(current_user.get_id())
            '''Рендер страницы с таблицой'''
            view_mode = request.args.get('view_mode', 'readonly')
            # Количество строк в таблице
            try:
                records_per_page = int(request.args.get('records_per_page',
                                                        10))
            except ValueError:
                records_per_page = 10
            # Параметры сортировки
            sort_by = request.args.get('sort_by', default=0, type=int)
            sort_dir = request.args.get('sort_dir', default='True', type=str)

            search_query = request.args.get('search_query', '')
            # Номер страницы
            try:
                page = int(request.args.get('page', 1))
            except ValueError:
                page = 1
            # Обновляем класс - сервис
            self.service.set_limit(records_per_page)
            self.service.set_page(page)
            self.service.set_sort(sort_by, True if
                                  sort_dir == 'True' else False)
            self.service.set_filter(search_query)

            return render_template(
                f"{self.template_folder}/{self.app_name}.html",
                active_page=get_activ_page(pages,
                                           f"{self.app_name}.render_table"),
                pages=pages,
                data=self.service.get_table(view_mode),
                records_per_page=records_per_page,
                current_page=page,
                total_pages=self.service.get_count_pages(),
                search_query=search_query,  # Передаем текущий поисковый запрос
                sort_by=sort_by,            # Передаем текущую сортировку
                sort_dir=sort_dir,          # Передаем направление сортировки
                view_mode=view_mode
            )

        @self.blueprint.route("/delete/<int:id>", methods=["DELETE"])
        @login_required
        def delete_entry(id):
            '''Удаление записи из таблицы'''
            try:
                self.service.delete_entry(id)
                return jsonify({"success": True})
            except Exception as e:
                return jsonify({"success": False, "error": str(e)}), 500

        @self.blueprint.route("/save", methods=["POST"])
        @login_required
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
                         'applicants')


class VacanciesRoutes(TableRoutes):
    def __init__(self):
        super().__init__(VacancyService(), 'vacancies', '/vacancies',
                         'vacancies')


class EmployersRoutes(TableRoutes):
    def __init__(self):
        super().__init__(EmployerService(), 'employers', '/employers',
                         'employers')


class ArchiveRoutes(TableRoutes):
    def __init__(self):
        super().__init__(ArchiveService(), 'archive', '/archive',
                         'archive')


archive = ArchiveRoutes()
applicants = ApplicantsRoutes()
vacancies = VacanciesRoutes()
employers = EmployersRoutes()

table_blueprints = {
    'archive.render_table': archive.get_blueprint(),
    'applicants.render_table': applicants.get_blueprint(),
    'vacancies.render_table': vacancies.get_blueprint(),
    'employers.render_table': employers.get_blueprint()
}
