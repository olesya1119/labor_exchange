INSERT INTO public.menu(
	id, id_parent, name, function_name, menu_order)
	VALUES 
	(1, 0, 'Главная страница', 'home.render_home', 1),
	(2, 0, 'Соискатели', 'applicants.render_table', 2),
	(3, 0, 'Работодатели', 'employers.render_table', 3),
	(4, 0, 'Вакансии', 'vacancies.render_table', 4),
	(5, 0, 'Архив', 'archive.render_table', 5),
	(6, 0, 'Справочники', 'directories.render_directories', 6),
	(7, 0, 'Документы', 'home.documents', 7),
	(8, 0, 'Справка', 'home.help', 8),
	(9, 0, 'Разное', 'home.various', 9),
	(10, 6, 'Специальности', 'specializations.render_table', 1),
	(11, 6, 'Учебные заведения', 'educational_institutions.render_table', 2),
	(12, 6, 'Уровни образования', 'education_levels.render_table', 3),
	(13, 6, 'Документы об образовании', 'education_documents.render_table', 4),
	(14, 6, 'Пособия', 'allowances.render_table', 5),
	(15, 6, 'Требования к работнику', 'applicant_requirements.render_table', 6),
	(16, 6, 'Сферы деятельности', 'fields_of_activity.render_table', 7),
	(17, 6, 'Города', 'cities.render_table', 8),
	(18, 6, 'Улицы', 'streets.render_table', 9);

