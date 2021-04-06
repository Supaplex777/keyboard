import csv
import random

from db import db_session
from db.models import School, Skill, StudyOption


def read_data(filename, fields):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, fields, delimiter=';')
        data = []
        for row in reader:
            data.append(row)
        return data


def upload_study_options(data):
    all_study_options = []
    for row in data:
        study_option = {
            'study_option': row['study_option']
        }
        all_study_options.append(study_option)
    db_session.bulk_insert_mappings(StudyOption, all_study_options, return_defaults=True)
    db_session.commit()


def upload_skills(data):
    all_skills = []
    for row in data:
        list_of_skills = row['skills'].split(',')
        for skill in list_of_skills:
            each_skill = {
                'skill': skill
            }
            all_skills.append(each_skill)
    db_session.bulk_insert_mappings(Skill, all_skills, return_defaults=True)
    db_session.commit()


def upload_schools(data):
    all_schools = []
    for row in data:
        school = {
            'school_name': row['school']
        }
        all_schools.append(school)
    db_session.bulk_insert_mappings(School, all_schools, return_defaults=True)
    db_session.commit()

# БУЩУЩИЙ ГЕНЕРАТОР ИНФЫ ДЛЯ ОСНОВНОЙ ТАБЛИЦЫ Courses
# def upload_courses(num):
#     data = generate_data(num)
    
    
# def generate_course_data(num_rows):
#     all_data = []
#     for row in range(num_rows):
#         course = {
#             'study_options': random.randint(1, 3), 

#             random.choice(opt), random.choice(skl), 'Название курса', 
#             random.choice(skl), random.randint(20000, 200000), round(random.uniform(1, 5), 1),
#             'Ccылка'
#         }
#         all_data.append(course)
#     return(all_data)


if __name__ == "__main__":
    # читаем инфо по направлениям и навыкам
    study_options_and_skills_data = read_data('study_options_and_skills.csv', ['study_option', 'skills'])
    # загружаем направления и навыки в таблицы
    upload_study_options(study_options_and_skills_data)
    upload_skills(study_options_and_skills_data)
    # читаем инфо по школам и загружаем в таблицу школ
    schools_data = read_data('schools.csv', ['school'])
    upload_schools(schools_data)
