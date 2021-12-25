import os

from dotenv import load_dotenv

from hh import get_hh_job_openings
from superjob import get_superjob_job_openings
from table_view import get_vacancies_table


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

    # hh_jobs = get_hh_job_openings(programming_languages)
    # table_instance = get_vacancies_table(hh_jobs, 'HeadHunter Moscow')
    # print(table_instance.table)
    superjobs_jobs = get_superjob_job_openings(programming_languages, superjob_token)
    table_instance = get_vacancies_table(superjobs_jobs, 'SuperJob Moscow')
    print(table_instance.table)


if __name__ == '__main__':
    main()
