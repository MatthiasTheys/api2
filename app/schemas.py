from pydantic import BaseModel

class LiftBase(BaseModel):
    name: str
    amount: str
    reps: int

class LiftCreate(LiftBase):
    pass

class Lift(LiftBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    id: int

class User(UserBase):
    id: int
    is_active: bool
    lifts: list[Lift] = []

    class Config:
        orm_mode = True
