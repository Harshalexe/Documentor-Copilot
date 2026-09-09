from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import Settings
import uvicorn

#Entry point of our application

app = FastAPI(title="Documentor-Copilot")
app.add_middleware(
    CORSMiddleware, # this allows the frontend/ any links to access the backend APIs. eg. links in allow origins can access the backend APIs. This is important for security reasons, as it prevents unauthorized access to your backend from other domains.
    allow_origins= Settings().cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#async allows the function to run multiple tasks concurrently, which is useful for handling multiple requests at the same time without blocking the server. This is especially important in web applications where you want to be able to handle many requests simultaneously without slowing down the response time for each individual request.

@app.get("/health")
async def health()-> dict[str,str]: 
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1",port=8000)

