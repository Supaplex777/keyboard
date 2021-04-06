from db.models import StudyOption

STUDY_OPTIONS = StudyOption.query.all()
print(STUDY_OPTIONS)