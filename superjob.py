import itertools

import requests

from predict_salary import predict_rub_salary

MOSCOW_CODE = 4
DEVELOPMENT_CATEGORY = 48


def save_analysis_result(keyword, salaries, vacancies_found, job_analysis_result):

    job_analysis_result[keyword]['vacancies_processed'] = len(salaries)
    job_analysis_result[keyword]['vacancies_found'] = vacancies_found
    try:
        job_analysis_result[keyword]['average_salary'] = int(sum(salaries) / len(salaries))
    except ZeroDivisionError:
        job_analysis_result[keyword]['vacancies_found'] = 0
        job_analysis_result[keyword]['vacancies_processed'] = 0
        job_analysis_result[keyword]['average_salary'] = 0

    return job_analysis_result


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

    number_pages = response.json()['total'] / payloads['count']
    vacancies_found = response.json()['total']

    for page in itertools.count():
        if page > number_pages:
            break

        payloads = {
            'town': MOSCOW_CODE,
            'catalogues': DEVELOPMENT_CATEGORY,
            'page': page,
            'count': 20,
            'keyword': keyword
        }
        response = requests.get(url, headers=superjob_header, params=payloads)
        response.raise_for_status()

        jobs.extend(response.json()['objects'])

    for job in jobs:
        salary = predict_rub_salary(job['payment_from'], job['payment_to'])
        if salary is not None:
            salaries.append(salary)

    return salaries, vacancies_found


def get_superjob_job_openings(keywords, superjob_token):
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
