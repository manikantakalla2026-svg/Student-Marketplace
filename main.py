from fastapi import FastAPI
from routes.item_routes import router

app = FastAPI()

# connect routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Student Marketplace backend running"}
