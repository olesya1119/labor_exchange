--Создание таблицы Специальность
CREATE TABLE specialization(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

--Создание таблицы Учебное заведение
CREATE TABLE educational_institution(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

--Создание таблицы Уровень образования
CREATE TABLE education_level(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

--Создание таблицы Документ об образовании
CREATE TABLE education_document(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

--Создание таблицы Пособие
CREATE TABLE allowance(
    id SERIAL PRIMARY KEY,
    amount REAL NOT NULL
);

--Создание таблицы Требования к работнику
CREATE TABLE applicant_requirements(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

--Создание таблицы Сфера Деятельности
CREATE TABLE field_of_activity(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

--Создание таблицы Улица 
CREATE TABLE street(
    id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL
);

--Создание таблицы Город 
CREATE TABLE city(
    id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL
);

--Создание таблицы Соискатель
CREATE TABLE applicant(
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(25) NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    middle_name VARCHAR(25),
    age INTEGER NOT NULL,
    passport_number INTEGER NOT NULL,
    passport_issue_date DATE NOT NULL,
    passport_issued_by VARCHAR(100) NOT NULL,
    city_id INTEGER NOT NULL,
    street_id INTEGER NOT NULL,
    house_number VARCHAR(5) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    photo VARCHAR(200) NOT NULL,
    education_level_id INTEGER,
    education_document_id INTEGER,
    education_document_details VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL,
    allowance_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES city (id),
    FOREIGN KEY (street_id) REFERENCES street (id),
    FOREIGN KEY (education_level_id) REFERENCES education_level (id),
    FOREIGN KEY (education_document_id) REFERENCES education_document (id),
    FOREIGN KEY (allowance_id) REFERENCES allowance (id)
);

--Создание таблицы Работодатель
CREATE TABLE employer(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    city_id INTEGER NOT NULL,
    street_id INTEGER NOT NULL,
    house_number VARCHAR(5) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    FOREIGN KEY (city_id) REFERENCES city (id),
    FOREIGN KEY (street_id) REFERENCES street (id)
);

--Создание таблицы Вакансия
CREATE TABLE vacancy(
    id SERIAL PRIMARY KEY,
    position_title VARCHAR(50) NOT NULL,
    lower_limit_of_salary INTEGER,
    upper_limit_of_salary INTEGER,
    employer_id INTEGER NOT NULL,
    FOREIGN KEY (employer_id) REFERENCES employer (id)
);


--Создание таблицы Архив
CREATE TABLE archive(
    id SERIAL PRIMARY KEY,
    applicant_id INTEGER NOT NULL,
    archive_date DATE NOT NULL,
    performed_by VARCHAR(100) NOT NULL,
    FOREIGN KEY (applicant_id) REFERENCES applicant (id)
);

--Создание таблицы Соглашение
CREATE TABLE agreement(
    id SERIAL PRIMARY KEY,
    applicant_id INTEGER NOT NULL,
    vacancy_id INTEGER NOT NULL,
    signature_date DATE NOT NULL,
    FOREIGN KEY (applicant_id) REFERENCES applicant (id),
    FOREIGN KEY (vacancy_id) REFERENCES vacancy (id)
);

--Создание таблицы Специальности соискателей
CREATE TABLE specialization_applicant(
    id SERIAL PRIMARY KEY,
    applicant_id INTEGER NOT NULL,
    specialization_id INTEGER NOT NULL,
    work_experience REAL NOT NULL,
    FOREIGN KEY (applicant_id) REFERENCES applicant (id),
    FOREIGN KEY (specialization_id) REFERENCES specialization (id)
);

--Создание таблицы Учебные заведения соискателей
CREATE TABLE educational_institution_applicant(
    id SERIAL PRIMARY KEY,
    applicant_id INTEGER NOT NULL,
    educational_institution_id INTEGER NOT NULL,
    FOREIGN KEY (applicant_id) REFERENCES applicant (id),
    FOREIGN KEY (educational_institution_id) REFERENCES educational_institution (id)
);

--Создание таблицы Требования вакансий
CREATE TABLE vacancy_applicant_requirements(
    id SERIAL PRIMARY KEY,
    vacancy_id INTEGER NOT NULL,
    applicant_requirements_id INTEGER NOT NULL,
    FOREIGN KEY (vacancy_id) REFERENCES vacancy (id),
    FOREIGN KEY (applicant_requirements_id) REFERENCES applicant_requirements (id)
);

--Создание таблицы Сферы деятельности вакансий
CREATE TABLE vacancy_field_of_activity(
    id SERIAL PRIMARY KEY,
    vacancy_id INTEGER NOT NULL,
    field_of_activity_id INTEGER NOT NULL,
    FOREIGN KEY (vacancy_id) REFERENCES vacancy (id),
    FOREIGN KEY (field_of_activity_id) REFERENCES field_of_activity (id)
);

CREATE TABLE menu(
    id SERIAL PRIMARY KEY,
    id_parent INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    function_name VARCHAR(50) NOT NULL,
    menu_order INTEGER NOT NULL
);

CREATE TABLE app_user(
    id SERIAL PRIMARY KEY,
    login VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE user_rights(
    id SERIAL PRIMARY KEY,
    id_app_user INTEGER NOT NULL,
    id_menu INTEGER NOT NULL,
    r BOOLEAN NOT NULL,
    w BOOLEAN NOT NULL,
    e BOOLEAN NOT NULL,
    d BOOLEAN NOT NULL,
    FOREIGN KEY (id_app_user) REFERENCES app_user(id),
    FOREIGN KEY (id_menu) REFERENCES menu(id)
);

