from terminaltables import AsciiTable


def get_vacancies_table(programming_languages, title):
    column_headers = [[
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата'
    ]]

    for language, details in programming_languages.items():
        column_headers.append([
            language,
            details['vacancies_found'],
            details['vacancies_processed'],
            details['average_salary'],
        ])

    table_instance = AsciiTable(column_headers, title)
    table_instance.justify_columns[3] = 'right'

    return table_instance
