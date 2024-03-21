from pydantic import BaseModel


class CalculationBase(BaseModel):
    expression: str
    result: float

class CalculationCreate(CalculationBase):
    pass

class Calculation(CalculationBase):
    id: int
    class Config:
        from_attributes = True

class Expression(BaseModel):
    expression_text: str
