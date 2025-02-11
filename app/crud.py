from sqlalchemy.orm import Session
from models import Tree


def create_tree(db: Session, tree: Tree):
    db.add(tree)
    db.commit()
    db.refresh(tree)
    return tree


def get_trees(db: Session):
    return db.query(Tree).all()


def get_tree(db: Session, tree_id: int):
    return db.get(Tree, tree_id)


def update_tree(db: Session, tree_id: int, updated_tree: Tree):
    tree = db.get(Tree, tree_id)
    if not tree:
        return None
    tree.name = updated_tree.name
    tree.age = updated_tree.age
    tree.height = updated_tree.height
    db.commit()
    db.refresh(tree)
    return tree


def delete_tree(db: Session, tree_id: int):
    tree = db.get(Tree, tree_id)
    if not tree:
        return None
    db.delete(tree)
    db.commit()
    return True
