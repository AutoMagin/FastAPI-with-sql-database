from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def zakaz():
    raise HTTPException(status_code=403, detail="По приколу")