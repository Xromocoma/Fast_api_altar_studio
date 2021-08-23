from fastapi import FastAPI
from app.routers.v1.urls import router
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

origins = [
    "http://0.0.0.0:80",
    "http://0.0.0.0:8080",
]

app = FastAPI(openapi_url=f"{settings.API_V1}/openapi.json")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(router, prefix=settings.API_V1)
