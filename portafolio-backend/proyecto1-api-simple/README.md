# API Simple con FastAPI

Este es un proyecto de API simple desarrollado con **FastAPI** y **MongoDB**. Es parte de un portafolio de proyectos backend para demostrar habilidades en el desarrollo de APIs RESTful.

## 🚀 Características

- CRUD completo (Crear, Leer, Actualizar, Eliminar) para una colección de ítems.
- Conexión a una base de datos MongoDB.
- Documentación automática generada por FastAPI (Swagger UI y ReDoc).

## 📂 Estructura del proyecto

```
proyecto1-api-simple/
├── app/
│   ├── __init__.py
│   ├── main.py        # Punto de entrada de la aplicación
│   ├── database.py    # Configuración de la conexión a MongoDB
│   ├── routes.py      # Rutas de la API
├── venv/              # Entorno virtual (opcional)
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Documentación del proyecto
```

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- **FastAPI**
- **MongoDB**
- **Uvicorn** (servidor ASGI)

## 📦 Instalación y configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd proyecto1-api-simple
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   pip install -r requirements.txt
   ```

3. Asegúrate de que MongoDB esté corriendo en `localhost:27017`.

4. Inicia el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Accede a la API en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 📖 Documentación de la API

La API incluye documentación interactiva generada automáticamente por FastAPI:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🛠️ Endpoints

### **1. Crear un ítem**
- **POST** `/items`
- **Cuerpo de la solicitud**:
  ```json
  {
      "name": "Laptop",
      "description": "Una laptop de alta gama",
      "price": 1500.99,
      "in_stock": true
  }
  ```
- **Respuesta**:
  ```json
  {
      "id": "644b1f2e5f1b2c3d4e5f6789",
      "name": "Laptop",
      "description": "Una laptop de alta gama",
      "price": 1500.99,
      "in_stock": true
  }
  ```

### **2. Obtener todos los ítems**
- **GET** `/items`
- **Respuesta**:
  ```json
  [
      {
          "id": "644b1f2e5f1b2c3d4e5f6789",
          "name": "Laptop",
          "description": "Una laptop de alta gama",
          "price": 1500.99,
          "in_stock": true
      }
  ]
  ```

### **3. Obtener un ítem por ID**
- **GET** `/items/{item_id}`
- **Respuesta**:
  ```json
  {
      "id": "644b1f2e5f1b2c3d4e5f6789",
      "name": "Laptop",
      "description": "Una laptop de alta gama",
      "price": 1500.99,
      "in_stock": true
  }
  ```

### **4. Actualizar un ítem**
- **PUT** `/items/{item_id}`
- **Cuerpo de la solicitud**:
  ```json
  {
      "name": "Laptop Actualizada",
      "description": "Una laptop con más RAM",
      "price": 1800.99,
      "in_stock": true
  }
  ```
- **Respuesta**:
  ```json
  {
      "id": "644b1f2e5f1b2c3d4e5f6789",
      "name": "Laptop Actualizada",
      "description": "Una laptop con más RAM",
      "price": 1800.99,
      "in_stock": true
  }
  ```

### **5. Eliminar un ítem**
- **DELETE** `/items/{item_id}`
- **Respuesta**:
  ```json
  {
      "id": "644b1f2e5f1b2c3d4e5f6789",
      "name": "Laptop",
      "description": "Una laptop de alta gama",
      "price": 1500.99,
      "in_stock": true
  }
  ```

## 📝 Notas adicionales

- Este proyecto es una API simple diseñada para demostrar habilidades en el desarrollo backend.
- Puedes extender esta API agregando autenticación, validaciones avanzadas o integraciones con otras tecnologías.

---