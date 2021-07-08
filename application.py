from fastapi import FastAPI
from src.routes import hello

def create_app() -> FastAPI:
    app = FastAPI()    
    app.include_router(hello.router)
    return app

app = create_app()