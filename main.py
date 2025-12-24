from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

# Crear la aplicación
app = FastAPI(title="Mi App Básica")

# Montar archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar templates HTML
templates = Jinja2Templates(directory="templates")

# Página principal
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "mensaje": "¡Hola desde FastAPI!"}
    )

# Ejemplo de API endpoint
@app.get("/api/saludo/{nombre}")
async def saludar(nombre: str):
    return {"mensaje": f"Hola, {nombre}!"}

# Ejemplo POST
@app.post("/api/enviar")
async def recibir_datos(data: dict):
    return {"recibido": data, "respuesta": "Datos recibidos correctamente"}

# Para desarrollo
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)