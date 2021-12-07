import requests


def predict_rub_salary(salary):
    if salary['currency'] != 'RUR':
        average_salary = None
    elif salary['from'] is not None and salary['to'] is None:
        average_salary = salary['from'] * 1.2

    elif salary['from'] is None and salary['to'] is not None:
        average_salary = salary['to'] * 0.8

    else:
        average_salary = (salary['from'] + salary['to']) / 2

    return average_salary


def get_hh_job_openings(programming_languages):
    for language in programming_languages:

        url = "https://api.hh.ru/vacancies"

        pages_number = 1
        page = 0
        salaries = []
        items = []

        while page < pages_number:
            payload = {
                'text': language,
                'only_with_salary': True,
                'page': page,
                'per_page': 20
            }
            page_response = requests.get(url, params=payload)
            page_response.raise_for_status()

            pages_number = page_response.json()['pages']
            programming_languages[language]['vacancies_found'] = page_response.json()['found']
            page += 1
            for item in page_response.json()['items']:
                items.append(item)

        for vacancy in items:

            salary = predict_rub_salary(vacancy['salary'])
            if salary is not None:
                salaries.append(salary)

        programming_languages[language]['vacancies_processed'] = len(salaries)
        programming_languages[language]['average_salary'] = int(sum(salaries) / len(salaries))

    return programming_languages