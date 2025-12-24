<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Instalación FastAPI + HTML App</title>
</head>
<body>
    <h1>Instalación y Configuración - FastAPI + HTML App</h1>
    <h2>1. Crear y activar entorno virtual</h2>
    <h3>Windows (CMD o PowerShell):</h3>
    <pre>
python -m venv venv
venv\Scripts\activate
    </pre>
    <h3>Linux/Mac:</h3>
    <pre>
python3 -m venv ldp
source ldp/bin/activate
    </pre>
    <p><strong>Nota:</strong> Deberías ver <code>(venv)</code> al inicio de la línea de comandos.</p>
    <h2>2. Instalar dependencias</h2>
    <pre>
pip install fastapi uvicorn jinja2 python-multipart
    </pre>
    <p>O si tienes el archivo requirements.txt:</p>
    <pre>
pip install -r requirements.txt
    </pre>
    <h2>3. Ejecutar el servidor</h2>
    <h3>Opción A: Con python directamente</h3>
    <pre>
python main.py
    </pre>
    <h3>Opción B: Con uvicorn (recomendado)</h3>
    <pre>
uvicorn main:app --reload
    </pre>
    <h2>4. Acceder a la aplicación</h2>
    <p><strong>Página principal:</strong> <a href="http://localhost:8000" target="_blank">http://localhost:8000</a></p>
    <p><strong>Documentación API:</strong> <a href="http://localhost:8000/docs" target="_blank">http://localhost:8000/docs</a></p>
    <p><strong>Documentación alternativa:</strong> <a href="http://localhost:8000/redoc" target="_blank">http://localhost:8000/redoc</a></p>
    <h2>5. Comandos rápidos de referencia</h2>
    <pre>
# Crear entorno
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Activar (Linux/Mac)
source venv/bin/activate

# Instalar paquetes
pip install fastapi uvicorn jinja2

# Ejecutar
uvicorn main:app --reload

# Detener servidor
Ctrl + C

# Desactivar entorno
deactivate
    </pre>
    <h2>6. Estructura de archivos necesaria</h2>
    <pre>
tu_proyecto/
├── main.py
├── requirements.txt (opcional)
├── templates/
│   └── index.html
└── static/
    └── style.css
    </pre>
    <h2>7. Solución de problemas comunes</h2>
    <p><strong>Error: "python no se reconoce"</strong></p>
    <pre>
# Usar python3 en algunos sistemas
python3 -m venv venv
    </pre>
    <p><strong>Error de permisos en Windows:</strong></p>
    <pre>
# Ejecutar PowerShell como administrador y usar:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    </pre>
    <p><strong>Error: Puerto en uso:</strong></p>
    <pre>
# Cambiar puerto
uvicorn main:app --port 8080 --reload
    </pre>
    <h2>8. Resumen de instalación rápida</h2>
    <pre>
# 1. Crear entorno
python -m venv venv

# 2. Activar
venv\Scripts\activate

# 3. Instalar
pip install fastapi uvicorn jinja2

# 4. Ejecutar
uvicorn main:app --reload
    </pre>
    <p><strong>¡Listo! La aplicación estará corriendo en http://localhost:8000</strong></p>
</body>
</html>