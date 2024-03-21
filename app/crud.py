from sqlalchemy.orm import Session

from . import models, schemas


def get_calculations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Calculation).offset(skip).limit(limit).all()


def create_calculation(db: Session, calculation: schemas.CalculationCreate):
    db_calculation = models.Calculation(**calculation)
    db.add(db_calculation)
    db.commit()
    db.refresh(db_calculation)
    return db_calculation
