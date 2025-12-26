from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:1337@localhost/Orm')
Session = sessionmaker(bind=engine)
session = Session()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String, nullable=False)
    students = relationship('Student', back_populates='group', cascade='all, delete-orphan')
class Worktype(Base):
    __tablename__ = 'worktypes'
    id = Column(Integer, primary_key=True)
    worktype_name = Column(String, nullable=False)
    marks = relationship('Mark', back_populates='worktype', cascade='all, delete-orphan')


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')
    marks = relationship('Mark', back_populates='student', cascade='all, delete-orphan')


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String, nullable=False)
    marks = relationship('Mark', back_populates='subject', cascade='all, delete-orphan')

class Mark(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    worktype_id = Column(Integer,ForeignKey('worktypes.id'))
    mark_value = Column(String, nullable=True)
    sem_number = Column(Integer, nullable=False)
    subject = relationship('Subject', back_populates='marks')
    worktype = relationship('Worktype', back_populates='marks')
    student = relationship('Student', back_populates='marks')

Base.metadata.create_all(engine)

#k373b = Group(group_name='K3-75Б')
#k374b = Group(group_name='K3-76Б')
#ivanov = Student(student_name='Иванов И.П.', group_id=3)
#petrov = Student(student_name='Петров П.И.', group_id=4)
#session.add_all([k373b, k374b, ivanov, petrov])
#session.commit()


results = session.query(Student).join(Group).all()
for stud in results:
     print(f'Student: {stud.student_name}, Group name: {stud.group.group_name}')
session.close()