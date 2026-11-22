from fastapi import FastAPI
from schemas.api import ApiResponse

app = FastAPI()

@app.get("/users")
def get_users():
    print("getting users!")
    return {"users": ["ankith", "sachin", "rahul"]}


#@app.get("/", response_model=ApiResponse)
#def home():
 #   print("its working!")
  #  return {"message": "hey this is working fine", "success": True, "status": "ok"}


#@app.get("/get-users")
#def get_users():
 ##  return {"users": ["ankith", "sachin", "rahul"]}
