from .base_model import BaseModel


class Vacancy(BaseModel):
    '''Класс, описывающий вакансию'''

    def __init__(
        self,
        id: int | None,
        position_title: str,
        lower_limit_of_salary: int | str | None,
        upper_limit_of_salary: int | str | None,
        employer_id: int | str
    ) -> None:
        super().__init__(id)
        if len(position_title) > 50:
            raise Exception(f'Значение {position_title} слишком большое.'
                            'Введите меньше 50 символов')
        self.position_title = position_title

        if lower_limit_of_salary is not None:
            try:
                if float(lower_limit_of_salary) < 0:
                    raise Exception('Значение зп не может быть отрицательным')

                self.lower_limit_of_salary = int(lower_limit_of_salary)
            except Exception:
                raise Exception(f'Значение зп {lower_limit_of_salary}'
                                ' некорректное')
        else:
            self.lower_limit_of_salary = lower_limit_of_salary

        if upper_limit_of_salary is not None:
            try:
                if float(upper_limit_of_salary) < 0:
                    raise Exception('Значение зп не может быть отрицательным')

                self.upper_limit_of_salary = int(upper_limit_of_salary)
            except Exception:
                raise Exception(f'Значение зп {upper_limit_of_salary}'
                                ' некорректное')
        else:
            self.upper_limit_of_salary = upper_limit_of_salary

        if (self.upper_limit_of_salary is not None and
            self.lower_limit_of_salary is not None and
                self.upper_limit_of_salary < self.lower_limit_of_salary):
            raise Exception('Нижняя граница зп не может больше верхней')
        self.employer_id = int(employer_id)


class VacancyApplicantRequirements(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int | str | None, vacancy_id: int | str,
                 applicant_requirements_id: int | str
                 ) -> None:
        super().__init__(id)
        try:
            self.vacancy_id = int(vacancy_id)
        except Exception:
            raise Exception('Введен неверный для ID Вакансия: '
                            f'{vacancy_id}')

        try:
            self.applicant_requirements_id = int(applicant_requirements_id)
        except Exception:
            raise Exception('Введен неверный для ID Требования к соискателю: '
                            f'{applicant_requirements_id}')


class VacancyFieldOfActivity(BaseModel):
    '''Класс, описывающий cпециальности соискателей'''

    def __init__(self, id: int | str | None, vacancy_id: int | str,
                 field_of_activity_id: int | str
                 ) -> None:
        super().__init__(id)
        try:
            self.vacancy_id = int(vacancy_id)
        except Exception:
            raise Exception('Введен неверный для ID Вакансия: '
                            f'{vacancy_id}')
        try:
            self.field_of_activity_id = int(field_of_activity_id)
        except Exception:
            raise Exception('Введен неверный для ID Сферы деятельности: '
                            f'{field_of_activity_id}')
