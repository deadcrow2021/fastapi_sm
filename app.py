from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src.models import Base, Todo
from src.database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory='templates')
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return templates.TemplateResponse('home.html', context={'request': request, 'todos': todos})


@app.post("/add/")
async def add(request: Request, title: str = Form(), db: Session = Depends(get_db)):
    new_todo = Todo(title=title)
    db.add(new_todo)
    db.commit()
    
    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/update/{todo_id}")
async def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()
    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get("/delete/{todo_id}")
async def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
