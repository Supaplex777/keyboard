from telegram.ext import ConversationHandler, CallbackContext
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    InlineKeyboardButton

from config import STUDY_OPTIONS, SKILLS
from .texts import welcome_text
from .utils import study_options_keybord, skills_keyboard, table_call
from db.models import StudyOption, Course

FIRST_STEP, SECOND_STEP = range(2)


def start_bot(update: Update, context: CallbackContext):
    keyboard = []
    options = StudyOption.query.all()
    if options:
        for x in options:
            keyboard.append([InlineKeyboardButton(x.study_option,
                                                  callback_data=x.id)])

    update.message.reply_text(text='Start, choose',
                              reply_markup=InlineKeyboardMarkup(keyboard))
    return FIRST_STEP


def start_over(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = []
    options = StudyOption.query.all()
    if options:
        for x in options:
            keyboard.append([InlineKeyboardButton(x.study_option,
                                                  callback_data=x.id)])
    query.edit_message_text(text='Start, choose',
                            reply_markup=InlineKeyboardMarkup(keyboard))
    return FIRST_STEP


def selected(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    courses = Course.query.filter(Course.study_option_id == query.data)
    if courses:
        keyboard = []
        for x in courses:
            keyboard.append([InlineKeyboardButton(x.course_name, callback_data=x.course_name)])
        query.edit_message_text(text=f'Selected: {query.data}', reply_markup=InlineKeyboardMarkup(keyboard))
        return SECOND_STEP


def selected_course(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f'Ты будешь изучать {query.data}')
    return ConversationHandler.END
# def generate_skills(update,context):
# study_option = update.message.text
# if study_option in STUDY_OPTIONS:
# update.message.reply_text(
# 'Выберите навык, который хотите изучить.',
# reply_markup=skills_keyboard(study_option))
# return 'courses'


# def generate_courses(update, context):
#     course_name = update.message.text
#     print(SKILLS.values())
#     for skills in SKILLS.values():
#         if course_name in skills:
#             update.message.reply_text(
#                 f'ЗДЕСЬ БУДЕТ СПИСОК КУРСОВ ПО {course_name}'
#                 )
#             return ConversationHandler.END
