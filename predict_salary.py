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


def get_analytics(salaries, vacancies_found):
    try:
        average_salary = int(sum(salaries) / len(salaries))

    except ZeroDivisionError:
        average_salary = 0

    job_analysis = {
        'vacancies_processed': len(salaries),
        'vacancies_found': vacancies_found,
        'average_salary': average_salary
    }

    return job_analysis
