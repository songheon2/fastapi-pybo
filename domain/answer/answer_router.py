from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.question import question_crud

router = APIRouter(
    prefix="/api/answer",
)

# 출력할 게 없을 때 HTTP 상태 코드 중 204( NO content)를 리턴
# 204는 오류가 아닌 정상적으로 답변을 저장하고 리턴할 데이터가 필요 없다는 의미
@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id: int,
                  _answer_create: answer_schema.AnswerCreate,
                  db: Session = Depends(get_db)):

    # create answer
    question = question_crud.get_question(db, question_id=question_id)
    if not question:
<<<<<<< HEAD
=======
        # 답변이 없으면 detail 출력
>>>>>>> c418497 (2-7답변등록까지 커밋)
        raise HTTPException(status_code=404, detail="Question not found")
    answer_crud.create_answer(db, question=question,
                              answer_create=_answer_create)