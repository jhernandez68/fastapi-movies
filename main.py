import os
from fastapi import Body, FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from src.Settings import Settings
from fastapi.middleware.cors import CORSMiddleware


from src.modules.auth.routers import auth_users_router
from src.modules.movies.routers import genres_router
from src.modules.movies.routers import movies_router

# Verificar y crear la carpeta 'static' si no existe
static_dir = "static"
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

settings = Settings()
app = FastAPI()
origins = [
    "*"
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"message": "API for Backend of SimpleMovies is running"}


app.include_router(auth_users_router.router)
app.include_router(genres_router.router)
app.include_router(movies_router.router)