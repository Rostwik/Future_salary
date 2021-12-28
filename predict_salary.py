def predict_rub_salary(salary_from, salary_to):
    if salary_from and not salary_to:
        average_salary = salary_from * 1.2

    elif not salary_from and salary_to:
        average_salary = salary_to * 0.8

    elif not salary_from and not salary_to:
        average_salary = 0
    else:
        average_salary = (salary_from + salary_to) / 2

    return average_salary


def save_analysis_result(keyword, salaries, vacancies_found, job_analysis_result):
    try:
        job_analysis_result = {
            keyword: {
                'vacancies_processed': len(salaries),
                'vacancies_found': vacancies_found,
                'average_salary': int(sum(salaries) / len(salaries))
            }
        }

    except ZeroDivisionError:
        job_analysis_result = {
            keyword: {
                'vacancies_processed': 0,
                'vacancies_found': 0,
                'average_salary': 0
            }
        }

    return job_analysis_result
