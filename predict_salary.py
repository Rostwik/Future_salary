def predict_rub_salary(salary_from, salary_to, currency='RUR'):
    if currency != 'RUR':
        average_salary = None

    elif salary_from and not salary_to:
        average_salary = salary_from * 1.2

    elif not salary_from and salary_to:
        average_salary = salary_to * 0.8

    else:
        average_salary = (salary_from + salary_to) / 2

    return average_salary
