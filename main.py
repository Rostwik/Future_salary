import os

from dotenv import load_dotenv

from hh import get_hh_job_statistics
from superjob import get_superjob_job_statistics
from table_view import get_vacancies_table

SJ_MOSCOW_CODE = 4
HH_MOSCOW_CODE = 1
SJ_DEVELOPMENT_CATEGORY = 48


def main():
    load_dotenv()
    superjob_token = os.getenv('SUPERJOB_SECRET_KEY')

    programming_languages = [
        'Java',
        'C',
        'Python',
        'C++',
        'Go',
        'C#',
        'Fortran',
        'JavaScript',
        'РНР',
        'Scratch',
    ]

    hh_jobs = get_hh_job_statistics(programming_languages, HH_MOSCOW_CODE)
    table_instance = get_vacancies_table(hh_jobs, 'HeadHunter Moscow')
    print(table_instance.table)
    superjobs_jobs = get_superjob_job_statistics(
        programming_languages,
        superjob_token,
        SJ_MOSCOW_CODE,
        SJ_DEVELOPMENT_CATEGORY)
    table_instance = get_vacancies_table(superjobs_jobs, 'SuperJob Moscow')
    print(table_instance.table)


if __name__ == '__main__':
    main()
