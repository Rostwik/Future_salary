import requests

from predict_salary import predict_rub_salary, save_job_analysis


def get_hh_job_openings(keywords):
    job_analysis_result = {x: {} for x in keywords}

    for keyword in keywords:

        url = "https://api.hh.ru/vacancies"

        pages_number = 1
        page = 0
        salaries = []
        jobs = []

        while page < pages_number:
            payload = {
                'text': keyword,
                'page': page,
                'per_page': 20
            }
            page_response = requests.get(url, params=payload)
            page_response.raise_for_status()

            pages_number = page_response.json()['pages']
            job_analysis_result[keyword]['vacancies_found'] = page_response.json()['found']
            page += 1
            for item in page_response.json()['items']:
                jobs.append(item)

        for job in jobs:
            if job['salary']:
                salary = predict_rub_salary(job['salary']['from'], job['salary']['to'], job['salary']['currency'])
                if salary is not None:
                    salaries.append(salary)

        save_job_analysis(job_analysis_result, keyword, salaries)

    return job_analysis_result
