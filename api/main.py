from fastapi import FastAPI
from routers import immigrants, population, unemployment, neighborhoods

app = FastAPI()

#incluimos los endpoints del fichero de acceso
app.include_router(immigrants.router)
app.include_router(population.router)
app.include_router(unemployment.router)
app.include_router(neighborhoods.router)

@app.get("/")
def raiz():
    return {
        "message": "Bienvenido a mi API"
    }
