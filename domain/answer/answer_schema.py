from pydantic import BaseModel, field_validator


# 답변 content 부분 스키마
class AnswerCreate(BaseModel):
    content: str

    # content가 저장될 때 not_empty 함수 실행
    # content가 비어 있으면 에러 리턴
    @field_validator('content')
    # cls : class 줄임말로 현재 클래스를 참조한다는 의미 ( self로 변경가능)
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v