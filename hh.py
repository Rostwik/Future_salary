import itertools

import requests

from predict_salary import predict_rub_salary, get_analytics


def get_keyword_statistics(keyword, town_code):
    url = "https://api.hh.ru/vacancies"
    salaries = []
    jobs = []

    for page in itertools.count():

        payload = {
            'text': keyword,
            'page': page,
            'area': town_code,
            'per_page': 20
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        page_response = response.json()
        pages_number = page_response['pages']

        jobs.extend(page_response['items'])

        if page >= pages_number - 1:
            break

    vacancies_found = page_response['found']

    for job in jobs:
        if job['salary'] and job['salary']['currency'] == 'RUR':
            salary = predict_rub_salary(job['salary']['from'], job['salary']['to'])
            if salary:
                salaries.append(salary)

    return salaries, vacancies_found


def get_hh_job_statistics(keywords, town_code):
    job_analysis = {}

    for keyword in keywords:
        salaries, vacancies_found = get_keyword_statistics(keyword, town_code)

        job_analysis[keyword] = get_analytics(
            salaries, vacancies_found
        )

    return job_analysis
