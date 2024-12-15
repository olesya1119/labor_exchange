INSERT INTO public.menu(
	id, id_parent, name, function_name, menu_order)
	VALUES 
	(1, 0, 'Главная страница', 'home.render_home', 1),
	(2, 0, 'Соискатели', 'applicants.render_table', 2),
	(3, 0, 'Работодатели', 'employers.render_table', 3),
	(4, 0, 'Вакансии', 'vacancies.render_table', 4),
	(5, 0, 'Архив', 'archive.render_table', 5),
	(6, 0, 'Справочники', 'directories.render_directories', 6),
	(7, 0, 'Документы', 'documents.render_documents', 8),
	(8, 0, 'Справка', 'help.render_help', 9),
	(9, 0, 'Разное', 'various.render_various', 10),
	(10, 0, 'Промежуточные таблицы', 'intermediate_tables.render_intermediate_tables', 7),
	(11, 6, 'Специальности', 'specializations.render_table', 1),
	(12, 6, 'Учебные заведения', 'educational_institutions.render_table', 2),
	(13, 6, 'Уровни образования', 'education_levels.render_table', 3),
	(14, 6, 'Документы об образовании', 'education_documents.render_table', 4),
	(15, 6, 'Пособия', 'allowances.render_table', 5),
	(16, 6, 'Требования к работнику', 'applicant_requirements.render_table', 6),
	(17, 6, 'Сферы деятельности', 'fields_of_activity.render_table', 7),
	(18, 6, 'Города', 'cities.render_table', 8),
	(19, 6, 'Улицы', 'streets.render_table', 9),
	(20, 10, 'Специальности соискателей', 'specialization_applicant.render_table', 1),
	(21, 10, 'Учебные заведения соискателей', 'educational_institution_applicant.render_table', 2),
	(22, 10, 'Требования вакансий', 'vacancy_applicant_requirements.render_table', 3),
	(23, 10, 'Сферы деятельности вакансий', 'vacancy_field_of_activity.render_table', 4),
	(24, 10, 'Соглашения', 'agreement.render_table', 5),
	(25, 9, 'Сменить пароль', 'various.change_password', 1),
	(26, 8, 'Содержание', 'help.content', 1),
	(27, 8, 'О программе', 'help.about_program', 2);


	



	

