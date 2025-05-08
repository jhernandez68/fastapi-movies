# FastAPI Movies

Un backend sencillo para gestionar películas y géneros, construido con FastAPI y SQLAlchemy.

Repositorio: [jhernandez68/fastapi-movies](https://github.com/jhernandez68/fastapi-movies)

---

## 📦 Características

- CRUD de géneros (`/genres`)
- CRUD de películas (`/movies`)
- Relación de cada película con un género
- Documentación automática via OpenAPI (Swagger UI)

---

## 🚀 Instalación

1. Clonar el repositorio  
   ```bash
   git clone https://github.com/jhernandez68/fastapi-movies.git
   cd fastapi-movies
2. Crear y activar un entorno virtual
  python -m venv .venv
  source .venv/bin/activate   # Linux / macOS
  .venv\Scripts\activate      # Windows
3. Instalar dependencias
    pip install -r requirements.txt
4. Crear la base de datos y ejecutar migraciones
    alembic upgrade head
