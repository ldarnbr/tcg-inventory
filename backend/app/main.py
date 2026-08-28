# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI

app = FastAPI(title="TCG Inventory API")

@app.get("/")
async def root():
    return {"message": "TCG Inventory API Welcome Message"}