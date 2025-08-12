# 질문 관련 함수 정의
from datetime import datetime

from domain.question.question_schema import QuestionCreate
from models import Question
from sqlalchemy.orm import Session

# 모든 질문을 list로 반환
# skip : 조회한 데이터의 시작 위치
# limit : 시작위치부터 가져올 데이터의 건수
# ex) skip = 20, limit = 10 -> 21~30번째 데이터
def get_question_list(db: Session, skip: int = 0, limit: int = 10):
    _question_list = db.query(Question)\
        .order_by(Question.create_date.desc())

    total = _question_list.count()
    question_list = _question_list.offset(skip).limit(limit).all()
    return total, question_list  # (전체 건수, 페이징 적용된 질문 목록)

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