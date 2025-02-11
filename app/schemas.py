from pydantic import BaseModel


class TreeBase(BaseModel):
    name: str
    age: int
    height: float


class TreeCreate(TreeBase):
    pass


class TreeUpdate(TreeBase):
    pass


class TreeResponse(TreeBase):
    id: int
