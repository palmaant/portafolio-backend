# Proyecto 2: API de Autenticación de Usuarios

## Descripción
Esta es una API desarrollada con **FastAPI** que permite la autenticación de usuarios mediante registro, inicio de sesión y generación de tokens JWT. Los datos de los usuarios se almacenan en una base de datos MongoDB.

---

## Características
- Registro de usuarios con encriptación de contraseñas.
- Inicio de sesión con generación de tokens JWT.
- Validación de correos electrónicos.
- Almacenamiento de datos en MongoDB.
- Documentación interactiva generada automáticamente con Swagger UI.

---

## Requisitos previos
Antes de comenzar, asegúrate de tener instalado lo siguiente:
- **Python 3.10 o superior** (se recomienda 3.13.2).
- **MongoDB** (local o en la nube, como MongoDB Atlas).

---

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd proyecto2-autenticacion-usuarios
   ```

2. **Crea y activa un entorno virtual**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno**:
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```env
   MONGO_DETAILS=mongodb://localhost:27017
   SECRET_KEY=tu_clave_secreta_super_segura
   ```

   - `MONGO_DETAILS`: URL de conexión a MongoDB.
   - `SECRET_KEY`: Clave secreta para firmar los tokens JWT.

5. **Inicia el servidor**:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

6. **Accede a la documentación interactiva**:
   Abre tu navegador y ve a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## Dependencias
El proyecto utiliza las siguientes dependencias, que están listadas en `requirements.txt`:

```plaintext
annotated-types==0.7.0
anyio==4.9.0
bcrypt==4.3.0
click==8.1.8
colorama==0.4.6
dnspython==2.7.0
ecdsa==0.19.1
email-validator==2.2.0
fastapi==0.115.12
h11==0.16.0
idna==3.10
motor==3.7.0
passlib==1.7.4
pyasn1==0.4.8
pydantic==2.11.3
pydantic_core==2.33.1
pymongo==4.12.0
python-dotenv==1.1.0
python-jose==3.4.0
uvicorn==0.23.2
```

---

## Endpoints

### **1. Endpoint raíz**
- **URL**: `GET /`
- **Descripción**: Devuelve un mensaje de bienvenida.
- **Respuesta**:
  ```json
  {
      "message": "Bienvenido a la API de Autenticación de Usuarios"
  }
  ```

### **2. Registro de usuario**
- **URL**: `POST /register`
- **Descripción**: Registra un nuevo usuario.
- **Cuerpo de la solicitud**:
  ```json
  {
      "username": "usuario1",
      "email": "usuario1@example.com",
      "password": "password123"
  }
  ```
- **Respuesta**:
  ```json
  {
      "message": "Usuario registrado exitosamente"
  }
  ```

### **3. Inicio de sesión**
- **URL**: `POST /login`
- **Descripción**: Inicia sesión y genera un token JWT.
- **Cuerpo de la solicitud**:
  ```json
  {
      "email": "usuario1@example.com",
      "password": "password123"
  }
  ```
- **Respuesta**:
  ```json
  {
      "access_token": "<token_generado>",
      "token_type": "bearer"
  }
  ```

---

## Interacción con MongoDB

### **Verificar usuarios registrados**
1. Abre la shell de MongoDB:
   ```bash
   mongosh
   ```
2. Cambia a la base de datos:
   ```bash
   use auth_db
   ```
3. Consulta los usuarios registrados:
   ```bash
   db.users.find().pretty()
   ```

---

## Pruebas

### **Pruebas en Swagger UI**
1. Ve a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
2. Prueba los endpoints interactivos.

### **Pruebas en la terminal**
#### **Prueba el endpoint raíz (`GET /`)**
```bash
curl -X GET http://127.0.0.1:8000/
```

#### **Prueba el registro de usuario (`POST /register`)**
```bash
curl -X POST http://127.0.0.1:8000/register \
-H "Content-Type: application/json" \
-d '{"username": "usuario1", "email": "usuario1@example.com", "password": "password123"}'
```

#### **Prueba el inicio de sesión (`POST /login`)**
```bash
curl -X POST http://127.0.0.1:8000/login \
-H "Content-Type: application/json" \
-d '{"email": "usuario1@example.com", "password": "password123"}'
```

---

## Problema conocido: Error con `bcrypt` y `passlib`

### **Descripción**
Al ejecutar la aplicación, es posible que aparezca el siguiente mensaje en los logs:

```
(trapped) error reading bcrypt version
Traceback (most recent call last):
  File "C:\...\bcrypt.py", line 620, in _load_backend_mixin
    version = _bcrypt.__about__.__version__
AttributeError: module 'bcrypt' has no attribute '__about__'
```

Este error ocurre porque `passlib` intenta acceder a un atributo (`__about__.__version__`) que ya no existe en las versiones más recientes de `bcrypt` (4.x en adelante). Aunque el error no afecta directamente el funcionamiento de la aplicación (por ejemplo, el registro de usuarios sigue funcionando correctamente), es recomendable solucionarlo para evitar problemas futuros.

---

### **Solución**
1. **Desinstalar la versión actual de `bcrypt`**:
   ```bash
   pip uninstall bcrypt
   ```

2. **Instalar una versión compatible de `bcrypt`**:
   ```bash
   pip install bcrypt==3.2.0
   ```

3. **Actualizar `requirements.txt`**:
   Una vez instalada la versión compatible, actualiza el archivo `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

4. **Reiniciar el servidor**:
   Detén el servidor actual y reinícialo:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

---

## Próximos pasos
- Implementar rutas protegidas con autenticación JWT.
- Agregar roles de usuario (administrador y usuario).
- Implementar recuperación de contraseñas.
- Desplegar la API en un servicio en la nube.

---

## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---