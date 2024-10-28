from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome():
  return "Главная страница"

@app.get("/user/{username}/{age}")
async def auser(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')], age: int=Path(ge=18, le=120, description='Enter age',example='24' )) -> dict:
  return {f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

@app.get("/user/admin")
async def admin():
  return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def new(user_id: int = Path(ge=1, le=100, description='Enter User ID', example = '1')) -> dict:
  return {"message": f"Вы вошли как № {user_id}"}

# uvicorn main:app --reload
# http://127.0.0.1:8000
