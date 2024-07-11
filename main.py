from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Mem

# Подключение к базе данных
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db:5432/memdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание FastAPI приложения
app = FastAPI()

# GET /memes
@app.get("/memes")
def get_memes():
    db = SessionLocal()
    memes = db.query(Mem).all()
    db.close()
    return memes

# GET /memes/{id}
@app.get("/memes/{id}")
def get_mem(id: int):
    db = SessionLocal()
    mem = db.query(Mem).filter(Mem.id == id).first()
    db.close()
    if mem is None:
        raise HTTPException(status_code=404, detail="Mem not found")
    return mem

# POST /memes
@app.post("/memes")
def create_mem(text: str, image_url: str):
    db = SessionLocal()
    new_mem = Mem(text=text, image_url=image_url)
    db.add(new_mem)
    db.commit()
    db.refresh(new_mem)
    db.close()
    return new_mem

# PUT /memes/{id}
@app.put("/memes/{id}")
def update_mem(id: int, text: str, image_url: str):
    db = SessionLocal()
    mem = db.query(Mem).filter(Mem.id == id).first()
    if mem is None:
        raise HTTPException(status_code=404, detail="Mem not found")
    mem.text = text
    mem.image_url = image_url
    db.commit()
    db.refresh(mem)
    db.close()
    return mem

# DELETE /memes/{id}
@app.delete("/memes/{id}")
def delete_mem(id: int):
    db = SessionLocal()
    mem = db.query(Mem).filter(Mem.id == id).first()
    if mem is None:
        raise HTTPException(status_code=404, detail="Mem not found")
    db.delete(mem)
    db.commit()
    db.close()
    return {"message": "Mem deleted"}
