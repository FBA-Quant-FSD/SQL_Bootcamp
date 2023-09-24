from fastapi import FASTAPI

app = FastAPI()

#API Endpoint
@app.get("/api-endpoint")
async def first_api():      #async : 필수 x
    return {'message': 'Hello Eric!'}