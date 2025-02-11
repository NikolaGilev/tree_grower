from sqlmodel import SQLModel, Field


class Tree(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
    height: float
