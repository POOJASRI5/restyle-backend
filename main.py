from fastapi import FastAPI
from database import engine

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ReStyle Backend Running"}

@app.get("/test-db")
def test_db():
    try:
        connection = engine.connect()
        connection.close()
        return {"message": "Database Connected Successfully"}
    except Exception as e:
        return {"error": str(e)}