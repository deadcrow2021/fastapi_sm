from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.routing import Mount, APIRoute

# @app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('home.html', context={'request': request})

routes = [
    APIRoute('/', endpoint=home),
    Mount('/static', StaticFiles(directory='static'), name='static'),
]
templates = Jinja2Templates(directory='templates')



app = FastAPI(routes=routes)