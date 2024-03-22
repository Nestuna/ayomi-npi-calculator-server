from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine
from app.lib import npi
from app.lib import data

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/calculations/', response_model=list[schemas.Calculation])
def read_calculations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    calculations = crud.get_calculations(db, skip=skip, limit=limit)

    return calculations

@app.get('/calculations/csv')
def read_calculations_csv(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    calculations = crud.get_calculations(db, skip=skip, limit=limit)
    calc_dict_list = []

    for item in calculations:
        item_dict = {
            'expression' : item.expression,
            'result' : item.result,
            'id' : item.id
        }
        calc_dict_list.append(item_dict)

    calc_csv = data.data_to_csv(calc_dict_list)
    return StreamingResponse(
        iter(calc_csv),
        media_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename=data.csv'}
    )

@app.post('/calculate_npi', response_model=schemas.Calculation)
def make_calculate_npi(expression: schemas.Expression, db: Session = Depends(get_db)):
    npi_result = {'expression': expression.expression_text,
                  'result': npi.calculate_from_npi(expression.expression_text)}
    calculation = crud.create_calculation(db, calculation=npi_result)

    return calculation

