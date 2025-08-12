import datetime

from pydantic import BaseModel, field_validator

from domain.answer.answer_schema import Answer


# pydantic 의 BaseModel 상속
class Question(BaseModel):
    # 선언한 항목은 모두 필수 항목으로 설정
    # subject: str | None = None 필수 항목이 아니게 설정
    id: int
    subject: str
    content: str

    create_date: datetime.datetime
    # answer 스키마로 구성된 answers 리스트
    answers: list[Answer] = []

# 질문 등록 스키마
class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class QuestionList(BaseModel):
    # 전체 계시물 갯수
    total: int = 0
    # 질문 목록
    question_list: list[Question] = []