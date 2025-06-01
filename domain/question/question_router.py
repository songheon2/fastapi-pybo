from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, get_db
from domain.question import question_schema
from models import Question

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    # db = SessionLocal()
    # db.close()
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()

    return _question_list
