import itertools

import requests

from predict_salary import predict_rub_salary, save_analysis_result


def get_keyword_statistics(keyword, url):
    salaries = []
    jobs = []

    for page in itertools.count():

        payload = {
            'text': keyword,
            'page': page,
            'per_page': 20
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        page_response = response.json()
        pages_number = page_response['pages']

        jobs.extend(page_response['items'])

        if page == 99:
            break

    vacancies_found = page_response['found']

    for job in jobs:
        if job['salary'] and job['salary']['currency'] == 'RUR':
            salary = predict_rub_salary(job['salary']['from'], job['salary']['to'])
            if salary:
                salaries.append(salary)

    return salaries, vacancies_found


def get_hh_job_statistics(keywords):
    job_analysis = {x: {} for x in keywords}

    for keyword in keywords:
        url = "https://api.hh.ru/vacancies"

        salaries, vacancies_found = get_keyword_statistics(keyword, url)

        job_analysis[keyword] = save_analysis_result(
            salaries, vacancies_found
        )

    return job_analysis
