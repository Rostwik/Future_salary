from terminaltables import AsciiTable


def get_vacancies_table(programming_languages, title):
    table_rows = [[
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата'
    ]]

    for language, details in programming_languages.items():
        table_rows.append([
            language,
            details['vacancies_found'],
            details['vacancies_processed'],
            details['average_salary'],
        ])

    table_instance = AsciiTable(table_rows, title)
    table_instance.justify_columns[3] = 'right'

    return table_instance
