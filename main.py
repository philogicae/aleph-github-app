from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.post("/webhook")
def webhook(content):
    return {"status": "ok"}