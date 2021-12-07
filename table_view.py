from terminaltables import AsciiTable


def table_view(programming_languages, title):
    output_data = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]

    for language, details in programming_languages.items():

        if details['vacancies_found']:
            output_data.append([
                language,
                details['vacancies_found'],
                details['vacancies_processed'],
                details['average_salary'],
            ])

    table_instance = AsciiTable(output_data, title)
    table_instance.justify_columns[3] = 'right'
    print(table_instance.table)
    print()
