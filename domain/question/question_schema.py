import datetime

from pydantic import BaseModel

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
