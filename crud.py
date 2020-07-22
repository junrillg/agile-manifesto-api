# type: ignore
from sqlalchemy.orm import Session
from models import Principle, Value
from schemas import DataRequest


def get_all_models(db: Session):
    principles = db.query(Principle)
    values = db.query(Value)
    return {"principles": principles.all(), "values": values.all()}


def create_from_model(db: Session, model, data_request: DataRequest):
    data = model()
    data.content = data_request.content
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update_from_model(db: Session, model, data_id: int, data_request: DataRequest):
    data = db.query(model).filter(model.id == data_id).first()
    data.content = data_request.content
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def delete_from_model(db: Session, model, data_id: int):
    data = db.query(model).filter(model.id == data_id).first()
    db.delete(data)
    db.commit()
