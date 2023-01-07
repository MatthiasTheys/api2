from sqlalchemy.orm import Session
import auth
import models
import schemas

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_heaviest_lift(db: Session, user_id: int):
    return db.query(models.Lift).filter(models.Lift.owner_id == user_id).order_by(models.Lift.amount.desc()).first()

def get_user_lifts(db: Session, user_id: int):
    return db.query(models.Lift).filter(models.Lift.owner_id == user_id).all()

def create_user_lift(db: Session, lift: schemas.LiftCreate, user_id: int):
    db_lift = models.Lift(**lift.dict(), owner_id=user_id)
    db.add(db_lift)
    db.commit()
    db.refresh(db_lift)
    return db_lift

def update_user_lift(db: Session, lift: schemas.LiftCreate, user_id: int):
    db_lift = db.query(models.Lift).filter(models.Lift.owner_id == user_id).order_by(models.Lift.amount.desc()).first()
    db_lift.name = lift.name
    db_lift.amount = lift.amount
    db_lift.reps = lift.reps
    db.commit()
    db.refresh(db_lift)
    return db_lift

def remove_user_lift(db: Session, user_id: int):
    db_lift = db.query(models.Lift).filter(models.Lift.owner_id == user_id).order_by(models.Lift.amount.desc()).first()
    db.delete(db_lift)
    db.commit()
    return db_lift

def remove_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user