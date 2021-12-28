import itertools

import requests

from predict_salary import predict_rub_salary, save_analysis_result

MOSCOW_CODE = 4
DEVELOPMENT_CATEGORY = 48


def get_keyword_statistics(keyword, superjob_header, url, town_code, category_code):
    jobs = []
    salaries = []

    for page in itertools.count():

        payloads = {
            'town': town_code,
            'catalogues': category_code,
            'page': page,
            'count': 20,
            'keyword': keyword
        }
        response = requests.get(url, headers=superjob_header, params=payloads)
        response.raise_for_status()
        page_response = response.json()

        jobs.extend(page_response['objects'])

        if not page_response['more']:
            break

    vacancies_found = page_response['total']

    for job in jobs:
        if job['currency'] == "rub":
            salary = predict_rub_salary(job['payment_from'], job['payment_to'])
            salaries.append(salary)

    return salaries, vacancies_found


def get_superjob_job_statistics(keywords, superjob_token):
    superjob_header = {'X-Api-App-Id': superjob_token}
    url = 'https://api.superjob.ru/2.0/vacancies'
    job_analysis = {x: {} for x in keywords}

    for keyword in keywords:
        salaries, vacancies_found = get_keyword_statistics(
            keyword, superjob_header, url, MOSCOW_CODE, DEVELOPMENT_CATEGORY
        )

        job_analysis_copy = {**job_analysis}
        job_analysis = save_analysis_result(
            keyword, salaries, vacancies_found, job_analysis_copy
        )

    return job_analysis
