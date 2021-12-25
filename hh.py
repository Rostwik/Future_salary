import itertools

import requests

from predict_salary import predict_rub_salary, save_analysis_result


def collecting_job_statistics(keyword, url):
    salaries = []
    jobs = []
    payload = {
        'text': keyword
    }
    page_response = requests.get(url, params=payload)
    page_response.raise_for_status()
    page_response = page_response.json()
    pages_number = page_response['pages']
    vacancies_found = page_response['found']

    for page in itertools.count():
        if page == pages_number:
            break
        payload = {
            'text': keyword,
            'page': page,
            'per_page': 20
        }
        page_response = requests.get(url, params=payload)
        page_response.raise_for_status()

        jobs.extend(page_response.json()['items'])
    for job in jobs:
        if job['salary'] and job['salary']['currency'] == 'RUR':
            salary = predict_rub_salary(job['salary']['from'], job['salary']['to'])
            salaries.append(salary)

    return salaries, vacancies_found


def get_hh_job_openings(keywords):
    job_analysis_result = {x: {} for x in keywords}

    for keyword in keywords:
        url = "https://api.hh.ru/vacancies"

        salaries, vacancies_found = collecting_job_statistics(keyword, url)

        job_analysis_result_copy = {**job_analysis_result}
        job_analysis_result = save_analysis_result(
            keyword, salaries, vacancies_found, job_analysis_result_copy
        )

    return job_analysis_result
