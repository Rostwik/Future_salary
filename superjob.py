import os

import requests


def predict_rub_salary_for_superjob(vacancy):
    if vacancy['payment_from'] == 0 and vacancy['payment_to'] == 0:
        average_salary = None

    elif vacancy['payment_from'] != 0 and vacancy['payment_to'] == 0:
        average_salary = vacancy['payment_from'] * 1.2

    elif vacancy['payment_from'] == 0 and vacancy['payment_to'] != 0:
        average_salary = vacancy['payment_to'] * 0.8

    else:
        average_salary = (vacancy['payment_from'] + vacancy['payment_to']) / 2

    return average_salary


def get_superjob_job_openings(programming_languages):
    superjob_token = os.getenv('SUPERJOB_SECRET_KEY')
    superjob_header = {'X-Api-App-Id': superjob_token}
    url = 'https://api.superjob.ru/2.0/vacancies'
    for language in programming_languages:
        page = 0
        number_pages = 1
        items = []
        salaries = []
        while page < number_pages:
            payloads = {
                'town': 4,
                'catalogues': 48,
                'page': page,
                'count': 20,
                'keyword': language
            }

            response = requests.get(url, headers=superjob_header, params=payloads)
            response.raise_for_status()

            number_pages = response.json()['total'] / payloads['count']
            programming_languages[language]['vacancies_found'] = response.json()['total']
            page += 1
            for item in response.json()['objects']:
                items.append(item)

        for vacancy in items:
            salary = predict_rub_salary_for_superjob(vacancy)
            if salary is not None:
                salaries.append(salary)

        programming_languages[language]['vacancies_processed'] = len(salaries)
        try:
            programming_languages[language]['average_salary'] = int(sum(salaries) / len(salaries))
        except ZeroDivisionError:
            print(f'Для языка {language} ваканский не найдено!')

    return programming_languages
