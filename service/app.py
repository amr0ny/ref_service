from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from repository import RefRepository
from database import init_db
from settings import logger
from uuid import UUID


app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.debug(f"Request URL: {request.url}")
    response = await call_next(request)
    return response

@app.get('/{link_id}')
async def redirect_to_ref(link_id: UUID, request: Request):
    ref = RefRepository.get_next_ref(link_id, request)
    if not ref:
        detail = 'Link not found or no references available, or IP has already accessed'
        logger.error(detail)
        raise HTTPException(404, detail=detail)
    logger.info(f'Redirected to: {ref.url}')
    return RedirectResponse(url=ref.url)