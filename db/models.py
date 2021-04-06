from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db import Base, engine

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    study_option_id = Column(Integer, ForeignKey('study_options.id'), index=True, nullable=False)
    course_name = Column(String)
    school = Column(Integer, ForeignKey('schools.id'), index=True, nullable=False)
    cost = Column(Integer)
    rating = Column(Float)
    link = Column(String(400), unique=True)

    def __repr__(self):
        return f"{self.course_name}, {self.school}, {self.cost}, {self.rating}"


class StudyOption(Base):
    __tablename__ = 'study_options'
    id = Column(Integer, primary_key=True)
    study_option = Column(String)

    def __repr__(self):
        return f'{self.id},{self.study_option}'


class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    skill = Column(String)


class School(Base):
    __tablename__ = 'schools'
    id = Column(Integer, primary_key=True)
    school_name = Column(String)


class SkillRelation(Base):
    __tablename__ = 'skill_relations'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), index=True, nullable=False)
    skill_id = Column(Integer, ForeignKey('skills.id'), index=True, nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
