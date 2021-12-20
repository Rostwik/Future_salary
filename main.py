from dotenv import load_dotenv

from hh import get_hh_job_openings
from superjob import get_superjob_job_openings
from table_view import displaying_vacancies


def main():
    load_dotenv()

    programming_languages = {
        'Java': {},
        'C': {},
        'Python': {},
        'C++': {},
        'Go': {},
        'C#': {},
        'Fortran': {},
        'JavaScript': {},
        'РНР': {},
        'Scratch': {},
    }

    hh_jobs = get_hh_job_openings(programming_languages)
    displaying_vacancies(hh_jobs, 'HeadHunter Moscow')
    superjobs_jobs = get_superjob_job_openings(programming_languages)
    displaying_vacancies(superjobs_jobs, 'SuperJob Moscow')


if __name__ == '__main__':
    main()
