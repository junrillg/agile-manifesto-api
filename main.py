# type: ignore
import models
import crud
from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from schemas import DataRequest
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/agile/manifesto")
def get_manifesto(db: Session = Depends(get_db)):
    """
    Fetch principles and values from agile software development
    """
    db_models = crud.get_all_models(db)
    if db_models is None:
        raise HTTPException(
            status_code=400, detail="Unable to retrieve Agile Manifesto"
        )
    return db_models


@app.post("/agile/principle", status_code=201)
def create_principle(data_request: DataRequest, db: Session = Depends(get_db)):
    """
    Creates principle on agile software development
    """
    db_principle = crud.create_from_model(db, models.Principle, data_request)
    return {"data": db_principle, "message": "Principle was successfully added"}


@app.put("/agile/principle/{principle_id}")
def update_principle(
    principle_id: int, data_request: DataRequest, db: Session = Depends(get_db)
):
    """
    Update principle from agile software development
    """
    db_principle = crud.update_from_model(
        db, models.Principle, principle_id, data_request
    )
    return {"data": db_principle, "message": "Principle was successfully updated"}


@app.delete("/agile/principle/{principle_id}")
def delete_principle(principle_id: int, db: Session = Depends(get_db)):
    """
    Delete principle from agile software development
    """
    crud.delete_from_model(db, models.Principle, principle_id)
    return {"message": "Principle was successfully deleted"}


@app.post("/agile/value", status_code=201)
def create_value(data_request: DataRequest, db: Session = Depends(get_db)):
    """
    Creates value on agile software development
    """
    db_value = crud.create_from_model(db, models.Value, data_request)
    return {"data": db_value, "message": "Value was successfully added"}


@app.put("/agile/value/{value_id}")
def update_value(
    value_id: int, data_request: DataRequest, db: Session = Depends(get_db)
):
    """
    Update value from agile software development
    """
    db_value = crud.update_from_model(db, models.Value, value_id, data_request)
    return {"data": db_value, "message": "Value was successfully updated"}


@app.delete("/agile/value/{value_id}")
def delete_value(value_id: int, db: Session = Depends(get_db)):
    """
    Delete value from agile software development
    """
    crud.delete_from_model(db, models.Value, value_id)
    return {"message": "Value was successfully deleted"}
