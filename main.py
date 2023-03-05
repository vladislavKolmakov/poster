from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from core.config import SessionLocal
from routes import router

app = FastAPI(
    title='Poster'
)

@app.middleware('http')
async def db_session_midlwere(request: Request, call_next):
    response = Response('internal server error', status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(response)
    finally:
        request.state.db.close()
    return response


app.include_router(router)