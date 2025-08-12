from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import  get_db
from domain.question import question_schema, question_crud
from starlette import status

router = APIRouter(
    prefix="/api/question",
)

# response_model 속성 : question_list 리턴값은 Question 스키마로 구성된 리스트로 세팅
@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db),page: int = 0, size: int = 10):
    # page : 페이지 번호  size : 한 페이지에 보여줄 게시물 갯수
    total, _question_list = question_crud.get_question_list(
    db, skip = page * size, limit = size)
    return {
        # 출력 스키마( QuestionList ) 에 매핑되는 딕셔너리로 return
        'total': total,
        'question_list': _question_list
    }

# /detail/:question_id 요청 처리
@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)