def predict_rub_salary(salary_from, salary_to, currency='RUR'):
    if currency != 'RUR':
        average_salary = None

    elif salary_from is not None and salary_to is None:
        average_salary = salary_from * 1.2

    elif salary_from is None and salary_to is not None:
        average_salary = salary_to * 0.8

    else:
        average_salary = (salary_from + salary_to) / 2

    return average_salary


def save_job_analysis(job_analysis_result, keyword, salaries):
    job_analysis_result[keyword]['vacancies_processed'] = len(salaries)
    try:
        job_analysis_result[keyword]['average_salary'] = int(sum(salaries) / len(salaries))
    except ZeroDivisionError:
        job_analysis_result[keyword]['vacancies_found'] = 0
        job_analysis_result[keyword]['vacancies_processed'] = 0
        job_analysis_result[keyword]['average_salary'] = 0