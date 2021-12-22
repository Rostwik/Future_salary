import itertools

import requests

from predict_salary import predict_rub_salary, save_job_analysis


def collect_statistics(jobs, salaries):
    for job in jobs:
        if job['salary']:
            salary = predict_rub_salary(job['salary']['from'], job['salary']['to'], job['salary']['currency'])
            if salary is not None:
                salaries.append(salary)


def get_hh_job_openings(keywords):
    job_analysis_result = {x: {} for x in keywords}

    for keyword in keywords:

        url = "https://api.hh.ru/vacancies"

        pages_number = 1
        salaries = []
        jobs = []

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

            pages_number = page_response.json()['pages']
            job_analysis_result[keyword]['vacancies_found'] = page_response.json()['found']
            jobs.extend(page_response.json()['items'])

        collect_statistics(jobs, salaries)

        save_job_analysis(job_analysis_result, keyword, salaries)

    return job_analysis_result
