import requests

from predict_salary import predict_rub_salary


def get_superjob_job_openings(keywords, superjob_token):
    superjob_header = {'X-Api-App-Id': superjob_token}
    url = 'https://api.superjob.ru/2.0/vacancies'
    job_analysis_result = {x: {} for x in keywords}

    for keyword in keywords:
        page = 0
        number_pages = 1
        jobs = []
        salaries = []
        while page < number_pages:
            payloads = {
                'town': 4,
                'catalogues': 48,
                'page': page,
                'count': 20,
                'keyword': keyword
            }

            response = requests.get(url, headers=superjob_header, params=payloads)
            response.raise_for_status()

            number_pages = response.json()['total'] / payloads['count']
            job_analysis_result[keyword]['vacancies_found'] = response.json()['total']
            page += 1
            for item in response.json()['objects']:
                jobs.append(item)

        for job in jobs:
            salary = predict_rub_salary(job['payment_from'], job['payment_to'])
            if salary is not None:
                salaries.append(salary)

        job_analysis_result[keyword]['vacancies_processed'] = len(salaries)
        try:
            job_analysis_result[keyword]['average_salary'] = int(sum(salaries) / len(salaries))
        except ZeroDivisionError:
            print(f'Для языка {keyword} ваканский не найдено!')

    return job_analysis_result
