import uvicorn
from fastapi import FastAPI

from api.endpoints.moderate import nsfw_r

app = FastAPI()
app.include_router(nsfw_r)

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )
