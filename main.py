from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
  return "Главная страница"

@app.get("/user")
async def auser(username: str, age: str) -> dict:
  return {f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

@app.get("/user/admin")
async def admin():
  return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def new(user_id: str) -> dict:
  return {"message": f"Вы вошли как № {user_id}"}



