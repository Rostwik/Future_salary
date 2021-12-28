import itertools

import requests

from predict_salary import predict_rub_salary, save_analysis_result

MOSCOW_CODE = 4
DEVELOPMENT_CATEGORY = 48


def collecting_job_statistics(keyword, superjob_header, url):
    jobs = []
    salaries = []

    payloads = {
        'town': MOSCOW_CODE,
        'catalogues': DEVELOPMENT_CATEGORY,
        'count': 20,
        'keyword': keyword
    }
    response = requests.get(url, headers=superjob_header, params=payloads)
    response.raise_for_status()

    vacancies_found = response.json()['total']

    for page in itertools.count():

        payloads = {
            'town': MOSCOW_CODE,
            'catalogues': DEVELOPMENT_CATEGORY,
            'page': page,
            'count': 20,
            'keyword': keyword
        }
        response = requests.get(url, headers=superjob_header, params=payloads)
        response.raise_for_status()
        json_response = response.json()

        jobs.extend(json_response['objects'])

        if not json_response['more']:
            break

    for job in jobs:
        if job['currency'] == "rub":
            salary = predict_rub_salary(job['payment_from'], job['payment_to'])
            salaries.append(salary)

    return salaries, vacancies_found


def get_superjob_job_statistics(keywords, superjob_token):
    superjob_header = {'X-Api-App-Id': superjob_token}
    url = 'https://api.superjob.ru/2.0/vacancies'
    job_analysis_result = {x: {} for x in keywords}

    for keyword in keywords:
        salaries, vacancies_found = collecting_job_statistics(
            keyword, superjob_header, url
        )

        job_analysis_result_copy = {**job_analysis_result}
        job_analysis_result = save_analysis_result(
            keyword, salaries, vacancies_found, job_analysis_result_copy
        )

    return job_analysis_result
