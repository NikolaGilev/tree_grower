from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from contextlib import asynccontextmanager
import uvicorn

from db import create_db_and_tables
from models import Tree
from crud import create_tree, get_trees, get_tree, update_tree, delete_tree
from schemas import TreeCreate, TreeUpdate, TreeResponse
from dependencies import get_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/trees/", response_model=TreeResponse)
def create_tree_endpoint(tree: TreeCreate, db: Session = Depends(get_database)):
    return create_tree(db, Tree(**tree.dict()))


@app.get("/trees/", response_model=List[TreeResponse])
def read_trees_endpoint(db: Session = Depends(get_database)):
    return get_trees(db)


@app.get("/trees/{tree_id}", response_model=TreeResponse)
def read_tree_endpoint(tree_id: int, db: Session = Depends(get_database)):
    tree = get_tree(db, tree_id)
    if not tree:
        raise HTTPException(status_code=404, detail="Tree not found")
    return tree


@app.put("/trees/{tree_id}", response_model=TreeResponse)
def update_tree_endpoint(
    tree_id: int, updated_tree: TreeUpdate, db: Session = Depends(get_database)
):
    tree = update_tree(db, tree_id, Tree(**updated_tree.dict()))
    if not tree:
        raise HTTPException(status_code=404, detail="Tree not found")
    return tree


@app.delete("/trees/{tree_id}")
def delete_tree_endpoint(tree_id: int, db: Session = Depends(get_database)):
    if not delete_tree(db, tree_id):
        raise HTTPException(status_code=404, detail="Tree not found")
    return {"message": "Tree deleted successfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
