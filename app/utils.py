from telegram import ReplyKeyboardMarkup

from config import SKILLS, STUDY_OPTIONS

from db import db_session, engine
from db.models import StudyOption


def study_options_keybord():
    return ReplyKeyboardMarkup(
        [STUDY_OPTIONS, ['Затрудняюсь...']],
        one_time_keyboard=True, resize_keyboard=True # one time - клавитура проподает,resize-маштаб эстетитка 
        )


def skills_keyboard(study_option):
    skills = SKILLS[study_option]
    return ReplyKeyboardMarkup(
        [skills], one_time_keyboard=True, resize_keyboard=True
    )

def table_call():
    calling_the_project_from_database = StudyOption.query.all()
    return calling_the_project_from_database
