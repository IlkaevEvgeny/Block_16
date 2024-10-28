from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
  id: int
  username: str
  age: int

@app.get("/users")
async def get_user() -> list[User]:
  return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',\
      example='UrbanUser')], age: int=Path(ge=18, le=120, description='Enter age', example='24')) -> dict:

    if not users:
        new_id = 1
    else:
        existing_ids = set([user.id for user in users])
        for i in range(1, 101):
            if i not in existing_ids:
                new_id = i
                break
        else:
            new_id = len(users) + 1

    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',\
      example='UrbanUser')],\
      user_id: int=Path(ge=1, le=100, description='Enter User ID',example='1'),\
      age: int=Path(ge=18, le=120, description='Enter age', example='43')) -> dict:

    for user in users:
      if user.id == user_id:
        user.username = username
        user.age = age
        return user
      else: raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example = '1')) -> dict:

    for index, user in enumerate(users):
      if user.id == user_id:
        users.pop(index)
        return users
      else: raise HTTPException(status_code=404, detail="User not found")

# uvicorn main:app --reload
# http://127.0.0.1:8000
