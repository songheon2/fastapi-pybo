from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import  get_db
from domain.question import question_schema, question_crud

router = APIRouter(
    prefix="/api/question",
)

# response_model 속성 : question_list 리턴값은 Question 스키마로 구성된 리스트로 세팅
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    # db = SessionLocal()
    # db.close()
    _question_list = question_crud.get_question_list(db)
    return _question_list

# /detail/:question_id 요청 처리
@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question