# Proyecto 4: Backend Comercio 🛒

Este proyecto es una API RESTful desarrollada con **FastAPI** y **MongoDB**. Está diseñada para gestionar productos y órdenes de compra en un sistema de comercio electrónico. Es parte de un portafolio backend para demostrar habilidades en el desarrollo de APIs modernas.

---

## 🚀 Características

- **Gestión de productos**: CRUD completo para productos.
- **Gestión de órdenes**: Crear, consultar y eliminar órdenes de compra.
- **Conexión a MongoDB**: Base de datos NoSQL para almacenamiento de datos.
- **Validación de datos**: Uso de Pydantic para garantizar la integridad de los datos.
- **Documentación automática**: Swagger UI y ReDoc generados automáticamente.
- **Serialización personalizada**: Manejo de `ObjectId` de MongoDB para compatibilidad con JSON.

---

## 📋 Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente:

- **Python 3.10 o superior**
- **MongoDB** (local o en la nube, como MongoDB Atlas)
- **Git** (opcional, para clonar el repositorio)

---

## 📦 Instalación y configuración

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

### 1. Clona el repositorio
```bash
git clone https://github.com/palmaant/portafolio-backend.git
cd portafolio-backend/proyectos/proyecto4-backend-comercio
```

### 2. Crea y activa un entorno virtual

#### En Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### En Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```env
MONGO_DETAILS=mongodb://localhost:27017
MONGO_DB=commerce_db
SECRET_KEY=<clave_secreta>
```

Asegúrate de que el archivo `.env` no se suba al repositorio para proteger datos sensibles.

### 5. Inicia el servidor
```bash
uvicorn app.main:app --reload
```

### 6. Accede a la documentación interactiva
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📖 Documentación de la API

### Productos 📦

- **Listar productos**
  - **GET** `/products`

- **Crear producto**
  - **POST** `/products`
  - **Cuerpo de la solicitud**:
    ```json
    {
      "name": "Producto A",
      "description": "Descripción del producto",
      "price": 100.0,
      "stock": 10
    }
    ```

- **Obtener producto por ID**
  - **GET** `/products/{id}`

- **Actualizar producto**
  - **PUT** `/products/{id}`

- **Eliminar producto**
  - **DELETE** `/products/{id}`

### Órdenes 🧾

- **Crear orden**
  - **POST** `/orders`
  - **Cuerpo de la solicitud**:
    ```json
    {
      "products": [
        { "product_id": "ID_DEL_PRODUCTO", "quantity": 2 }
      ],
      "total_price": 200.0,
      "status": "pending"
    }
    ```

- **Consultar todas las órdenes**
  - **GET** `/orders`

- **Consultar orden por ID**
  - **GET** `/orders/orders/{id}`

- **Eliminar orden**
  - **DELETE** `/orders/orders/{id}`

---

## 🧪 Pruebas

### Pruebas en Swagger UI
1. Ve a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
2. Prueba los endpoints interactivos.

### Pruebas en la terminal

#### Crear una orden
```bash
curl -X POST http://127.0.0.1:8000/orders/ \
-H "Content-Type: application/json" \
-d '{
  "products": [{"product_id": "ID_DEL_PRODUCTO", "quantity": 2}],
  "total_price": 200.0,
  "status": "pending"
}'
```

#### Consultar todas las órdenes
```bash
curl -X GET http://127.0.0.1:8000/orders/
```

#### Consultar una orden por ID
```bash
curl -X GET http://127.0.0.1:8000/orders/orders/{id}
```

#### Eliminar una orden
```bash
curl -X DELETE http://127.0.0.1:8000/orders/orders/{id}
```

---

## 📅 Próximos pasos

- Agregar autenticación y autorización.
- Implementar paginación en los endpoints de consulta.
- Mejorar el manejo de errores y validaciones.
- Dockerizar la aplicación para facilitar el despliegue.

---

## 📝 Notas adicionales

- Este proyecto es una API backend diseñada para demostrar habilidades en el desarrollo de APIs RESTful.
- Puedes extender esta API agregando nuevas funcionalidades o integraciones con otros servicios.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.