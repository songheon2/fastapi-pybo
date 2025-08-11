# 질문 관련 함수 정의
from datetime import datetime

from domain.question.question_schema import QuestionCreate
from models import Question
from sqlalchemy.orm import Session

# 모든 질문을 list로 반환
def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list

# question id로 질문 조회
def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           create_date=datetime.now())
    db.add(db_question)
    db.commit()